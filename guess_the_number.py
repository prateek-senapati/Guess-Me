# COURSE: Complete Python Bootcamp: Go from zero to hero in Python 3
# INSTRUCTOR: Jose Portilla
# PLATFORM: Udemy

# Guessing Game Challenge: GUESS ME

import random

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("If your guess is less than 1 or more than 100, the GAME will be OVER")
print("LET'S PLAY!")
number_of_guesses = 0
random_number = random.randint(1, 100)
guessed_correctly = False
while not guessed_correctly:
    current_guess = int(input("Enter your guess: "))
    number_of_guesses += 1
    if current_guess not in range(1, 101):
        print("OUT OF BOUNDS. Game Over!")
        print(f"The randomly generated number is {random_number}")
        break
    elif current_guess == random_number:
        print(f"You have guessed the number correctly in {number_of_guesses} turns")
        guessed_correctly = True
    else:
        if number_of_guesses == 1:
            if abs(random_number - current_guess) <= 10:
                print("WARM")
            else:
                print("COLD")
        else:
            if abs(random_number - current_guess) < abs(random_number - previous_guess):
                print("WARMER")
            else:
                print("COLDER")
        previous_guess = current_guess
