"""
TODO: 리스트

- 변경 가능한 자료형으로, 다양한 데이터 타입의 항목 포함 가능
- 다양한 자료형을 갖는 item 을 보관하는 자료구조
- 리스트를 만들 때는 대괄호[]로 감싸주고 각 item은 쉼표로 구분

! 리스트 안에는 어떠한 자료형도 포함할 수 있다.
"""


# TODO: 리스트 생성
a=[] 
print(a) # []

b=[1,2,3]
print(b) # [1, 2, 3]

c=["Life","is","too","short"]
print(c) # ['Life', 'is', 'too', 'short']

d=[1,2,"Life","is"]
print(d) # [1, 2, 'Life', 'is']

e=[1,2,["Life","is"]]
print(e) # [1, 2, ['Life', 'is']]


# TODO: 리스트의 인덱싱(문자열 사용법과 동일)
a=[1,2,3]

print(a[0]) # 1
print(a[-1]) # 3

b= a[0]+a[2]
print(b) # 4


a=[1,2,3,["a","b","c"]]

b=a[3]
print(b) # ['a', 'b', 'c']

b=a[-1]
print(b) # ['a', 'b', 'c']

b=a[-1][0]
print(b) # a

b=a[-1][1]
print(b) # b

b=a[-1][2]
print(b) # c


# TODO: 리스트의 슬라이싱(문자열 사용법과 동일)
a=[1,2,3,4,5]

print(a[0:2]) # [1, 2]
print(a[:2]) # [1, 2]
print(a[2:]) # [3, 4, 5]


a=[1,2,3,["a","b","c"],4,5]
print(a[2:5]) # [3, ['a', 'b', 'c'], 4]
print(a[3][:2]) # ['a', 'b']


# TODO: 리스트 연산하기
a=[1,2,3]
b=[4,5,6]

# 더하기
print(a+b) # [1, 2, 3, 4, 5, 6]

# 곱하기
print(a*3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
 
# 길이 구하기
print(len(a)) # 3


# TODO 리스트의 수정과 삭제
# item 수정하기
a=[1,2,3]
a[2]=4
print(a) # [1, 2, 4]

# item 삭제하기(del 함수 이용)
a=[1,2,3]
del a[1]
print(a) # [1, 3]

a=[1,2,3,4,5]
del a[2:]
print(a) # [1,2]


# TODO 리스트 관련 함수
# item 추가하기 - append
a=[1,2,3]
a.append(4)
print(a) # [1, 2, 3, 4]

a.append([5,6])
print(a) # [1, 2, 3, 4, [5, 6]]


# 정렬 - sort
# * 유니코드 기반 정렬
a=["a","c","b"]
a.sort()
print(a) # ['a', 'b', 'c']

a=[1,4,3,2]
a.sort()
print(a) # [1, 2, 3, 4]


# 순서 뒤집기 - reverse
# ! reverse은 정렬과 무관하다.
a=["a","c","b"]
a.reverse()
print(a) # ['b', 'c', 'a']


# 인덱스 반환 - index
a=[1,2,3]
print(a.index(3)) # 2
print(a.index(1)) # 0
# print(a.index(6)) # ! index에 값이 존재하지 않으면 error


# 특정 위치에 item 삽입 - insert
a=[1,2,3]
a.insert(0,4) # 리스트의 0번째 위치에 4를 삽입
print(a) # [4, 1, 2, 3]

a=[4, 1, 2, 3]
a.insert(3,5)
print(a) # [4, 1, 2, 5, 3] 


# item 제거 - remove
# ! 여러 개 있으면, 첫 번째 item만 제거
# * 인덱스 값이 아닌 요소 값으로 판단
a=[1,2,3,1,2,3]
a.remove(3)
print(a) # [1, 2, 1, 2, 3]


# 특정 위치의 item 빼내기 - pop
a=[1,2,3]
a.pop() # 마지막 요소를 삭제
print(a) # [1, 2]

a=[1,2,3]
a.pop(1)
print(a) # [1, 3]

a=[1,2,3]
a.pop(0) # 첫 번째 요소를 삭제
print(a) # [2, 3]


# 특정한 item 개수 세기 - count
a=[1,2,3,1]
print(a.count(1)) # 2
print(a.count(2)) # 1


# 확장 - extend
# ! 함수의 인자는 리스트만 가능  --> 교재가 틀림 tuple, dict도 들어가긴 함
a=[1,2,3]   
a.extend((4,5))
print(a) # [1, 2, 3, 4, 5]

b=[6,7]
a.extend(b) 
print(a) # [1, 2, 3, 4, 5, 6, 7]