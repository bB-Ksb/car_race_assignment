class ErrorClass:
    class LowMovementError(Exception):
        def __init__(self, message="이동 횟수는 1 이상이어야 합니다."):
            self.message = message

    class IllegalArgumentException(Exception):
        def __init__(self, msg="잘못된 입력입니다."):
            self.msg = msg
