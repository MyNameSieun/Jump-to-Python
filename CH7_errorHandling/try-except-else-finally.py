# try-except-else-finally.py
try:
    x = int(input("10을 나눌 숫자를 입력: "))
    y = 10 / x
except ZeroDivisionError: # 에러가 발생했을 때 실행
    print("0으로 나누는 것은 불가") 
else: # 예외가 발생하지 않았을 때 실행
    print(y)
finally: # 예외 발생과 상관 없이 항상 실행
    print("코드 실행 종료")