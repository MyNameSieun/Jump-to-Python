# 시은이의 정리 노트

![list, tuple](<src/img/list, tuple.jpg>)![dictionary, set](<src/img/dictionary, set.jpg>)

1. 사칙 연산자의 / 연산자의 몫 연산자 // 차이는?

2. 문자열 슬라이싱에서 `0`은 문자열의 첫 번째 문자, `-1`은 문자열의 맨 마지막 문자를 의미한다.

   ![](./src/img/문자열_슬라이싱.png)

3. 파이썬이 기존 언어와 다른 연산자를 채택하고 있는데, 그걸 아는 것이 중요

   1. c언어에선 //는 주석인데 python에선 연산자로 쓰임!
   2. c언어엔 있는데 python엔 없는 것: 지수 연산자 print(a\*\*b), 몫 연산자: print(a//b)

4. 리스트 안에는 어떠한 자료형도 포함할 수 있다.

5. find와 index는 에러 처리에 차이가 있다.
   1. find는 에러발생 x, index는 에러 발생 o
6. reverse는 정렬과 무관

7. remove는 여러 개 있으면 첫 번째 제거

8. `",".join(abcd)` => `a,b,c,d`

9. 리스트 관련 함수 함수의 인자는 리스트만 가능

10. 튜플은 불변하기 때문에 item을 바꿀 수 없다. 리스트는 item 생성, 삭제, 수정 가능

11. 집합은 순서가 없지만 리스트, 튜플은 순서가 있다.

12. append, insert, extend 차이 제대로 알자

---

<br><br>

# 챕터 별 문제

## CH1

<details>
  <summary>02 number-type</summary>
  
> 문제 1: 기본 숫자형

설명: 다음의 변수에 정수형, 실수형 값을 할당한 후, 해당 값의 타입을 출력하는 프로그램을 작성하세요.

- a에 100을 할당
- b에 3.14를 할당

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 2: 2진수, 8진수, 16진수 변환

설명: 다음의 10진수 숫자를 각각 2진수, 8진수, 16진수로 변환하여 출력하는 프로그램을 작성하세요.

- 10 (10진수)
- 255 (10진수)

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 3: 사칙연산

설명: 두 정수 a = 15, b = 4에 대해 다음의 연산을 수행하고 결과를 출력하는 프로그램을 작성하세요.

- a와 b의 합
- a와 b의 차
- a와 b의 곱
- a를 b로 나눈 결과
- a를 b로 나눈 몫
- a를 b로 나눈 나머지

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 4: 지수 연산

설명: 정수 a = 2, b = 5에 대해 a의 b제곱을 계산하고 결과를 출력하는 프로그램을 작성하세요.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 5: 복합 연산자

설명: 정수 x = 10을 초기값으로 설정하고 다음의 연산을 수행하여 결과를 출력하는 프로그램을 작성하세요.

- x에 5를 더하고 결과 출력
- x에 2를 곱하고 결과 출력
- x를 3으로 나누고 결과 출력
- x의 나머지를 4로 구하고 결과 출력
- x를 2로 나눈 몫을 구하고 결과 출력

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 6: 실수형 연산

설명: 다음의 두 실수형 변수 num1 = 5.5, num2 = 2.0에 대해 사칙연산을 수행하고 결과를 출력하는 프로그램을 작성하세요.

- 덧셈
- 뺄셈
- 곱셈
- 나눗셈

```python
# TODO: 아래에 코드를 작성하세요.
```

</details>

<br>

<details>
  <summary>03 string type</summary>
  
> 문제 1

다음 중 출력 결과가 올바르게 나오는 코드를 고르세요.

```python
# 1.
print("Python is 'fun'")

# 2.
print('Python is "fun"')

# 3.
print("Python's fun")

# 4.
print('Python's fun')
```

> 문제 2

다음 코드를 실행했을 때 출력 결과는 무엇일까요?

```python
a = "Hello"
b = "World"
print(a + " " + b)  # ?
```

> 문제 3

다음 코드에서 print(a \* 3)의 결과를 예측하세요.

```python
a = "python "
print(a * 3)  # ?
```

> 문제 4

문자열 "Life is too short"의 길이를 구하는 코드를 작성하세요.

```python
a = "Life is too short"
# 문자열 길이를 구하는 코드
```

> 문제 5

다음 중 여러 줄 문자열을 올바르게 출력하는 코드를 고르세요.

```python
# 1.
print("""Hello
World""")

# 2.
print("Hello
World")
```

> 문제 6

- 다음 문자열에 포함된 따옴표를 제대로 출력하도록 코드 작성하기.
  - 문자열: "Python's fun!"

```python
# 코드 작성
```

> 문제 7

다음 코드를 실행했을 때 결과가 어떻게 나오는지 예측하세요.

```python
a = "=" * 10
b = "-" * 5
print(a + b)  # ?
```

</details>

<br>

<details>
  <summary>04 string indexing and slicing</summary>
  
> 문제 1

다음 코드를 실행했을 때 출력 값을 예측하시오.

```python
a = "Python programming"
print(a[0])  # ?
print(a[5])   # ?
print(a[-0])   # ?
print(a[-3])  # ?
```

> 문제 2

다음 코드를 실행했을 때 결과를 예측하세요. 또한, 이 코드에서 문자열 슬라이싱의 start와 end가 각각 어떻게 적용되는지 설명해보세요.

```python
a = "Life is too short, You need Python"
print(a[0:4])  # ?
print(a[:3])  # ?
print(a[3:])  # ?
print(a[8:11])  # ?
print(a[:])  # ?
print(a[2:-3])  # ?

```

> 문제 3

문자열에서 끝에서부터 세 번째 문자를 추출하려면 어떻게 해야 할까요? 코드로 작성해보세요.

```python
a = "Hello, Python!"
# 끝에서 세 번째 문자 추출하는 코드

```

> 문제 4

다음 문자열을 슬라이싱을 사용하여 날짜와 날씨 정보를 각각 추출하는 코드를 작성하세요.

```python
a = "20241014Cloudy"
# 날짜와 날씨를 추출하는 코드 작성

```

> 문제 5

다음 코드를 실행했을 때 출력 결과는 무엇일까요?

```python
a = "I love Python"
print(a[:6])  # ?
print(a[7:])  # ?
```

> 문제 6

- 문자열 "2024년 10월 14일"에서 연, 월, 일을 각각 슬라이싱을 사용해 추출하고, 아래와 같이 출력하는 코드를 작성하세요.
  - 연: 2024
  - 월: 10
  - 일: 14

```python
a = "2024년 10월 14일"
# 연, 월, 일을 추출하는 코드 작성
```

> 문제7

아래 코드가 에러가 나는 이유를 설명하세요.

```python
a="Pithon"
a[1]="y"
print(a[1])
```

> 문제 8

문자열 "Python"에서 두 번째 문자를 "y"로 바꾸기 위해 슬라이싱을 사용한 코드를 작성하세요.

```python
a = "Pithon"
# 두 번째 문자를 "y"로 변경하는 코드 작성
```

</details>

<br>

<details>
  <summary>05 string fomatting</summary>
  
> 문제 1

다음 코드를 실행했을 때 출력 결과를 예측하세요.

```python
a = "I eat %d apples." % 5
print(a)
```

> 문제 2

포맷 함수를 사용하여 아래 문자열을 출력해보세요.

```python
number = 10
day = "three"
# 출력: I ate 10 apples. So, I was sick for three days.
```

> 문제 3

다음 코드의 출력 결과를 예측해 보세요.

```python
a="%s" % "apple"
print(a)

a = "%10s" % "apple"
print(a)

a = "%-10s" % "apple"
print(a)
```

> 문제 4

다음 코드에서 number가 3이고 apples가 "five"일 때, f-string 포매팅을 이용해서 아래와 같은 문자열을 출력하는 코드를 완성하세요.

```python
number = 3
apples = "five"
# 출력: I have 3 apples and my brother has five.
```

> 문제 5

포맷 함수와 f-string 포매팅을 사용하여 왼쪽으로 정렬하고, 총 15자리의 공백을 "!"로 채워서 출력하는 코드를 작성하세요.

```python
a = "Python"
```

> 문제 6

포맷 함수와 f-string 포매팅을 사용하여 소수점 둘째 자리까지만 출력하도록 코드를 수정하세요.

```python
number = 3.14159
```

> 문제 7

f-string 포매팅을 이용하여 age가 25일 때 "나의 나이는 25살입니다."라는 문장을 출력하는 코드를 작성하세요.

```python
age = 25
# f-string을 사용해 나이를 포함하는 문장을 출력
```

> 문제 8

포맷 함수와 f-string 포매팅을 사용하여 문자열 "Python"을 가운데 정렬하고, 공백을 \*로 채운 결과를 출력하는 코드를 작성하세요.

```python
a = "Python"
```

</details>

<br>

<details>
  <summary>06 string function</summary>
  
   
> 문제 1

문자열에서 문자 'a'의 개수를 세는 코드를 작성하세요.

> 문제2

문자열 a = "programming"에서 문자 'm'이 처음으로 나타나는 위치를 찾는 코드를 작성하세요.

> 문제3

문자열 "apple"에서 find()와 index()의 차이를 확인해보세요. 문자 'p'와 'z'를 찾는 코드를 작성하세요.

> 문제4

문자열 "abcd"를 콤마(,)로 구분하여 연결된 문자열로 변환하는 코드를 작성하세요.

> 문제5

문자열 "HELLO world"를 모두 소문자로 변환한 결과를 출력하는 코드를 작성하세요.

> 문제6

문자열 "hello world"를 모두 대문자로 변환한 결과를 출력하는 코드를 작성하세요.

> 문제7

다음 문자열에서 왼쪽과 오른쪽의 공백을 제거한 후 결과를 출력하세요.

```python
a= "  hi  "
```

> 문제8

다음 문자열에서 오른쪽의 공백을 제거한 후 결과를 출력하세요.

```python
a= "  hi  "
```

> 문제9

문자열 "I love apples"에서 "apples"를 "bananas"로 변경하는 코드를 작성하세요.

> 문제10

문자열 "one:two:three:four"를 콜론(:)을 기준으로 분리한 후, 결과를 출력하세요.

</details>

<br>

<details>
  <summary>07 bool</summary>

> 문제1

다음 코드의 출력 결과를 예측해보세요.

```python
a = bool("Hello World")
b = bool("")
c = bool([0, 1, 2])
d = bool([])

print(a)
print(b)
print(c)
print(d)
```

> 문제2

다음 코드에서 참(True) 또는 거짓(False)으로 평가되는 값을 확인하고, 올바른 결과를 예측하세요.

```python
a = bool(0)
b = bool(-1)
c = bool(3.14)
d = bool(None)

print(a)
print(b)
print(c)
print(d)
```

> 문제3

다음 리스트에서 참(True)로 평가되는 값만 출력하도록 코드를 작성하세요.

```python
items = [0, 1, "", "Python", [], [1, 2], {}, {"key": "value"}, None]

# 힌트: for 문과 if 문을 활용하세요.
```

> 문제4

사용자로부터 입력받은 값이 비어있지 않으면 "입력되었습니다"를 출력하고, 비어 있으면 "입력되지 않았습니다"를 출력하는 프로그램을 작성하세요.

```python
# 예시
user_input = input("값을 입력하세요: ")

# 여기서 작성
```

> 문제5

다음 값들이 참(True)인지 거짓(False)인지 확인하는 코드를 작성하세요.

```python
bool("False")
bool([])
bool([None])
bool({})
bool(100)
bool(())
bool((""))
```

</details>

<br>

<details>
  <summary>08 variable</summary>

> 문제1

다음 코드의 출력 결과를 예측해보세요.

```python
a = [1, 2, 3]
b = a

a[0] = 100
print(a)  # ?
print(b)  # ?
```

> 문제2

다음 코드에서 a와 b가 같은 객체를 가리키는지 확인하는 코드를 작성하세요.

```python
a = [1, 2, 3]
b = a[:]

# a와 b가 같은 객체인지 확인하는 코드
```

> 문제3

copy 모듈을 사용하지 않고 리스트 a를 복사하여 b에 저장한 후, a의 값을 수정했을 때 b의 값이 영향을 받지 않도록 하세요.

```python
a=[1,2,3]

# 여기서 작성
```

> 문제4

copy 모듈을 사용하여 리스트 a를 복사하여 b에 저장한 후, a의 값을 수정했을 때 b의 값이 영향을 받지 않도록 하세요.

```python
a=[1,2,3]

# 여기서 작성
```

> 문제5

다음 코드를 실행했을 때 출력 결과가 무엇일지 예측하세요.

```python
a, b = ("apple", "banana")
print(a)  # ?
print(b)  # ?
```

> 문제6

다음 코드에서 여러 변수에 같은 값을 할당하고, 그 값을 출력하는 코드를 작성하세요.

```python
a = b = c = "hello"

print(a)  # ?
print(b)  # ?
print(c)  # ?
```

> 문제7

두 변수 a와 b의 값을 서로 바꾸는 코드를 작성하세요.

```python
a = 10
b = 20

# a와 b의 값을 바꾸는 코드
print(a)  # 20
print(b)  # 10
```

> 문제8

리스트 [10, 20, 30]을 변수 a, b, c에 각각 할당하는 코드를 작성하세요. 한 줄로 해결해 보세요.

```python
# 예시: a = 10, b = 20, c = 30
```

</details>

<br>

<details>
  <summary>07 bool</summary>

> 문제1

다음 코드의 출력 결과를 예측해보세요.

```python
a = bool("Hello World")
b = bool("")
c = bool([0, 1, 2])
d = bool([])

print(a)
print(b)
print(c)
print(d)
```

> 문제2

다음 코드에서 참(True) 또는 거짓(False)으로 평가되는 값을 확인하고, 올바른 결과를 예측하세요.

```python
a = bool(0)
b = bool(-1)
c = bool(3.14)
d = bool(None)

print(a)
print(b)
print(c)
print(d)
```

> 문제3

다음 리스트에서 참(True)로 평가되는 값만 출력하도록 코드를 작성하세요.

```python
items = [0, 1, "", "Python", [], [1, 2], {}, {"key": "value"}, None]

# 힌트: for 문과 if 문을 활용하세요.
```

> 문제4

사용자로부터 입력받은 값이 비어있지 않으면 "입력되었습니다"를 출력하고, 비어 있으면 "입력되지 않았습니다"를 출력하는 프로그램을 작성하세요.

```python
# 예시
user_input = input("값을 입력하세요: ")

# 여기서 작성
```

> 문제5

다음 값들이 참(True)인지 거짓(False)인지 확인하는 코드를 작성하세요.

```python
bool("False")
bool([])
bool([None])
bool({})
bool(100)
```

</details>

<br><br>

## CH2

<details>
  <summary>01 list</summary>

> 문제1

다음 리스트에서 ['a', 'b', 'c']를 인덱싱으로 출력하는 코드를 작성하세요.

```python
a = [1, 2, 3, ['a', 'b', 'c']]
```

> 문제2

다음 코드의 출력 값은 무엇일까용?

```python
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3]) #
print(a[-1]) #

print(a[-1][0]) #
print(a[-1][1]) #
```

> 문제3

다음 리스트에서 ['Life', 'is']를 슬라이싱으로 출력하는 코드를 작성하세요.

```python
a = [1, 2, ['Life', 'is', 'too', 'short']]
```

> 문제4

다음 리스트의 출력 결과는 무엇일까요?

```python
a=[1,2,3,["a","b","c"],4,5]
print(a[0:2]) #
print(a[:2]) #
print(a[2:]) #


a=[1,2,3,["a","b","c"],4,5]
print(a[2:5]) #
print(a[3][:2]) #
```

> 문제3

다음 리스트 a와 b를 더한 결과는 무엇인가요?

```python
a = [1, 2, 3]
b = [4, 5, 6]
```

> 문제4

다음 코드에서 리스트 a의 값을 [1, 4, 3]으로 수정하세요.

```python
a = [1, 2, 3]
```

> 문제5

2가지 방식을 사용하여 리스트에서 마지막 요소를 삭제하는 코드를 작성하세요.

```python
a = [1, 2, 3, 4]
```

> 문제6

슬라이스를 사용하여 리스트 0,1번째 item을 삭제하는 코드를 작성하세요.

```python
a = [1, 2, 3, 4]
```

> 문제7

다음 리스트를 오름차순으로 정렬하고, 그 결과를 출력하는 코드를 작성하세요.

```python
a = [3, 1, 4, 5, 2]
```

> 문제8

리스트에 새로운 요소 [7, 8]을 추가하는 코드를 두 가지 방식으로 작성하세요.

```python
a = [1, 2, 3, 4, 5, 6]
```

> 문제9

리스트에서 숫자 3이 몇 번 등장하는지 출력하는 코드를 작성하세요.

```python
a = [3, 1, 2, 3, 4, 3, 5]
```

> 문제10

다음 리스트의 순서를 뒤집는 코드를 작성하세요.

```python
a=["a","c","b"]
```

> 문제 11

리스트의 0번째 위치에 4를 삽입하는 코드를 작성하세요

```python
a=[1,2,3]
```

> 문제 12

리스트의 3번째 위치에 5를 삽입하는 코드를 작성하세요

```python
a=[4, 1, 2, 3]
```

> 문제13

다음 코드의 출력 값을 예측해보세요.

```python
a=[1,2,3,1,2,3]
a.remove(3)
```

</details>

<br>

<details>
  <summary>02 tuple</summary>

> 문제1

다음 튜플에서 "b"를 인덱싱으로 출력하는 코드를 작성하세요.

```python
t1 = (1, 2, "a", "b")
```

> 문제2

다음 튜플에서 ("a", "b")를 슬라이싱으로 출력하는 코드를 작성하세요.

```python
t2 = (1, 2, 3, "a", "b")
```

> 문제3

다음 두 튜플 t1과 t2를 더한 결과는 무엇인가요?

```python
t1=(1,2,"a","b")
t2 = (3, 4)
```

> 문제4

다음 두 튜플 t2과 t3를 곱한 결과는 무엇인가요?

```python
t2=(3,4)
t3=t2*3
```

> 문제5

다음 튜플의 길이를 구하는 코드를 작성하세요.

```python
t3 = (1, 2, 3, "a", "b", "c")
```

> 문제6

다음 튜플을 두 배로 곱한 결과를 출력하는 코드를 작성하세요.

```python
t4 = (1, "a", 3)
```

> 문제7

아래 코드가 오류가 나는 이유를 리스트와 튜플의 차이점에 빗대어 설명해주세요.

```python
del t1[0]
t1[0]="c"
```

</details>

<br>

<details>
  <summary>03 dictionary</summary>

> 문제1

다음 딕셔너리에서 "name" 키에 해당하는 값을 출력하는 코드를 작성하세요.

```python
a = {"name": "pey", "age": 30, "city": "Seoul"}
```

> 문제2

다음 딕셔너리에 "email" 키와 "email@example.com" 값을 추가하는 코드를 작성하세요.

```python
b = {"name": "pey", "age": 30, "city": "Seoul"}
```

> 문제3

다음 딕셔너리에서 "age" 키에 해당하는 값을 "31"로 수정하는 코드를 작성하세요.

```python
c = {"name": "pey", "age": 30, "city": "Seoul"}
```

> 문제4

다음 딕셔너리에서 "city" 키를 삭제하는 코드를 작성하세요.

```python
d = {"name": "pey", "age": 30, "city": "Seoul"}
```

> 문제5

다음 딕셔너리에 존재하지 않는 "phone" 키를 찾을 때, 값이 없으면 "No phone number"를 반환하는 코드를 작성하세요.

```python
e = {"name": "pey", "age": 30}
```

> 문제6

다음 딕셔너리의 출력 값을 예상해보세요.

```python
a={1:"a",1:"b"}
```

> 문제7

다음 딕셔너리가 오류가 나는 이유를 설명해보세요.

```python
# a={[1,2]:"hi"}
# print(a)
```

> 문제8

다음 딕셔너리의 key 리스트를 만들고 list로 반환하세요.

```python
a={"name":"pey", "phone":"010-1234-5678", "birth":"1118"}
```

> 문제9

for in 함수를사용하여 아래와 같이 key를 반환하세요

```python
# name
# phone
# birth
```

> 문제10

다음 딕셔너리의 value 리스트를 만들고 list로 반환하세요.

```python
a={"name":"pey", "phone":"010-1234-5678", "birth":"1118"}
```

> 문제 11

다음 딕셔너리의 item을 구하고 list로 반환하세요

```python
a={"name":"pey", "phone":"010-1234-5678", "birth":"1118"}
```

> 문제12

다음 딕셔너리의 item을 삭제하세요.

```python
a={"name":"pey", "phone":"010-1234-5678", "birth":"1118"}
```

> 문제13

함수를 사용하여 key로 value값을 구하세요.

```python
a={"name":"pey", "phone":"010-1234-5678", "birth":"1118"}
```

> 문제14

아래 코드가 오류가 나는 이유와 오류가 나지 않도록 변경한 코드를 작성하세요.

```python
# b=a["nokey"]
# print(b)
```

> 문제15

딕셔너리에 "name"이라는 키가 존재하는지 확인하는 코드를 작성하세요.

</details>

<br>

<details>
  <summary>04 set</summary>

> 문제1

다음 리스트에서 중복을 제거하여 집합으로 변환한 후 출력하는 코드를 작성하세요.

```python
my_list = [1, 2, 2, 3, 4, 4, 5]
```

> 문제2

다음 두 집합의 교집합을 두 가지 방식으로 구하세요.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
```

> 문제3

다음 두 집합의 합집합을 두 가지 방식으로 구하세요.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
```

> 문제4

다음 두 집합의 차집합을 두 가지 방식으로 구하세요.

```python
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5}
```

> 문제5

다음 집합에 숫자 7을 추가한 후, 숫자 1을 제거하는 코드를 작성하세요.

```python
set1 = {1, 2, 3, 4, 5}
```

> 문제6

다음 집합에 숫자 6,7을 추가하는 코드를 작성하세요.

```python
set1 = {1, 2, 3, 4, 5}
```

> 문제7

다음 집합을 리스트와 튜플로 변환하세요.

```python
s1=set([1,2,3])
```

</details>

<br><br>

## CH3

<details>
  <summary>01 if</summary>

> 문제 1: 돈이 있으면 택시 타기

설명: 아래 코드를 참고하여 주어진 조건에 따라 다른 메시지를 출력하는 코드를 작성하세요.

- money 변수를 True 또는 False로 설정합니다.
- money가 True일 경우 "택시를 타고 가라"라는 메시지를 출력하고, False일 경우 "걸어가라"라는 메시지를 출력하도록 하세요.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 2: 논리 연산자 사용하기

설명: 아래 코드를 참고하여 금액과 카드를 활용해 택시를 탈 수 있는지를 판단하세요.

money 변수를 2000으로 설정하고 card 변수를 True로 설정합니다.

- money가 3000 이상이거나 card가 True인 경우 "택시를 타고 가라"라는 메시지를 출력하고, 그렇지 않을 경우 "걸어가라"라는 메시지를 출력하도록 코드를 작성하세요.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 3: 리스트에서 값 확인하기

설명: 주어진 리스트에서 특정 값이 포함되어 있는지 확인하는 코드를 작성하세요.

- pocket 리스트를 ["paper", "cellphone", "money"]로 설정합니다.
- 만약 "money"가 pocket 리스트에 포함되어 있으면 "택시를 타고 가라"라는 메시지를 출력하고, 그렇지 않으면 "걸어가라"라는 메시지를 출력하도록 하세요.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 4: 카드 여부에 따른 판단

설명: 다음 조건에 따라 메시지를 출력하는 코드를 작성하세요.

- pocket 리스트를 ["paper", "cellphone"]로 설정하고 card 변수를 True로 설정합니다.
- 만약 "money"가 pocket 리스트에 포함되어 있으면 "택시를 타고 가라"라는 메시지를 출력하고,
- 그렇지 않으면 카드 여부에 따라 "택시를 타고 가라" 또는 "걸어가라"라는 메시지를 출력하도록 하세요.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 5: 조건부 표현식 활용하기

설명: 점수를 바탕으로 메시지를 출력하는 코드를 작성하세요.

- score 변수를 40으로 설정합니다.
- score가 60 이상이면 "success", 그렇지 않으면 "failure"라는 메시지를 출력하는 코드를 조건부 표현식을 사용하여 작성하세요.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 6: pass 문 활용하기

설명: pass 문을 활용하여 특정 조건을 건너뛰는 코드를 작성하세요.

- pocket 리스트를 ["paper", "cellphone", "money"]로 설정합니다.
- 만약 "money"가 포함되어 있으면 pass를 사용하여 아무 작업도 하지 않고, 그렇지 않으면 "카드를 꺼내라"라는 메시지를 출력하는 코드를 작성하세요.

```python
# TODO: 아래에 코드를 작성하세요.
```

</details>

<br>

<details>
  <summary>02 while</summary>

> 문제 1: 나무 찍기 게임
> 설명: 나무를 5번 찍는 게임을 만듭니다. 사용자가 나무를 몇 번 찍었는지 출력하고, 3번 찍었을 때 "나무 넘어갑니다."라고 출력합니다. 사용자가 5번 찍으면 게임이 종료됩니다.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 2: 커피 자판기

설명: 커피 자판기 프로그램을 작성하세요. 사용자가 돈을 입력하면, 300원이면 커피를 주고, 300원 초과일 경우 거스름돈을 주며 커피를 제공합니다. 300원 미만일 경우 "돈을 다시 돌려주고 커피를 주지 않습니다."라는 메시지를 출력합니다. 만약 커피가 다 떨어지면 "커피가 다 떨어졌습니다. 판매를 중지 합니다."라는 메시지를 출력하고 프로그램을 종료합니다.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 3: 홀수 출력하기

설명: 1부터 10까지의 숫자를 순회하면서 짝수는 continue를 사용하여 건너뛰고 홀수만 출력하는 프로그램을 작성하세요.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 4: 1부터 100까지의 합계 구하기 (10의 배수 제외)

설명: 1부터 100까지의 숫자 중 10의 배수를 제외한 나머지 숫자의 합계를 구하는 프로그램을 작성하세요. 이때 continue를 사용하여 10의 배수를 건너뛰도록 합니다.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 5: 사용자가 입력한 숫자 합계 구하기

설명: 사용자가 입력한 숫자의 합계를 구하는 프로그램을 작성하세요. 사용자가 0을 입력하면 종료됩니다. 이때, 사용자가 음수를 입력하면 "음수를 입력하셨습니다."라는 메시지를 출력하고, 다음 숫자를 입력받습니다.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 6: 특정 숫자까지의 짝수 출력하기

설명: 사용자가 특정 숫자를 입력하면, 1부터 해당 숫자까지의 짝수만 출력하는 프로그램을 작성하세요. continue를 사용하여 홀수는 건너뛰도록 합니다.

```python
# TODO: 아래에 코드를 작성하세요.
```

</details>

<br>

<details>
  <summary>03 for</summary>

> 문제 1: 학생 점수 합격 여부 출력하기
>
> 설명: 아래와 같이 5명의 학생 점수가 주어졌을 때, 합격인지 불합격인지 결과를 출력하는 프로그램을 작성하세요.

- 점수 리스트 marks를 [85, 55, 75, 45, 90]으로 설정합니다.
- 각 학생의 점수가 60점 이상이면 "n번 학생은 합격입니다."라고 출력하고, 그렇지 않으면 "n번 학생은 불합격입니다."라고 출력하세요.

```python
marks = [85, 55, 75, 45, 90]
# TODO: 아래에 코드를 작성하세요.
```

> 문제 2: 합격자에게만 축하 메시지 보내기

설명: 문제 1에서 작성한 프로그램을 바탕으로, 합격한 학생에게만 축하 메시지를 출력하는 코드를 작성하세요.

- 점수 리스트는 동일하게 사용합니다.
- 합격한 학생에게만 "n번 학생 축하합니다. 합격입니다."라고 출력하도록 하세요.

```python
marks = [85, 55, 75, 45, 90]
# TODO: 아래에 코드를 작성하세요.
```

> 문제 3: 1부터 20까지의 합계 구하기

설명: range 함수를 사용하여 1부터 20까지의 합계를 계산하고 출력하는 프로그램을 작성하세요.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 4: 리스트 내포 사용하여 제곱 리스트 만들기

설명: 1부터 10까지의 숫자를 제곱한 값을 가진 리스트를 리스트 내포를 사용하여 만들고 출력하세요.

- 결과 리스트는 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]이 되어야 합니다.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 5: 홀수 리스트 만들기

