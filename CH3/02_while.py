"""
TODO: 기본 예제
"""

treeHit=0
while treeHit<5:
    treeHit=treeHit+1
    print("나무를 %d번 찍었습니다." % treeHit)
    
    if treeHit==3:
        print("나무 넘어갑니다.")

'''
출력
나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무 넘어갑니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
'''


"""
TODO: while문 빠져 나가기 - break
"""
# ! 아래 코드 유사한 문제 중간고사에 출제할 거라고 하심
coffee=10
while True:
    money=int(input("돈을 넣어 주세요: "))
    if money==300:
        print("커피를 줍니다.")
        coffee=coffee-1
    elif money>300:
        print("거스름돈 %d를 주고 커피를 줍니다."%(money-300))
        coffee=coffee-1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다."%coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break


"""
TODO: while문 처음으로 돌아가기 - continue
"""
a=0
while a<10:
    a=a+1
    if a%2==0:
        continue
    print(a)


'''
출력
1
3
5
7
9
'''