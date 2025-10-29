

def score_guess(secret: str, guess: str) -> tuple[int, int]:

    bull = 0
    cows = 0

    for i in range(0,len(guess)):
        if secret[i] == guess[i]:
            bull += 1
        if guess[i] in secret:
            cows += 1

    return (bull, cows)


def is_won(bulls: int, length: int) -> bool:
    if bulls == length:
        return True


def init_state(secret: str, length: int, max_tries: int | None, unique_digits: bool, allow_leading_zero: bool):

    game_state = {
        "secret" : secret,
        "length" : length,
        "max_tries" : max_tries,
        "tries_used" : 0,
        "unique_digits" : unique_digits,
        "allow_leading_zero" : allow_leading_zero,
        "history" : [],
        "seen" : set()}

    return game_state


def apply_guess(state: dict, guess: str) -> tuple[int, int]:


    score1, score2 = score_guess(state["secret"], guess)
    state["tries_used"] += 1
    state["seen"].add(guess)
    state["history"].append(tuple(list((guess, score1, score2))))

    return tuple((score1,score2))












