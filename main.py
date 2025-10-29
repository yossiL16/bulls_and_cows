from game.secret import generate_secret
from game.validate import is_valid_guess
from game.logic import score_guess

secret = generate_secret()
print(secret)
guss = input("enter: ")
guss_cleane = "".join(guss.split())
rezolt_bool = is_valid_guess(guss_cleane)
score_guess(secret, guss)
