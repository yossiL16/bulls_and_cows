import random
from tabnanny import check

def generate_secret(length: int = 4) -> str:
    list_numbers = set()
    str_secret_number = ""
    for i in range(length):
        while True:
            secret_number = random.randint(1,9)
            if secret_number not in list_numbers:
                list_numbers.add(secret_number)
                str_secret_number += str(secret_number)
                break
            else:
                continue
    return str_secret_number









