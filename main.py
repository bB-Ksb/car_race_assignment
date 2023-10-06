from car_view import winner_car_print, RaceView
from car_error_classes import LowMovementError


def main():
    try:
        winner_car_print()

    except LowMovementError:
        RaceView.display_message(f"[ERROR]")


if __name__ == "__main__":
    main()
