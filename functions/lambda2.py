a = [2, 3, 2, 1, 4, 5, 2, 4, 3, 1, 3, 4]
num = 10
# a = map(lambda i : i + num, a)

a = list(map(lambda i : i + num, a))
print(a)