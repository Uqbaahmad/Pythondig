def check_prime():
    a = 13
    for i in range(2, a):
        if a % i == 0:
            return "Not Prime"
            
    else:
        return "Prime"

check_prime()

out = check_prime()
print(out)