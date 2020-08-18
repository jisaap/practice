functions = []

for i in range(10):
    print(i)
    functions.append(lambda : i)

b = 1

for f in functions:
    print(b + 1)
    print(f())
