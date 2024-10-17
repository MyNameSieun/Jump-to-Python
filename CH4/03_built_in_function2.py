"""
아스키코드는 1바이트, 유니코드는 3바이트
"""

# TODO: chr(i)
# * chr() 함수는 아스키 코드와 유니코드 값을 문자로 변환

# 유니코드
print(chr(0xac00)) # 가
print(chr(0xac01)) # 각
print(chr(0xac02)) # 갂
print(chr(0xac03)) # 갃
print(chr(0xac04)) # 간

# 아스키코드
print(chr(64)) # @
print(chr(65)) # A
print(chr(66)) # B


# TODO: ord(c)
# * 입력된 한 문자의 유니코드 숫자 값을 반환
# * ord() 함수는 아스키코드 및 유니코드 문자를 숫자로 변환 (한 개의 문자만 입력 가능)

a = ord("가")
print(a)  # 44032


# TODO: divmod(a,b)
# * a를 b로 나눈 몫과 나머지를 튜플로 반환

a=divmod(7,3)
print(a) # (2, 1)



# TODO: eval(표현식)
# * 문자열의 표현식을 입력 받아 이의 실행 결과를 반환

a=eval("1+2")
print(a) # 3

a=eval("divmod(4,3)")
print(a) # (1, 1)


# TODO: filter(x, y)
# * x 입력은 함수, y 입력은 반복 가능한 데이터 y 데이터를 x 함수에 적용, 결과가 참인 입력값만 묶어 반환

def positive(x): return x>0
a=list(filter(positive,[1,-3,2,0,-5,6]))
print(a) # [1, 2, 6]

a=list(filter(lambda x: x>0,[1,-3,2,0,-5,6]))
print(a) # [1, 2, 6]


# TODO:  hex(i)
# * 정수를 입력 받아 16진수 문자열로 반환

print(hex(234)) # 0xea


# TODO: oct(i)
# * 정수를 입력 받아 8진수 문자열로 반환

print(oct(34)) # 0o42


# TODO: id(x)
# * 입력값이 저장된 메모리 주소를 반환

a=3
print(id(a)) # 140709100636664


# TODO: tuple(x)
# * 반복 가능한 데이터를 튜플로 반환

print(tuple("abc")) # ('a', 'b', 'c')
print(tuple([1,2,3])) # (1, 2, 3)
print(tuple({1,2,3})) # (1, 2, 3)


# TODO:  type(x)
# *  x 입력값의 자료형을 반환

print(type([])) # <class 'list'>
print(type(open("test","w"))) # <class '_io.TextIOWrapper'>


# TODO: zip(x)
# * 반복 가능한 데이터를 여러 개 입력받아 묶음으로 반환

a=list(zip([1,2,3],[4,5,6]))
print(a) # [(1, 4), (2, 5), (3, 6)]

a=list(zip([1,2,3],[4,5,6],[7,8,9]))
print(a) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

a=list(zip("abc","def"))
print(a) # [('a', 'd'), ('b', 'e'), ('c', 'f')]

