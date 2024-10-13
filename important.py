
# TODO: 지수표현 방식
a=4.24e10
print(a) # 42400000000.0

a=4.24E-10
print(a) # 4.24e-10


# TODO: 8진수 - 0o또는 0O로 시작
a=0o177;
print(a)


# TODO: 16진수 - 0x또는 0X로 시작
a=0x8ff;
print(a)

# TODO: 2진수 - 0b또는 0B로 시작
a = 0b1101  
print(a) # 13 


# TODO: Python c언어와 다른 점
# 1. 주석: 파이썬의 주석은 #, c언어의 주석은 //
print(2**3) # 2. 지수 연산자
print(7//3) # 3. 몫 연산자
print("python"+" is fun") # 4. 문자열 연산


# TODO: 문자열 길이 구하기
a="시은이는 예쁘다?"
print(len(a)) # 9


# TODO: 문자열 단어 치환
# ! 파이썬에서 문자열은 불변(immutable)하기 때문에 오류 발생
# a="Pithon"
# a[1]="y"
# print(a[1])

# ! 따라서 아래와 같이 슬라이싱을 사용해 문자열 단어 치환
a[:1] # p
a[2:] # thon
a=a[:1]+"y"+a[2:]
print(a) # Python


"""
TODO: 포맷 코드와 숫자 함께 사용하기
- 양수면 뒤부터 정렬 후 앞에는 공백
- 음수면 앞부터 정렬 후 뒤에는 공백
"""

# 정렬과 공백
a="%10s" % "hi" # 전체 길이가 10개인 문자열 공간에서 대입되는 값 오른쪽 정렬하고 그 앞 나머지 공백
print(a) #         hi (공백 8개)

# ? 이해 안됨 ppt chp2 17장
a="%-10shi" % "good"
print(a) # good      hi


# TODO: 소수점 표현하기
a="%0.4f"%3.42 # 출력 시 빈 자리를 0으로 채움
print(a) # 3.4200


a="%.4f" % 3.42
print(a) # 3.4200

a="%10.4f" % 3.42
print(a) #     3.4200


# TODO: format 함수를 사용한 포매팅(1) 
a="I {0} apple ".format(3)
print(a)

a="I {0} apple".format("eat")
print(a)

a="I have {number} {string}".format(number=3,string="감자")
print(a)


# TODO: format 함수를 사용한 포매팅(3) 
# 공백 채우기
a="{0:!<10}".format("3")
print(a)

a="{0:=^10}".format("!")
print(a)

"""
TODO f문자열 포매팅
파이썬 3.6 ver 부터는 f 문자열 포매팅 기능을 사용
"""

name="박시은"
age=23

a=f"나의 이름은 {name}입니다. 나이는 {age}입니다."
print(a) # 나의 이름은 박시은입니다. 나이는 23입니다.

a=f"나는 내년이면 {age+1}살이 된다."
print(a) # 나는 내년이면 24살이 된다.


# ! 위치를 알려주는 find와 index는 에러 처리에 차이가 있다.
# * 찾고자 하는 문자가 없을 때 find는 -1을 반환하지만 index는 Value Error를 반환한다!


# 위치 알려주기 1 - find
a="hobby"
print(a.find("b")) # 2
print(a.find("k")) # -1

# 위치 알려주기 2 - index
a="hobby"
print(a.index("b")) # 2
# print(a.index("k")) # *error 반환

