from car_view import RaceMsgView, GameResultPrint
from car_error_classes import LowMovementError, IllegalArgumentException


def main():
    try:
        GameResultPrint.winner_car_print()

    except (LowMovementError(), IllegalArgumentException()):
        RaceMsgView.display_message( f"[ERROR]" )


if __name__ == "__main__":
    main()
