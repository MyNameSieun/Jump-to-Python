class Family:
    lastname="최"

a=Family()
b=Family()

print(f"Family.lastname = {Family.lastname}")
print(f"a.lastname = {a.lastname}")
print(f"b.lastname = {b.lastname}")

Family.lastname="박"

print(f"Family.lastname = {Family.lastname}")
print(f"a.lastname = {a.lastname}")
print(f"b.lastname = {b.lastname}")