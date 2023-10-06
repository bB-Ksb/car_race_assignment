from car_controller import RaceController


class RaceMsgView:
    @staticmethod
    def display_message(message):
        print( message )


def print_more_than_one_winner(won_car):
    """
    승리한 자동차가 1대 이상인 경우의 프린트
    :param won_car: 승리한 자동차의 이름
    :return: (예) pho, nim
    """
    if won_car > 0:
        print( ", ", end="" )


class GameResultPrint:
    def __init__(self):
        pass

    def print_winner_cars(self, winner_cars):
        """
        승리한 자동차(들) 출력
        들여쓰기 조건을 맞추기 위해 따로 전역 함수로 관리
        """
        for won_car in range( len( winner_cars ) ):
            print_more_than_one_winner( won_car )
            print( winner_cars[won_car], end="" )

    def winner_car_print(self, winner_cars):
        """
        우승자를 출력 양식에 맞춰 출력하는 함수
        :param winner_cars: 우승한 자동차 이름 리스트
        """
        if winner_cars:
            print( "\n최종 우승자: ", end="" )
            self.print_winner_cars( winner_cars )
            print()
