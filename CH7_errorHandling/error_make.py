# error_make.py

# 사용자 정의 예외 클래스
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

# 예외를 발생시키는 함수
def say_nick(nick):
    if nick == '바보':
        raise MyError()  # MyError 예외를 발생시킴
    print(nick)

# 예외 처리
try:
    say_nick("천사")
    say_nick("바보")  # 이 부분에서 예외가 발생
except MyError as e:
    print(e)  # "허용되지 않는 별명입니다." 출력