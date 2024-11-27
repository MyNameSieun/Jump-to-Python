# try-except.py
try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
    print(e)
except IndexError as e:
    print("인덱싱 할 수 없습니다.") # 인덱싱 할 수 없습니다.
    print(e) # list index out of range