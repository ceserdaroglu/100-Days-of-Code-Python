import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer,turns):
    if guess > answer:
        print("To high.")
        return turns -1
    elif guess < answer:
        print("To low.")
        return turns -1
    else:
        print(f"You got it! 🏆 The answer was {answer}.")
        
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
answer = random.randrange(1,100)
def game():
    print("Welcome to the Number Guessing Game!")
    print("🤖:I'm thinking of a number between 1 and 100.")
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        print("--------------------------------------------------------------")  
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.😭")
            return  
        elif guess != answer:
            print("Guess again.🤔")
                    
game()