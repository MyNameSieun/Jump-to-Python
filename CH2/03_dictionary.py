"""
딕셔너리
- Key와 Value를 한 쌍으로 가지는 자료형
- 리스트나 튜플처럼 순차적으로 해당 item을 구하지 않고 Key를 통해 Value를 획득
- key가 중복으로 존재할 수 없다.
"""

# TODO: 딕셔너리의 생성
a={"name":"pey","phone":"010-1234-5678","birth":"1118"}
b={1:"hi"}
c={"a":[1,2,3]}

print(a) # {'name': 'pey', 'phone': '010-1234-5678', 'birth': '1118'}
print(b) # {1: 'hi'}
print(c) # {'a': [1, 2, 3]}


# TODO: item(pair) 추가하기
a={1:"a"}
a[2]="b"
print(a) # {1: 'a', 2: 'b'}

a["name"]="pey"
print(a) # {1: 'a', 2: 'b', 'name': 'pey'}

a[3]=[1,2,3]
print(a) # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}


# TODO: item(pair) 삭제하기
a={1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
del a[1]
print(a) # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}


# TODO: key를 이용하여 Value 구하기
# ! key는 immutable 한 것만 가능 -> 따라서, 튜플은 key로 가능하나 리스트는 불가능하다.
# ! 딕셔너리의 key 사용 여부는 key가 immutable 여부에 따라 다르다.
grade={"pey":10,"julliet":99}
a=grade["pey"]
b=grade["julliet"]

print(a) # 10
print(b) # 99


a={1:"a",2:"b"}
print(a[1]) # a
print(a[2]) # b


a={"a":1,"b":2}
print(a["a"]) # 1
print(a["b"]) # 2

# ! 중복되는 key를 사용하면 기존의 것은 무시되고 새로운 key:value로 설정된다.
a={1:"a",1:"b"} 
print(a) # {1: 'b'}



# ! 리스트는 key를 사용할 수 없으므로 아래 코드는 오류 발생
# a={1:"a",a:"b"}
# print(a)

# a={[1,2]:"hi"}
# print(a)


"""
TODO 딕셔너리 관련 함수
"""
# key 리스트 만들기 - keys
a={"name":"pey", "phone":"010-1234-5678", "birth":"1118"}
print(a.keys()) # dict_keys(['name', 'phone', 'birth'])

b=list(a.keys())
print(b) # ['name', 'phone', 'birth']

# * 기억할 사항
for k in a.keys():  
    print(k)                      
# name
# phone
# birth


# value 리스트 만들기 - values
a={"name":"pey", "phone":"010-1234-5678", "birth":"1118"}
print(a.values()) # dict_values(['pey', '010-1234-5678', '1118'])

b=list(a.values())
print(b) # ['pey', '010-1234-5678', '1118']


# item 구하기 - items (Key, Value pair 구하기)
a={"name":"pey", "phone":"010-1234-5678", "birth":"1118"}
print(a.items()) # dict_items([('name', 'pey'), ('phone', '010-1234-5678'), ('birth', '1118')])

b=list(a.items())
print(b) # [('name', 'pey'), ('phone', '010-1234-5678'), ('birth', '1118')]


# item 지우기 - clear (Key, Value pair 지우기)
a={"name":"pey", "phone":"010-1234-5678", "birth":"1118"}
a.clear()
print(a) # {}



# key로 value 구하기 - get
a={"name":"pey", "phone":"010-1234-5678", "birth":"1118"}

b=a.get("name")
print(b) # pey

b=a["name"]
print(b) # pey

b=a.get("nokey")
print(b) # None, 에러는 나지 않음

# ! 딕셔너리 a에 "nokey"라는 키가 존재하지 않기 때문에 오류 발생
# b=a["nokey"]
# print(b)

# ! 따라서 아래와 같이 변경해줘야함.
b=a.get("nokey","foo") # key가 없는 경우, "foo" 반환
print(b) # foo


# key 존재 여부 조사 - in
b="name" in a
print(b) # True

b="email" in a
print(b) # False



