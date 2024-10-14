# 문자열 길이 구하기
a="sdf"
print(len(a))

# 문자열 인덱싱
a="Life is too short"
print(a[0])
print(a[3])
print(a[-1])


# 문자열 슬라이싱
a="Life is too short"
print(a[0:3]) # Lif
print(a[3:]) # e is ...
print(a[2:3]) # f
print(a[:]) # ...
print(a[1:-1]) # i~r


# 문자열 단어 치환
a="pithon"
result=a[:1]+"y"+a[2:]
print(result)


# 문자열 포매팅
a="I eat %d apple"%3
print(a)

number=3
a="I eat %d apple"%number
print(a)

a="I eat %d%% apple"%3
print(a)


a="I eat %s apples"%"4"

number=10
day="tree"
a="I %d %s"%(number,day)
print(a)


a="%10s"%"hi"
print(a)

a="%-10s"%"hi"
print(a)