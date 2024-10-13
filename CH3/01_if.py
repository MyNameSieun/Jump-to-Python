"""
TODO: 기본 예제
"""

money=True
if money:
    print("택시를 타고 가라") 
else:
    print("걸어가라")

# 출력: 택시를 타고 가라


"""
TODO: 논리 연산자 (and, or, not)
"""
money=2000
card=True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라") 

# 출력: 택시를 타고 가라


"""
TODO: in, not in 연산자
- x in (리스트,튜플,딕셔너리 집합,문자열)
- x not in (리스트,튜플,딕셔너리 집합,문자열)
"""

print(1 in [1,2,3]) # True
print(1 not in [1,2,3]) # False

print(1 in (1,2,3)) # True
print(1 not in (1,2,3)) # False

# ! 주의 ! 딕셔너리에서 in 연산자를 사용하면, **딕셔너리의 키(key)**만을 확인하기 때문에 아래 코드는 False가 출력
print(1 in{"1":1, "2":2, "3":3}) # False

print(1 in {1,2,3}) # True
print("j" not in "python") # False


"""
TODO: if문과 in 연산자 결합
"""
pocket=["paper","cellphone","money"]
if "money" in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 출력: 택시를 타고 가라


# pass를 사용하면 건너뛰기 가능
pocket=["paper","cellphone","money"]
if "money" in pocket:
    pass
else:
    print("카드를 꺼내라")

# 출력: x


"""
TODO: elif 문
"""
pocket=["paper","cellphone"]
card=True

if "money" in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 출력: 택시를 타고 가라


"""
TODO: 조건부 표현식
변수 = 조건문이_참인_경우의_값  if  조건문  else  조건문이_거짓인_경우의_값
"""

# if score>=60:
#     message="success"
# else:
#     message="failure"

score=40
message="success" if score >=60 else "failure"
print(message) # failure




