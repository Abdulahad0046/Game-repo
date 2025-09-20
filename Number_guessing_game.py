import random
print("Welcome,\nTo my number guessing game... ")
top_of_range = input("enter a number ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range == 0:
        print("Please enter a number larger than 0 next time")
        quit()
else:
    print("Tyoe a number next time")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guesses = input("make a guesses: ")
    if user_guesses.isdigit():
        user_guesses = int(user_guesses)
    else:
        print("please type a numbr next time")
        continue

    if user_guesses == random_number:
        print("You got it!")
        break
    elif user_guesses > random_number:
        print("You are above the number")
    else:
        print("you are below the number")

print(f"You have got number in {guesses} guesses")