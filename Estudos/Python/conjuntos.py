x = {1,1,2,3,3,4,5}
y = set([3,5,6,6,7,8])
print(type(x))

print(x)

print(len(x))

print(y)

print("Interseção: ", x&y)

print(x.isdisjoint(y))

print(x-y)

print(y-x)

print("Diferença Simétrica:", x^y)

print("União: ", x|y)
