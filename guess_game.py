import random

number = random.randint(1,10)


def guess_game():
    count = 0
    while True:
        count=count+1

        guess_number = int(input("Please guess the number between range 1 to 9 : > "))

        if guess_number == number:
            print("Congratulations , you guessed right !")
        elif guess_number > number:
            print("Number guesses is greater ")
        else:
            print("Number guesses is lower ")

        game_status = input("Enter exit if you wish to exit this game else type something else : ")
        if game_status=="exit":
            print(count)
            break

guess_game()


