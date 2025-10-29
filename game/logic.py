

def score_guess(secret: str, guess: str) -> tuple[int, int]:

    bull = 0
    cows = 0

    for i in range(0,len(guess)):
        if secret[i] == guess[i]:
            bull += 1
        if guess[i] in secret:
            cows += 1

    return (bull, cows)
