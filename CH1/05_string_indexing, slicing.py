"""
TODO: 문자열 인덱싱(indexing)
변수 a에 저장한 문자열의 각 문자마다 번호
"""

a="Life is too short, You need Python"

print(a[0]) # L
print(a[3]) # e
print(a[-1]) # n
print(a[-0]) # L # ! a[-0]은 a[0]과 같다!




"""
TODO: 문자열 슬라이싱(slicing)
문자열에서 단순히 한 문자만을 뽑아 내는 것이 아니라 ‘Life’ 또는 ‘You’와 같은 단어를 뽑아 내는 방법
"""

a="Life is too short, You need Python"

print(a[0:6]) # Life i
print(a[2:]) # fe is too short, You need Python
print(a[:3]) # Lif
print(a[:]) # Life is too short, You need Python
print(a[3:-3]) # e is too short, You need Pyt

a="20241011Sunny"

data=a[:8]
weather=a[8:]
print(data) # 20241011
print(weather) # Sunny


# 문자열 단어 치환
# ! 파이썬에서 문자열은 불변(immutable)하기 때문에 오류 발생
# a="Pithon"
# a[1]="y"
# print(a[1])

# ! 따라서 아래와 같이 슬라이싱을 사용해 문자열 단어 치환
a[:1] # p
a[2:] # thon
a=a[:1]+"y"+a[2:]
print(a) # Python

