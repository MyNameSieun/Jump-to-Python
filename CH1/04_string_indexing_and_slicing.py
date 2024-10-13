"""
TODO: 문자열 인덱싱(indexing)
- 인덱싱은 무언가를 “가리킨다” 라는 의미로, 문자열에서 개별 문자를 추출하려면 인덱싱을 사용한다.
- 인덱스는 0부터 시작하며, 음수 인덱스는 문자열의 끝에서부터 문자를 센다.
"""

a="Life is too short, You need Python"

print(a[0]) # L
print(a[3]) # e
print(a[-1]) # n
print(a[-0]) # L # ! a[-0]은 a[0]과 같다!




"""
TODO: 문자열 슬라이싱(slicing)
- 슬라이싱은 무언가를 “잘라낸다” 라는 의미로, 문자열의 특정 부분을 추출할 수 있다.
- 슬라이싱의 기본 구문은 [start:end]이다.
- start는 포함되며, end는 포함되지 않는다.
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

