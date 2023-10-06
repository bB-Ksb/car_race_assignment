from car_controller import RaceController
class RaceView:
    @staticmethod
    def display_message(message):
        print(message)


def winner_car_print():
    """
    우승자를 출력 양식에 맞춰 출력하는 함수
    :return: 우승자1(, 우승자2)
    """
    winner_cars = RaceController()
    winner_cars = winner_cars.race()
    # TypeError: Missing 1 required positional argument: 'self' 방어
    if winner_cars:
        print("\n최종 우승자: ", end="")
        for won_car in range(len(winner_cars)):
            print_more_than_one_winner( won_car )
            print(winner_cars[won_car], end="")
        print()


def print_more_than_one_winner(won_car):
    """
    승리한 자동차가 1대 이상인 경우의 프린트
    :param won_car: 승리한 자동차의 이름
    :return: (예) pho, nim
    """
    if won_car > 0:
        print( ", ", end="" )