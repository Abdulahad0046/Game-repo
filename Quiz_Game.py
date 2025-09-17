print("Hello, Welcome to my quiz game!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Lets play game  :)")
score = 0
try:
    answer = input("what does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Your answer is correct")
        score += 1
    else:
        print("Incorrect answer")

    answer = input("what does GPU stands for? ")
    if answer.lower() == "graphics processing unit":
        print("Your answer is correct")
        score += 1
    else:
        print("Incorrect answer")

    answer = input("what does RAM stand for? ")
    if answer.lower() == "random access memory":
        print("Your answer is correct")
        score += 1
    else:
        print("Incorrect answer")

    answer = input("what does ATM stand for? ")
    if answer.lower() == "automatic teller machine":
        print("Your answer is correct")
        score += 1
    else:
        print("Incorrect answer")

    print(f"You have {score} corrected answers")
    print(f"Your score is {(score / 4) * 100}%")
      
finally:
    print("Thanks for giving your precious time!")