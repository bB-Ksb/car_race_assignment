from car_model import Car
from car_error_classes import LowMovementError, IllegalArgumentException


def get_valid_car_names():
    """
    조건에 적합할 때까지 자동차의 이름을 입력 받도록 하는 함수
    :return: 조건을 충족하는 자동차 이름들(,를 기준으로 구분됨)
    """
    while True:
        car_names_input = input( "경주할 자동차 이름을 입력하세요 (이름은 쉼표(,)로 구분):\n" )
        car_names_list = car_names_input.split( ',' )
        valid_names = []
        invalid_names = []

        # 이름 조건 충족 확인(5자 이하)
        name_length_condition( car_names_list, invalid_names, valid_names )

        if len( invalid_names ) != 0:
            each_invalid_car_names( invalid_names )
            continue

        if valid_names:
            return valid_names


def name_length_condition(car_names_list, invalid_names, valid_names):
    """
    리스트로 받은 자동차 이름들을 분리해줌
    """
    for car_name in car_names_list:
        car_name = car_name.strip()
        is_it_valid_invalid( car_name, invalid_names, valid_names )


def is_it_valid_invalid(car_name, invalid_names, valid_names):
    """
    자동차 이름이 조건에 맞는지 판별하는 함수
    """
    if len( car_name ) <= 5:
        valid_names.append( car_name )
    elif len( car_name ) > 5:
        invalid_names.append( car_name )


def each_invalid_car_names(invalid_names):
    """
    invalid_car_names 에서 (조건에 맞지 않는)자동차 이름 출력
    :param invalid_names: 조건에 충족하지 않는 자동차 이름들을 출력해줌
    :return: (예) 유효하지 않는 자동차 이름: abcdef, ghijk
    """
    print( f"유효하지 않는 자동차 이름: ", end="" )
    print( ", ".join( invalid_names ) )  # 들여쓰기 최소화
    # for name in invalid_names:
    #     print( f"유효하지 않은 자동차 이름: {name} (5자 이상 규칙 미준수)" )


class RaceController:
    def __init__(self):
        pass

    @staticmethod
    def valid_car_movement(cars, how_much_car_play):
        """
        게임에 플레이하는 자동차 이름에 대해, 어떤 차가 얼만큼 움직였는지 보여줌
        :param cars: 게임 플레이하는 자동차 이름(들)
        :param how_much_car_play: 몇 번 경주를 할 것인지
        :return: 경기 한 판 후 자동차의 이동 정보
        """
        for moving_number in range( how_much_car_play ):
            print( f"\n{moving_number + 1}번째 경주 결과: " )
            for car in cars:
                car.move()
                print( car )

    # @staticmethod
    @property
    def race(self):
        valid_car_name = get_valid_car_names()
        """
        자동차 게임 진행 시키는 메서드
        :return: 승리 조건을 충족한 자동차 이름(들) 돌려줌
        """
        try:
            car_names = valid_car_name
            how_much_car_play = int( input( f"시도할 회수는 몇 회인가요?\n" ) )

            if how_much_car_play <= 0:
                raise LowMovementError()

            cars = [Car( name ) for name in car_names]

            RaceController.valid_car_movement( cars, how_much_car_play )

            max_distance = max( car.distance for car in cars )
            winner_cars = [car.name for car in cars if car.distance == max_distance]
            return winner_cars

        except TypeError:
            raise IllegalArgumentException()
