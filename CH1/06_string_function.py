"""
TODO: 문자열 관련 함수
"""

# 문자 개수 세기 - count
a="hobby"
print(a.count("b")) # 2


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



# 문자열 삽입 - join⭐
print(",".join("abcd")) # a,b,c,d

# 소문자를 대문자로 바꾸기 - upper
a="hobby"
print(a.upper()) # HOBBY 

# 대문자를 소문자로 바꾸기 - lower
a="hobby"
print(a.lower()) # hobby



# 왼쪽 공백 제거 - lstrip
a= "  hi  "
print(a.lstrip()) # hi

# 오른쪽 공백 제거 - rstrip
a= "  hi  "
print(a.rstrip()) #   hi

# 양쪽 공백 제거
a= "  hi  "
print(a.strip()) # hi



# 문자열 바꾸기 - replace
a="Life is too short"
a=a.replace("Life","Your leg")
print(a) # Your leg is too short



# 문자열 나누기 - split
a="Life is too short"
print(a.split()) # ['Life', 'is', 'too', 'short']

b="a:b:c:d"
print(b.split(":")) # ['a', 'b', 'c', 'd']