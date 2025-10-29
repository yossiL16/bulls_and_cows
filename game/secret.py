import random
from tabnanny import check

def generate_secret(length: int = 4) -> str:

    list_secret_number = []
    for i in range(length):
        while True:
            secret_number = random.randint(1,9)
            if secret_number not in list_secret_number:
                list_secret_number.append(secret_number)
                break
            else:
                continue
    return str(list_secret_number)








