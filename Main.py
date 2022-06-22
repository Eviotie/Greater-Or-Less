import random

print("Please input give a range of numbers. ")
r1 = input("Number 1 ")
r2 = input("Number 2 ")
x = 0
Thenumber = random.randint(int(r1), int(r2))
while True:
    guess = int(input("Please guess a number. "))
    if guess == Thenumber:
        print("You have won in {x} tries!".format(x = x))
        break
    else:
        if guess > Thenumber:
            print("Less")
        else:
            print("Greater")
    x += 1