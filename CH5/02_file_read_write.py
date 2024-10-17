"""
TODO: 파일 입출력
* 파일 생성 - 내장함수 open 이용하여 파일 생성
* 파일_객체=open(파일이름, 파일열기모드)
* 파일 열기 모드: r(읽기 모드), w(쓰기 모드), a(추가 모드)
"""



"""
# TODO: 파일 생성 및 닫기
파일을 쓰기 모드(w)로 열면 해당 파일이 이미 존재할 경우
원래 있던 내용이 모두 사라지고, 해당 파일이 존재하지 않으면 새로운 파일이 생성된다.
"""

f=open("새파일.txt", "w")
# f=open("C:/tep/새파일.txt", "w") # * 다음과 같이 경로지정 가능
f.close()


# TODO: 파일을 쓰기 모드로 열어 내용 쓰기
# * (1) 먼저 cmd에서 tmp 디렉토리 생성해주기 "mkdir C:\tmp"
# * (2) 그 후, C:\tmp 디렉토리에 아래 코드를 "write_data.py"로 저장

f=open("C:/tmp/새파일.txt","w")
for i in range(1,11):
    data="%d번째 줄입니다.\n" % i
    f.write(data) 
f.close()   


# * (3) 그 후, cmd에서 "cd C:\tmp" 로 이동하여 "python write_data.py" 수행하기
# * (4) 이제 새파일.txt가 생성되는데, 이 파일을 실행 시키면 됨.


# TODO: 파일을 읽는 여러가지 방법
# *(1) readline 함수 이용하기(가장 많이 사용됨)
# ! readline은 내장 함수가 아니다. 파일 객체가 갖는 함수임!
# readline_test.py
f=open("C:/tmp/새파일.txt", "r")
line = f.readline()
print(line) # 1번째 줄입니다.\n
f.close()

# 위 코드에서 모든 줄 출력하기
f=open("C:/tmp/새파일.txt", "r")
while True:
    line=f.readline()
    if not line: break
    print(line) #  1번째 줄입니다.\n\n2번째 줄입니다.\n\n ...10번쨰 줄입니다. 
f.close()


# *(2) readlines 함수 사용하기 - 파일의 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 리턴
# readlines.py
f=open("C:/tmp/새파일.txt", "r")
lines=f.readlines()
for line in lines:
    print(line) # ["1번째 줄입니다.\n", "2번째 줄입니다.\n", ..., "10번째 줄입니다.\n"]ㅣ
f.close()


# 줄바꿈\n 제거하기 with strip()
f=open("C:/tmp/새파일.txt", "r")
lines=f.readlines()
for line in lines:
    line=line.strip()
    print(line)
f.close()
    

# *(3) read 함수 사용하기 - f.read()는 파일의 내용 전체를 문자열로 리턴한다. 따라서 위 예의 data는 파일의 전체 내용이다.
# read.py
f=open("C:/tmp/새파일.txt", "r")
data=f.read()
print(data)
f.close()


# *(4) 파일 객체를 for 문과 함께 사용하기 - 파일 객체(f)는 기본적으로 위와 같이 for 문과 함께 사용하여 파일을 줄 단위로 읽을 수 있다.
# read_for.py
f=open("C:/tmp/새파일.txt", "r")
for line in f:
    print(line)
f.close() 


"""
# TODO: 파일에 새로운 내용 추가하기
쓰기 모드('w')로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다.
하지만 원래 있던 값을 유지하면서 단지 새로운 값만 추가해야 할 경우도 있다. 이런 경우에는 파일을 추가 모드('a')로 열면 된다.
# ! TODO: print가 없으므로 개행문자 \n 넣어주기

* 아래는 새파일.txt 파일을 추가 모드('a')로 열고 write를 사용해서 결괏값을 기존 파일에 추가해 적는 예이다.
* 여기에서 추가 모드로 파일을 열었기 때문에 새파일.txt 파일이 원래 가지고 있던 내용 바로 다음부터 결괏값을 적기 시작한다.
"""
# add_data.py
f=open("C:/tmp/새파일.txt", "a")
for i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()




# TODO: with 문과 함께 사용하기
# ! with를 사용하면 close를 사용하지 않아도 된다. (파일을 열고 닫는 것을 자동으로 처리)
with open("새파일.txt","w") as f:
    f.write("Life is too short, your need python")


# TODO: sys 모듈을 사용하면 사용자 입력 없이 프로그램에 인수를 전달할 수 있다.