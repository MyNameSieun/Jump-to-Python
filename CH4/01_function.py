
# TODO: 일반적인 함수

def add(a,b):
    return a+b

a=3
b=4
c=add(a,b)
print(c) # 7
 

# TODO: 입력값이 없는 함수
def say():
    print("hi")

say() # hi


# TODO: 리턴값이 없는 함수
def add(a,b):
    print("%d %d의 합은 %d 입니다."%(a,b,a+b))

a=add(3,4) # 3 4의 합은 7 입니다.

# ! 함수는 값을 반환하지 않기 때문에 print(a)를 하면 None이 출력더ㅣㄴ다.
print(a) # None


# TODO: 매개변수를 지정하여 호출
def sub(a,b):
    return a-b

result=sub(a=7,b=3) 
print(result) # 4

result=sub(b=5,a=3) 
print(result) # -2


# TODO: 입력값 갯수를 모를 때
# * 관례적인 사용: args
def add_many(*args):
    result=0
    for i in args:
        result=result+i # args에 입력받은 모든 값을 더한다.
    return result

result = add_many(1,2,3)
print(result) # 6

result = add_many(1,2,3,4,5,6,7,8,9)
print(result) # 55


# TODO: 입력값 수량을 모를 때
# 다양한 매개변수 추가
def add_mul(choice,*args):
    if choice=="add":
        result=0
        for i in args: result += i
    elif choice =="mul":
        result=1
        for i in args:result*=i
    return result

result=add_mul("add",1,2,3,4,5)
print(result) # 15

result=add_mul("mul",1,2,3,4,5)
print(result) # 120


# 키워드 매개변수, kwargs
# * 관례적인 사용: kwargs

def print_kwargs(**kwargs):
    print(kwargs)

# * 딕셔너리가 되며, 입력 값들은 해당 딕셔너리에 저장
print_kwargs(a=1) # {'a': 1}
print_kwargs(name="foo",age=3) # {'name': 'foo', 'age': 3}


# TODO: 매개변수에 초기값 미리 설정하기
# ! 초기값이 설정된 매개변수는 가장 뒤쪽에 위치해야한다.
def say_myself(name,age,man=True):
    print("나의 이름은 %s 입니다."%name)
    print("나이는 %d 살입니다."%age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용",27) # 나의 이름은 박응용 입니다.\n나이는 27 살입니다.\n남자입니다.
say_myself("박응용",27,True) # 나의 이름은 박응용 입니다.\n나이는 27 살입니다.\n남자입니다.
say_myself("박응선",27,False) # 나의 이름은 박응용 입니다.\n나이는 27 살입니다.\n여자입니다.



# TODO: 함수의 리턴값은 하나? 여러개?
# * 파이썬은 함수에서 여러 개의 값을 리턴할 때 tuple이라는 자료형으로 묶어서 리턴, 즉 함수는 튜플 하나를 리턴함
def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result) # (7,12)

result1,result2=add_and_mul(3,4)
print(result1) # 7
print(result2) # 12


# TODO: 함수 내부 변수의 유효 범위
# * 전역변수는 지역변수와 다른 별개의 변수로 취급

# 동일한 명칭으로 함수 외부에서 선언 & 내부에서 선언
a=1 # 전역 변수
def vartest(a):
    a=a+1 # 지역변수

vartest(a) 
print(a) # 1


# 명시적인 반환
a=1
def vartest(a):
    a=a+1
    return a

a=vartest(a)
print(a) # 2


# global 키워드 사용
a=1
def vartest():
    global a # 함수 밖에 있는 변수 a 사용
    a=a+1

vartest()
print(a) # 2


# TODO: lambda 예약어
# * 람다 예약어는 def와 동일한 역할이며, 한 줄의 간결한 사용 및 일회성 용도
# * return 명령어가 없어도 결과를 반환
add=lambda a,b:a+b
result=add(3,4)
print(result) # 7

