# try-except-finally.py
try:
    a = [1, 2]
    print(a[3])
    4/0
except Exception as e:
    print("에러 발생: ", e) # 에러 발생:  list index out of range
finally:
    print("정상 종료합니다.") # 정상 종료합니다.