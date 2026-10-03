import random
number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number(1-100):"))

    if guess < number:
        print("low")
    elif guess > number:
        print("high")
    else:
        print("correct")
        break