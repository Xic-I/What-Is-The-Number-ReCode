import random


limit_number = [
                (0,100),
                (0,200),
                (0,400),
                (0,800),
                (0,1000),
            ]

def Level():
    random_number = random.choice(limit_number)
    random_target = random.randint(random_number[0], random_number[4])
    
    while True:
        answer = int(input("What is The Number: "))

        if answer == random_target:
            print('Congratulations filho da putinha\n')
            break

        if answer > random_target:
            print('The number is smaller\n')
        else:
            print('The number is bigger\n')

Level()