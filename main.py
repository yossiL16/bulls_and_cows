from game.secret import generate_secret
# from game.validate import is_valid_guess
from game.logic import score_guess, init_state, apply_guess
from game.io_1 import prompt_guess, print_feedback, print_status
from game.logic import is_won
from game.io_1 import nprint_result



def play(length: int = 4) -> None:

    secret_number = generate_secret()
    state = init_state(secret_number, length)
    while True:
        numbers_guess = prompt_guess(length)
        score_g = score_guess(secret_number, numbers_guess)
        win = is_won(score_g[0], length)
        if win:
            nprint_result(state,win)
            print("bay")
            break
        apply_guess(state, numbers_guess)
        print_feedback(numbers_guess, score_g[0], score_g[1])
        print("-- - - - - - - ")
        print_status(state)

if __name__ == "__main__":
    play()

