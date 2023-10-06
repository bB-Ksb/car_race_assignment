from car_controller import winner_car_print
from car_error_classes import ErrorClass
from car_view import RaceView


def main():
    try:
        winner_car_print()

    except ErrorClass.LowMovementError:
        RaceView.display_message(f"[ERROR]")


if __name__ == "__main__":
    main()
