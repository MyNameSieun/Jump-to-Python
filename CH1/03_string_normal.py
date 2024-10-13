"""
TODO: 문자열 만드는 방법
"""

# 1. 쌍따옴표 이용
print("Hello World") # Hello World

# 2. 단따옴표 이용
print('Hello World') # Hello World

# 3. 쌍따옴표 3개 연속
print("""Hello World""") # Hello World

# 3. 단따옴표 3개 연속
print('''Hello World''') # Hello World

# 4. 여러 줄인 문자열
print("""      
Hello                # Hello
      World             #   World
""")


"""
TODO: 문자열 안에 따옴표 포함
"""
# 문자열에 단따옴표 포함
result="파이썬 '너무 재밌어"
print(result) # 파이썬 '너무 재밌어

# 문자열에 쌍따옴표 포함
result ='"1더하기 1"이 뭐지?'
print(result) # "1더하기 1"이 뭐지?

# 역슬래시 이용
result="python\'s is very easy!"
print(result) # python's is very easy!


"""
TODO: 문자열 연산하기
"""

# 문자열 더하기
head="Python"
tail=" is fun!"
print(head+tail) # Python is fun!


# 문자열 곱하기
a="python"
print(a*2) # pythonpython

print("=" * 10) # ==========


# 문자열 길이 구하기
a="Life is too short"
print(len(a)) # 17


