def check_prime():
    a = 541
    for i in range(2, 541):
        if a % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

check_prime()

var = check_prime()
print(var)