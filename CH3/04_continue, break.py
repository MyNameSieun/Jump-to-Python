"""
TODO: continue - 하위 부분 수행하지 않고 다음 loop로 이동
"""

# i=0
# while i<10:
#     i+=1
#     if i%2==0:
#         continue
#     print(i)

"""
출력
1
3
5
7
9
"""


"""
TODO: break - 반복문 내부에서 loop 밖으로 이동
"""
i=0
while i<10:
    i+=1
    if i%2 ==0:
        break
    print(i) 

"""
출력
1
"""


"""
TODO: pass - 실행할 부분이 없는 경우 다음으로 이동
"""
i=0
while i<10:
    i+=1
    if i%2==0:
        pass
    print(i)