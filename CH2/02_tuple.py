"""
튜플
- 리스트와 유사하지만, 튜플은 (), 리스트는 []
- 리스트와 달리 t2=(1,) 처럼 단지 1개의 요소만을 가질 떄는 요소 뒤에 쉼표(,)를 #! 반드시 붙여야 한다.
- t4=1,2,3 처럼 소괄호(())를 생략해도 된다.
! ⭐ 리스트는 item의 생성, 삭제, 수정이 가능하지만, 튜플은 item을 변경할 수 없다-> 불변성(immutable)
"""

# TODO: 튜플의 생성
t1=()
t2=(1,)
t3=(1,2,3)
t4 =1,2,3 # 소괄호 생략 가능
t5=t1=(1,2,"a","b")
t6=("a","b",("ab","cd"))

print(t1) # ()
print(t2) # (1,)
print(t3) # (1, 2, 3)
print(t4) # (1, 2, 3)
print(t5) # (1, 2, 'a', 'b')
print(t6) # ('a', 'b', ('ab', 'cd'))

# ! 튜플은 불변하기 때문에 아래 코드는 오류 발생
# del t1[0]
# t1[0]="c"


# TODO: 튜플 인덱싱
t1=(1,2,"a","b")
print(t1[0]) # 1
print(t1[3]) # b


# TODO: 튜플 슬라이싱
t1=(1,2,"a","b")
print(t1[1:]) # (2, 'a', 'b')


# TODO: 튜플 더하기
t1=(1,2,"a","b")
t2=(3,4)
t3=t1+t2
print(t3) # (1, 2, 'a', 'b', 3, 4)


# TODO: 튜플 곱하기
t2=(3,4)
t3=t2*3
print(t3) # (3, 4, 3, 4, 3, 4)

# TODO: 튜플 길이 구하기
print(len(t1)) # 4