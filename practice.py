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

a="%10sGood"%"hi"
print(a) 

a="%-10sGood"%"hi"
print(a)


# 소수점 표현하기
a="%0.4f"%3.42324
print(a)# 3.4232

a="%.4f"%3.42324
print(a)

a="%10.4f"%3.42324
print(a) #   3.4232

a="I eat {0} {1}".format("감자",3)
print(a)

number=3
a="I eat {0}".format(number)
print(a)

number=10
string="5"
a="I {number} {string}".format(number=3,string="sdf")
print(a) 


number=14
a="I {0} {stw}".format(number,stw="4")
print(a)


a="{0:^10}".format("감자")
print(a)

a="{0:!^10}".format("기러기")
print(a)

a="{0:=<10}".format("등호!")
print(a)

a="{0:#^10}".format("안녕!")
print(a)


