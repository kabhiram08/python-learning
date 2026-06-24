secret_word = "apple"
ask_for_guess = input("Enter your guess: ")

while ask_for_guess != secret_word:
    print("You are wrong, try again!")
    ask_for_guess = input("Enter your guess: ")

if ask_for_guess == secret_word:
    print("You are right!")