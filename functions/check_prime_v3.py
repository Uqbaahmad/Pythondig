from sympy import prime


def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return 'Not Prime'
    else:
        return 'Prime'
       
for i in range(2, 100):
    out = check_prime(i)
    print(i, out)