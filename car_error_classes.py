class ErrorClass(Exception):
    pass

class LowMovementError(ErrorClass):
    def __init__(self, message="이동 횟수는 1 이상이어야 합니다."):
        self.message = message

class IllegalArgumentException(ErrorClass):
    def __init__(self, msg="잘못된 이름을 입력했습니다."):
        self.msg = msg
