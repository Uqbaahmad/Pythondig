import random

dice = input("Write start to roll dice")
if dice == 'start':
    possible_answer = [1, 2, 3, 4, 5, 6]
    choose = random.choice(possible_answer)
    print(str(choose))