from game.secret import generate_secret
from game.validate import is_valid_guess

print(generate_secret())
guss = input("enter: ")
is_valid_guess(guss)