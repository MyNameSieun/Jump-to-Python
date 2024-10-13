'''
# ! 중요

# 파이썬이 기존 언어와 다른 연산자를 채택하고 있는데, 그걸 아는 것이 중요
# 1. c언어에선 //는 주석인데 python에선 연산자로 쓰임!
# 2. c언어엔 있는데 python엔 없는 것: 지수 연산자 print(a**b), 몫 연산자: print(a//b)

'''

a=3
b=4
c=5
d=6

# 1. 사칙 연산자
print(a+b) # 7
print(a-b) # -1
print(a*b) # 12
print(a/b) # 0.75

# 2. 지수 연산자
print(a**b) # 81

# 3. 나머지 연산자
print(a%b) # 3

# 4. 몫 연산자
print(a//b) # 0


# 5. 복합 연산자
a+=1
print(a) # 4

a-=1
print(a) # 3

a*=1
print(a) #3

a/=2
print(a) # 1.5

b//=2
print(b) # 2

c%=2
print(c) # 1

d**=2
print(d) # 36
 

