"""
TODO: 리스트 사용하는 예제
"""

_list=["one","two","three"]
for i in _list:
    print(i)

"""
출력
one
two
three
"""


a=[(1,2),(3,4),(5,6)]
for(frist,last) in a:
    print(frist+last)

"""
출력
3
7
11
"""


"""
TODO: for문의 응용
문제: 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이면 합격이고 그렇지 않으면 불합격이다. 합격인지, 불합격인지 결과를 보여 주시오.
"""
marks=[90,25,67,45,80]
number=0
for mark in marks: # 90,25,67,45,80을 순서대로 mark에 대입
    number+=1
    if mark>=60:
        print("%d번 학생은 불합격입니다."%number)
    else:
        print("%d번 학생은 불합격입니다."%number)

"""
출력
1번 학생은 불합격입니다.
2번 학생은 불합격입니다.
3번 학생은 불합격입니다.
4번 학생은 불합격입니다.
5번 학생은 불합격입니다.
"""


"""
TODO: for문과 continue 문
문제: 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이면 합격이고 그렇지 않으면 불합격이다. 합격인 사람에게만 축하 메시지를 보내도록 작성 하시오.
! 중요 시험에 나올듯 !
"""
marks=[90,25,67,45,80]
number=0
for mark in marks:
    number+=1
    if mark<60:
        continue
    print("%d번 학생 축하합니다. 합격입니다."%number)

"""
출력
1번 학생 축하합니다. 합격입니다.
3번 학생 축하합니다. 합격입니다.
5번 학생 축하합니다. 합격입니다.
"""

"""
TODO: for문과 range 함수
숫자 리스트를 자동으로 만들어 주는 range 함수와 빈번한 사용
"""
a=range(1,11)
print(a) # range(1, 11)

add=0
for i in range(1,11):
    add+=i
    
    print(add)

"""
출력
1
3
6
10
15
21
28
36
45
55
"""


"""
TODO: for문을 포함하는 list comprehension 사용
[표현식 for 항목 in 반복_가능_객체 if 조건문]

편리하고 직관적인 프로그래밍 가능
"""
# a=[1,2,3,4]
# result=[]
# for num in a:
#     result.append(num*3)

# print(result) # [3, 6, 9, 12]


a=[1,2,3,4]
result=[num * 3 for num in a]
print(result) # [3, 6, 9, 12]
