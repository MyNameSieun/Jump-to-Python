"""
TODO: 문자열 포매팅
문자열 안에 특정한 값을 삽입
"""

# 포맷 코드 %d를 이용한 숫자 대입
a= "I eat %d apples." % 3  
print(a) # I eat 3 apples.

number=3
a="I eat %d apples." %number 
print(a) # I eat 3 apples.

a="Error is %d%%." % 98
print(a) # Error is 98%.


# 포맷 코드 %s를 이용한 문자열 대입
# * %s는 전달된 값이 숫자든 문자열이든 관계없이, 해당 값을 문자열로 변환해 출력
a= "I have %s apples" % 3
print(a) # I have 3 apples

a= "I have %s apples" % 3.232
print(a) # I have 3.232 apples


# 2개 이상을 대입
number = 10
day="three"
a= "I ate %d apples. so I was sick for %s days." % (number,day)
print(a) # I ate 10 apples. so I was sick for three days.



"""
TODO: 포맷 코드와 숫자 함께 사용하기
- 양수면 뒤부터 정렬 후 앞에는 공백
- 음수면 앞부터 정렬 후 뒤에는 공백
"""

# 정렬과 공백
a="%s안녕" % "good" # 정렬x
print(a) # good안녕

a="%10s"%"hi"
print(a) #         hi

a="%-10s"%"hi"
print(a) # hi

a="%10shi" % "good" # 전체 길이가 10개인 문자열 공간에서 대입되는 값 오른쪽 정렬하고 그 앞 나머지 공백
print(a) #       goodhi

a="%-10shi" % "good"
print(a) # good      hi


# 소수점 표현하기
a="%0.4f"%3.42 # 출력 시 빈 자리를 0으로 채움
print(a) # 3.4200


a="%.4f" % 3.42
print(a) # 3.4200

a="%10.4f" % 3.42134234 # 전체길이 10개, 공백 4개
print(a) #     3.4213



"""
TODO: format 함수를 사용한 포매팅(1) 
"""
# 숫자 바로 대입하기
a="I eat {0} apples".format(3)
print(a) # I eat 3 apples

# 문자열 바로 대입하기
a="I eat {0} apples".format("five")
print(a) # I eat five apples

# 숫자 값을 가진 변수로 대입하기
number=3
a="I eat {0} apples".format(number)
print(a) # I eat 3 apples

# 2개 이상의 값 대입하기
number =3
string="five"

a= "I have {0} apples and my brother has {1}.".format(number,string) 
print(a) # I have 3 apples and my brother has five.

# 이름으로 대입하기
a= "I have {number} apples and my brother has {string}.".format(number=3,string="five") 
print(a) # I have 3 apples and my brother has five.


# 인덱스와 이름을 혼용해서 대입하기
a="I ate {0} apples. so I was sick for {day} days".format(10,day=3) 
print(a) # I ate 10 apples. so I was sick for 3 days



"""
TODO: format 함수를 사용한 포매팅(2) 
"""

# 왼쪽 정렬
a="{0:<10}".format("hi") 
print(a) # hi

# 오른쪽 정렬
a="{0:>10}".format("hi") 
print(a) #         hi

# 가운데 정렬
a="{0:^10}".format("hi") 
print(a) #     hi



"""
TODO: format 함수를 사용한 포매팅(3) 
"""
# 공백 채우기
a="{0:=^10}".format("hi")
print(a) # ====hi====

a="{0:!<10}".format("hi")
print(a) # hi!!!!!!!!


# 소수점 표현
a=3.4213424
b="{0:0.4f}".format(a)
print(b) # 3.4213

a=3.4213424
b="{0:10.4f}".format(a)
print(b) #     3.4213


# { 또는 } 문자 표현
a="{{ and }}".format()
print(a) # { and }


"""
TODO f문자열 포매팅
파이썬 3.6 ver 부터는 f 문자열 포매팅 기능을 사용
"""

# 문자열 앞에 f 접두사 이용
a=f"안녕하세여 {"감자"}입니다"
print(a)

name="박시은"
age=23

a=f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(a) # 나의 이름은 박시은입니다. 나이는 23입니다.

a=f"나는 내년이면 {age+1}살이 된다."
print(a) # 나는 내년이면 24살이 된다.


# 정렬
a=f"{"hi":<10}" # 왼쪽 정렬
print(a) # hi

a=f"{"hi":>10}" # 오른쪽 정렬
print(a) #         hi

a=f"{"hi":^10}" # 가운데 정렬
print(a) #     hi


# 공백 채우기
a=f'{"hi":=^10}' # 가운데 정렬하고 "=" 문자로 공백 채우기
print(a) # ====hi====

a=f'{"hi":!<10}' # 왼쪽 정렬하고 "!" 문자로 공백 채우기
print(a) # hi!!!!!!!!


# 소수점 표현
y=3.42134234

a= f"{y:0.4f}" # 소수점 4째자리까지만 표현
print(a) # 3.4213

a=f"{y:10.4f}" # 소수점 4째자리까지 표현하고 총 자리수를 10으로 맞춤
print(a) #     3.4213


# { 또는 } 문자 표현
a=f"{{ end }}"
print(a) # { end }

