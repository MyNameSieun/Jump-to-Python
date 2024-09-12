# 01_문자열 자료형

# 파이썬이 기존 언어와 다른 연산자를 채택하고 있는데, 그걸 아는 것이 중요
# 1. **c언어에선 //는 주석인데 python에선 연산자로 쓰임!**
# 2. c언어엔 있는데 python엔 없는 것: 지수 연산자 print(a**b), 몫 연산자: print(a//b)


#  실수형으로 나옴
a=3
b=4
a/b # 0.75



print("---------문자열 인덱싱------------------")

a="Life is too short, you need Python"
print(a[0]) # L
print(a[12]) # s
print(a[-1]) # n
print(a[-0]) # L


print("---------문자열 슬라이싱------------------")

a="Life is too short, you need Python"
print(a[0:4]) # Life
print(a[5:7]) # is
print(a[12:17]) # short
print(a[19:]) # you need Python
print(a[:17]) # Life is too short
print(a[19:-7]) # you need
print(a[:]) # Life is too short, you need Python


print("-----------문자열 단어 치환 ----------------")

## _인덱싱으로 새로운 메모리 주소 할당 받아야함
a="pithon"
print(a[:1]) # p
print(a[2:]) # thon
print(a[:1]+"y"+a[2:]) # python



print("----------문자열 포맷팅--------------------")
## 1. 포맷코드 %d 이용한 숫자 대입
print("I eat %d apples" % 3) # I eat 3 apples

## 2. 포맷코드 %s 이용한 문자열 대입
print("I eat %s apples" % "five") # I eat five apples

## 3. 2개 이상을 대입
number = 10
day="three"
print("I ate %d apples. so I was sick for %s days." % (number,day)) # I ate 10 apples. so I was sick for three days.


## 4. 번외) %c는 문자 1개 뿐만 아닌 숫자가 와도 된다.
print("I have %capples" % 3) # I have apples



print("------------문자열 포맷 코드에 숫자 이용----------")
## 1. 정렬과 공백 (ppt 메모리 할당 확인하기)
print("%5s" % "hi") #    hi

print("%-5ssieun" % "hi") # hi   sieun


## 2. 소수점 표현하기
print("%0.4f" % 3.141592) # 3.1416
print("%.4f" % 3.141592) # 3.1416
print("%10.4f" % 3.141592) #     3.1416


print("------------format 함수를 사용한 포매팅----------")
## 1. 숫자 바로 대입하기
print("I eat {0} apple".format(3)) # I eat 3 apple

## 2. 문자열 바로 대입하기
print("I eat {0} apples".format("five")) # I eat five apples

## 3. 숫자 값을 가진 변수로 대입하기
number=3
print("I eat {0} apples".format(number)) # I eat 3 apples


print("------------format 함수를 사용한 포매팅-cont. ----------")
## 1. 2개 이상의 값 대입하기
number=10
day="three"
print("I ate {0} apples. so I was sick for {1} days.".format(number,day)) # I ate 10 apples. so I was sick for three days.

## 2. 이름으로 대입하기
print("I ate {number} apples. so I was sick for {day} days.".format(number=10,day=3)) # I ate 10 apples. so I was sick for 3 days.

## 3. 인덱스와 이름을 혼용해서 대입하기
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3)) # I ate 10 apples. so I was sick for 3 days.


