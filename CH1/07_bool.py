"""
불(bool)
- 참과 거짓
- 항상 대문자(True / False)로 시작
"""

# TODO: Ture, False
a=True
b=False

print(type(a)) # <class 'bool'>
print(type(b)) # <class 'bool'>


# TODO: 조건문의 반환값
print(1==1) # True
print(2>1) # True
print(2<1) # False


"""
TODO 자료형의 Ture/False

# 문자형
"Python" - True
"" - Flase

# 리스트
[1,2,3] - True
[] - False

# 튜플
(1,2,3) - True
() - False

# 딕셔너리
{"a":1} - True
{} - False

# 숫자형
1 - True
0 - False

# 기타
None = False

"""
print(bool("Python")) # True
print(bool("")) # False

print(bool([1,2,3])) # True
print(bool([])) # False

print(bool((1,2,3))) # True
print(bool()) # False

# True: 참 (1로 취급), False: 거짓 (0으로 취급) 
# ! 0이 아닌 숫자 (예: -1, 1, 100 등): True로 변환
print(bool(1)) # True
print(bool(0)) # False
print(bool(-1)) # True


print(bool(None)) # False
