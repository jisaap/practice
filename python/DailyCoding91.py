functions = []

for i in range(10):
    a = i
    functions.append(lambda : a)
    print(a)


for f in functions:
    print(f)
    print(f())

