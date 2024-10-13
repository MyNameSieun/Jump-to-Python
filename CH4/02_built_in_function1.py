"""
내장 함수는 import 키워드 없이 바로 사용
반복 가능한 데이터: 문자열, 리스트, 튜플, 딕셔너리, 집합
"""


# TODO: abs(i)
# * 숫자를 입력받았을 때 그 절대값을 반환

a=abs(-3)
print(a) # 3


# TODO: all(x) 
# * 반복 가능한 데이터의 x의 모든 요소가 참이면 Ture, 하나라도 거짓이면 False를 반환

a=all([1,2,3,0])
b=all([])

print(a) # False
print(b) # True


# TODO: any(x)
# * all(x)와 반대로 동작

a=any([0,""])
b=any([])

print(a) # False
print(b) # False


# TODO: dir(x)
# * 객체가 지닌 변수나 함수를 보여 주는 함수

a=dir([1,2,3])
b=dir({"1":"a"})

print(a) # ['__add__', '__class__', '__class_getitem__', '__con ...
print(b) # ['__class__', '__class_getitem__', '__conta ...


# TODO: enumerate(x)
# * 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴

for i, name in enumerate(["body","foo,bar"]):
    print(i,name)

# 출력 결과
# 0 body
# 1 foo,bar


# TODO: input(입력)
# * 사용자 입력을 받아 문자열을 반환

a=input()
print(a)


# TODO: int(x)
# * 문자열 형태의 숫자나 실수형 숫자를 정수로 반환

a=int("3")
print(a) # 3 

a= int(3.4)
print(a) # 3


# TODO: int(x, radix) 
# * radix 진수로 표현된 문자열 x를 10진수로 반환

a=int("11",2)
print(a) # 3


# TODO: len(x)
# * 반복 가능한 데이터 입력값 x의 요소 개수, 즉 길이를 반환
print(len("python")) # 6


# TODO: isinstance(object, class)
# * 첫 번째 인수로 객체, 두 번째 인수로 클래스 입력으로 받은 객체가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 반환

class Person:pass
a = Person()
print(isinstance(a, Person)) # True


# TODO: list(x)
# * 반복 가능한 데이터를 입력 받아 리스트로 반환

print(list("python")) # ['p', 'y', 't', 'h', 'o', 'n']
print({1,2,3}) # {1, 2, 3}
print([1,2,3]) # [1, 2, 3]


# TODO: max(x)
# * 반복 가능한 데이터를 입력 받아 요소의 최대값을 반환

print(max("python")) # y


# TODO: min(x)
# * 반복 가능한 데이터를 입력 받아 요소의 최소값을 반환

print(min("python")) # h


# TODO: map(x, y)
# * 입력 y 데이터의 각 요소에 함수 x를 적용한 결과를 반환: x 입력은 함수, y 입력은 반복 가능한 데이터

def two_times(x):return x*2
a=list(map(two_times,[1,2,3,4]))
print(a) # [2, 4, 6, 8]

a=list(map(lambda a:a*2,[1,2,3,4]))
print(a) # [2, 4, 6, 8]


# TODO: open(x, y)
# * 접근한 파일 객체를 반환: x 입력은 파일명, y 입력은 파일 접근 모드

f=open("bin_file","rb")


# TODO: pow(x, y)
# * x 입력값을 y 입력값으로 제곱한 결과 반환

print(pow(2,4)) # 16


# TODO: range(x, y, z)
# * 입력된 숫자에 해당하는 범위 값을 반환: x 값은 시작점, y 값은 종점, z 값은 스텝: x, z 값은 생략 가능

a=list(range(5))
print(a) # [0, 1, 2, 3, 4]

a=list(range(5,10))
print(a) # [5, 6, 7, 8, 9]


a=list(range(1,10,2))
print(a) # [1, 3, 5, 7, 9]


# TODO: round(x, y)
# * x 값을 반올림한 결과를 반환: x 값은 숫자, y 값은 반올림 소수점의 자리수: y 값은 생략 가능

a=round(4.6)
print(a) # 5

a=round(5.678,2)
print(a) # 5.68


# TODO: sorted(x)
# * 반복 가능한 데이터를 정렬하여 리스트로 반환

a= sorted([3,1,2])
print(a) # [1, 2, 3]

a=sorted("zero") 
print(a) # ['e', 'o', 'r', 'z']

sorted({3,2,1})
print(a) # ['e', 'o', 'r', 'z']


# TODO: str(x)
# * x 입력값을 문자열 형태로 반환

print(str(3)) # "3"



# TODO: sum(x)
# * x 입력 데이터의 요소(item) 합을 반환: 요소는 숫자형

print(sum([1,2,3])) # 6


