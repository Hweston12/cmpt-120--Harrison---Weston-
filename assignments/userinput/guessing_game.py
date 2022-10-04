def start():
    '''
    This function starts the guessing game loop logic. The function will poll and wait
    until the user inputs their guess and will exit once some conditions are met.
    '''
    print("Guessing Game: Input different animals untill the correct one is entered to win the game")
    # Create a string variable that contains the answer.
    answer = "dog"
    guesses = 0 
    
    while guesses < 3: 
        guess = input("Enter your animal guess: ").lower()
        if guess == 'quit':
            print("Game has been terminated, thank you for playing!")
            break
        if guess != answer:
            guesses = guesses + 1 
            print("Answer is incorrect, Keep Guessing!")
            True
        else:
            print("Good Job! You win!")
            False
            break
start()