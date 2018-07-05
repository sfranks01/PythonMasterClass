import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
while guess != answer:
    if guess == 0:
        print("Game over")
        break
    if guess < answer:
        print("Try higher")
        guess = int(input())
    if guess > answer:
        print("Try lower")
        guess = int(input())
    continue

else:
    print("Congratulations!")