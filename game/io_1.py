


def prompt_guess(length: int) -> str:
    while True:
        guess = "".join(input("please enter 4 numbrs to guess: ").split())
        if len(guess) == length:
            return guess
        else:
            print(f"enter only {length} numbers")

def print_feedback(guess: str, bulls: int, cows: int) -> None:

    print("YOUR STATUS:")
    print("yor guess is:", guess, "bulls = ", bulls, "cows = ", cows)

def print_status(state: dict) -> None:

    print(f"Your guesses so far: {state["seen"]}")


def nprint_result(state: dict, won: bool) -> None:

    if won == True:
        print(f"you winn!!!!")
        print(f"the secret number is: {state["secret"]}. your try is: {state["tries_used"]}")
