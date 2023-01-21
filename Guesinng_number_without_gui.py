import random

random_number = random.randint(1, 100)
tries = 3

while True:
    number_from_user = int(input())

    if number_from_user == random_number:
        print("Congratulations, you won!")
        break
    else:
        print("Sorry, but you lost!")
        print("Try again!")
        tries -= 1

        if tries <= 0:
            break

    if tries == 1:
        print(f"Don't worry you have {tries} try left!")
    else:
        print(f"Don't worry you have {tries} tries left!")
