"""
변수
- 파이썬은 변수에 저장된 값을 스스로 판단하여 자료형의 타입을 지정
- 데이터(객체)를 저장하는 공간의 주소를 가리킴

- C나 JAVA에서는 변수를 만들 때 자료형의 타입을 직접 지정해야 하지만, 
파이썬은 변수에 저장된 값을 스스로 판단하여 자료형의 타입을 지정하기 때문에 더 편리하다.

"""

# TODO: 변수의 복사 - 동일한 복사(복제)
a=[1,2,3]
b=a

print(a) # [1, 2, 3]
print(b) # [1, 2, 3]

print(id(a)) # 2167728427264
print(id(b)) # 2167728427264

print(a is b) # True


a[1]=4

print(a) # [1, 4, 3]
print(a is b) # True


# TODO: 변수의 복사 - [:] 이용하여 다르게 복사
a=[1,2,3]
b=a[:]

print(a) # [1, 2, 3]
print(b) # [1, 2, 3]

print(id(a)) # 1903041377984
print(id(b)) # 1903041374656

print(a is b) # False


# TODO: 변수의 복사 - copy 모듈 이용하여 다르게 복사
# ? form copy import copy 안해도 copy 되는 이유
a=[1,2,3]
b=a.copy()

print(a) # [1, 2, 3]
print(b) # [1, 2, 3]

print(id(a)) # 2181788260480
print(id(b)) # 2181790847936

print(a is b) # False


# TODO: 변수 만들기
# 튜플
a,b=("python","life")
(a,b)="python","life"

print(a) # python
print(b) # life
print(a,b) # python life
print((a,b)) # ('python', 'life')


# 리스트
[a,b]=["python","life"]


# 여러 개의 변수에 동일한 값을 대입
a=b="python"

print(a) # python
print(b) # python
print(a,b) # python python
print((a,b)) # ('python', 'python')


# 변수의 변경
a=3
b=5
a,b=b,a

print(a) # 5
print(b) # 3