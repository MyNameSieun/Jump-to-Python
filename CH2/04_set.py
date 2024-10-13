"""
집합
- 중복 불가. 순서가 없다.(리스트, 튜플은 순서가 있음)
- set은 중복을 허용하지 않는 특징 때문에 데이터의 중복을 제거하기 위한 필터로 종종 사용
- 만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환한 후에 해야 한다.
"""

# TODO: 생성 방법
s1=set([1,2,3])
print(s1) # {1, 2, 3}

s2=set("Hello")
print(s2) # {'l', 'e', 'o', 'H'}


# TODO: 저장된 값을 인덱싱으로 접근(리스트나 튜플로 변환)
s1=set([1,2,3])
t1=list(s1)

print(t1) # [1, 2, 3]
print(t1[0]) # 1

t1=tuple(s1)
print(t1) # (1, 2, 3)
print(t1[0]) # 1


# TODO: 교집합
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

a=s1 & s2
print(a) # {4, 5, 6}

a=s1.intersection(s2)
print(a) # {4, 5, 6}


# TODO: 합집합
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

a=s1 | s2
print(a) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

a=s1.union(s2)
print(a) # {1, 2, 3, 4, 5, 6, 7, 8, 9}


# TODO: 차집합
a=s1-s2
print(a) # {1, 2, 3}

a=s1.difference(s2)
print(a) # {1, 2, 3}

a=s2-s1
print(a) # {8, 9, 7}

a=s2.difference(s1)
print(a) # {8, 9, 7}


# TODO: 집합 자료형 관련 함수
# item 1개 추가 - add
s1=set([1,2,3])
s1.add(4)
print(s1) # {1, 2, 3, 4}


# item 여러 개 추가 - update
s1=set([1,2,3])
s1.update([4,5,6])
print(s1) # {1, 2, 3, 4, 5, 6}


# item 제거 - remove
s1=set([1,2,3])
s1.remove(2)
print(s1) # {1, 3, 4, 5, 6}