설명: 1부터 30까지의 숫자 중 홀수만 포함된 리스트를 만들고 출력하세요. 리스트 내포를 사용하여 구현합니다.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 6: 리스트에서 특정 조건을 만족하는 값 필터링하기

설명: 주어진 리스트에서 10보다 큰 값만을 포함하는 새로운 리스트를 만들어 출력하세요.

- 원본 리스트는 [5, 12, 3, 18, 7, 30, 9]입니다.

```python
original_list = [5, 12, 3, 18, 7, 30, 9]
# TODO: 아래에 코드를 작성하세요.
```

</details>

<br>

<details>
  <summary>04 continue and break</summary>

> 문제 1: 홀수 출력하기 (continue 사용)

설명: 1부터 20까지의 숫자 중 홀수만 출력하는 프로그램을 작성하세요. 이때 짝수는 continue를 사용하여 출력하지 않도록 합니다.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 2: 첫 짝수 출력 후 종료하기 (break 사용)

설명: 1부터 10까지의 숫자를 순회하면서 첫 번째 짝수를 출력하고, 그 후에는 더 이상 숫자를 출력하지 않는 프로그램을 작성하세요. 이때 break를 사용하여 반복문을 종료합니다.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 3: 1부터 10까지의 숫자 중 짝수는 패스하고 출력하기 (pass 사용)

