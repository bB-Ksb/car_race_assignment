from car_model import Car
from car_error_classes import ErrorClass


def get_valid_car_names():
    """
    조건에 적합할 때까지 자동차의 이름을 입력 받도록 하는 함수
    :return: 조건을 충족하는 자동차 이름들(,를 기준으로 구분됨)
    """
    while True:
        car_names_input = input("경주할 자동차 이름을 입력하세요 (이름은 쉼표(,)로 구분):\n")
        car_names_list = car_names_input.split(',')
        valid_names = []
        invalid_names = []

        # 이름 조건 충족 확인(5자 이하)
        name_length_condition(car_names_list, invalid_names, valid_names)

        if len(invalid_names) != 0:
            each_invalid_car_names(invalid_names)
            continue

        if valid_names:
            return valid_names


def each_invalid_car_names(invalid_names):
    """
    invalid_car_names 에서 (조건에 맞지 않는)자동차 이름 출력
    :param invalid_names:
    :return:
    """
    for name in invalid_names:
        print( f"유효하지 않은 자동차 이름: {name} (5자 이상 규칙 미준수)" )


def name_length_condition(car_names_list, invalid_names, valid_names):
    """
    이름 길이가 5자 이하인지 확인하는 함수
    :param car_names_list:
    :param invalid_names:
    :param valid_names:
    :return:
    """
    for car_name in car_names_list:
        car_name = car_name.strip()
        is_it_valid_invalid( car_name, invalid_names, valid_names )


def is_it_valid_invalid(car_name, invalid_names, valid_names):
    """
    자동차 이름이 조건에 맞는지 판별하는 함수
    :param car_name:
    :param invalid_names:
    :param valid_names:
    :return:
    """
    if len( car_name ) <= 5:
        valid_names.append( car_name )
    elif len( car_name ) > 5:
        invalid_names.append( car_name )


class RaceController:
    def __init__(self):
        pass

    @staticmethod
    def race():
        valid_car_name = get_valid_car_names()
        """
        자동차 게임 진행 시키는 메서드
        :return: 승리 조건을 충족한 자동차 이름(들)
        """
        try:
            car_names = valid_car_name
            how_much_car_play = int(input(f"시도할 회수는 몇 회인가요?\n"))

            if how_much_car_play <= 0:
                raise ErrorClass.LowMovementError()

            cars = [Car(name) for name in car_names]

            for moving_number in range(how_much_car_play):
                print(f"\n{moving_number + 1}번째 경주 결과: ")
                for car in cars:
                    car.move()
                    print(car)

            max_distance = max(car.distance for car in cars)
            winner_cars = [car.name for car in cars if car.distance == max_distance]
            return winner_cars

        except TypeError:
            raise f"게임 로직 에러 발생"


def winner_car_print():
    """
    우승자를 출력 양식에 맞춰 출력해주는 함수
    :return: 우승자1(, 우승자2)
    """
    winner_cars = RaceController()
    winner_cars = winner_cars.race()
    # TypeError: Missing 1 required positional argument: 'self' 방어
    if winner_cars:
        print("\n최종 우승자: ", end="")
        for won_car in range(len(winner_cars)):
            if won_car > 0:
                print(", ", end="")
            print(winner_cars[won_car], end="")
        print()
