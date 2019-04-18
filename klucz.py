slownik = {"a":11, "v":22, "r":[33, 200, [100, 999]]}
print(slownik["r"][2][1])
print(type(slownik))

slownik["k"] = 88
print(slownik)
del(slownik["r"][2][0])
print(slownik)

print(slownik.keys())
print(slownik.values())

print("k" in slownik.keys())