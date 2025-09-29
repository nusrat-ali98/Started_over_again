import random
rand_number = random.randint(1,20)

for i in range(7):
    guessed_num = int(input("enter your guess: "))
    if guessed_num < rand_number:
        print("your guess is too low")
    elif guessed_num > rand_number:
        print("your guess is too high")
    else:
        break
if guessed_num == rand_number:
    print("You guessed right! in " + str(i) + " attempts ")
else:
    print("sorry, you won't be able to make it. The correct answer was " + str(rand_number))



