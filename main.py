import random

range_top = input("Enter the extent for the selection of the number: ")

if range_top.isdigit():
    range_top = int(range_top)
    if range_top <= 0:
        print("Please enter a number greater than 0, nest time.")
        quit()
else:
    print("Please enter a valid number, next time.")
    quit()

random_num = random.randint(0, range_top)
print(f"A random number is selected between 0 to {range_top}")
guess_count = 0;

while True:
    user_guess = input("Enter your guess: ")
    user_guess = int(user_guess)
    if user_guess > random_num:
        print("Lower!")
        guess_count += 1
    elif user_guess < random_num:
        print("Higher!")
        guess_count += 1
    else:
        print("You guessed it right!")
        guess_count += 1
        break

print(f"You took {guess_count} guesses.")
