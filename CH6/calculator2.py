result1=0
result2=0

def add(num):
    global result1
    result1 += num
    return result1

def add(num):
    global result2
    result2 += num
    return result2

print(add(3))
print(add(4))
print(add(5))


