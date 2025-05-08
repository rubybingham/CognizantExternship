import random
number_to_guess = random.randint(1, 100)
print("The secret number is between 1 and 100. Can you guess it?")

count = 0
while count < 10:
    user_num = int(input("Enter your guess: "))
    if user_num == number_to_guess:
        print("Congratulations! You guessed it in", count, "attempts!")
        break
    elif user_num < number_to_guess:
        print("Too low! Try again!")
    else:
        print("Too high! Try again!")
    count += 1
if count == 10:
    print("Game over! Better luck next time!")