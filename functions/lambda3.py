# map function

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 1]

f = list(map(lambda i,j: i + j , a, b))
print(f)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 1]
c = 100
f = list(map(lambda i,j: i + j+c , a, b))
print(f)