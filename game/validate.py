

# def is_valid_guess(guess: str) -> tuple[bool, str]:
#
#     if len(guess) != 4:
#         return (False, "enter only 4 numbers")
#     seti = set()
#     for i in guess:
#         seti.add(i)
#     if len(seti) != 4:
#         return (False, "Enter 4 different numbers.")
#     return (True, "good")


def is_new_guess(guess: str, history: set[str]) -> bool:

    if guess in history:
        return False