설명: 1부터 10까지의 숫자를 순회하면서 짝수는 pass를 사용하고 홀수만 출력하는 프로그램을 작성하세요.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 4: 1부터 100까지의 합계 구하기 (continue 사용)

설명: 1부터 100까지의 숫자 중 10의 배수는 건너뛰고 나머지 숫자의 합계를 구하는 프로그램을 작성하세요. 이때 continue를 사용하여 10의 배수를 건너뛰도록 합니다.

```python
# TODO: 아래에 코드를 작성하세요.
```

> 문제 5: "a"가 포함된 문자열 필터링하기 (break 사용)

설명: 주어진 문자열 리스트에서 "a"가 포함된 문자열을 만나면 출력하고, 그 후 더 이상 문자열을 출력하지 않는 프로그램을 작성하세요. 이때 break를 사용합니다.

```python
strings = ["apple", "banana", "cherry", "date", "fig", "grape"]
# TODO: 아래에 코드를 작성하세요.
```

> 문제 6: 1부터 50까지의 숫자 중 7의 배수는 건너뛰고 출력하기 (pass 사용)

설명: 1부터 50까지의 숫자를 순회하면서 7의 배수는 pass하고 나머지 숫자를 출력하는 프로그램을 작성하세요.

```python
# TODO: 아래에 코드를 작성하세요.
```

</details>

<br><br>

## CH4

<details>
  <summary></summary>

> 문제1

```python

```

> 문제2

```python

```

> 문제3

```python

```

> 문제4

```python

```

> 문제5

```python

```

> 문제6

```python

```

> 문제7

```python

```

</details>

<br>

<details>
  <summary></summary>

> 문제1

```python

```

> 문제2

```python

```

> 문제3

```python

```

> 문제4

```python

```

> 문제5

```python

```

> 문제6

```python

```

> 문제7

```python

```

</details>

<br>

<details>
  <summary></summary>

> 문제1

```python

```

> 문제2

```python

```

> 문제3

```python

```

> 문제4

```python

```

> 문제5

```python

```

> 문제6

```python

```

> 문제7

```python

```

</details>

<br>
