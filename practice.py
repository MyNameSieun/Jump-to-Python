s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])


#교집합
a=s1&s2
b=s1.intersection(s2)
print(a)
print(b)

# 합집합
a=s1|s2
b=s1.union(s2)
print(a)
print(b)

# 차집합
a=s1-s2
b=s1.difference(s2)
print(a)
print(b)

a=s2-s1
b=s2.difference(s1)
print(a)
print(b)

s1=set([1,2,3])
s1.add(4)
print(s1)


s1=set([1,2,3])
s1.update([4,5,6])
print(s1)


s1=set([1,2,3])
s1.remove(3)
print(s1 )
