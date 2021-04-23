import random


def play():
    print("*********************************")
    print("Welcome to the guessing game!")
    print("*********************************")

    secret_number = random.randrange(1, 101)
    max_of_tries = 0
    points = 1000

    print("Choose the difficulty")
    print("[1] Easy [2] Normal [3] Hard")

    level = int(input("Define the level: "))

    if level == 1:
        max_of_tries = 20
    elif level == 2:
        max_of_tries = 8
    elif level == 3:
        max_of_tries = 3
    else:
        print("You must choose one option between 1,2 and 3.")

    for rounds in range(1, max_of_tries + 1):
        print("Try {} of {}".format(rounds, max_of_tries))
        print("The number must be between 1 and 100")
        guess = int(input("Type any number: "))

        right = guess == secret_number
        higher = guess > secret_number
        smaller = guess < secret_number

        if guess < 1 or guess > 100:
            print("The number has to be between 1 and 100.")
            continue

        if right:
            print("Your answer is right and you made {} points!".format(points))
            break
        else:
            if higher:
                print("Your answer is wrong!")
                print("Your answer is higher then the correct number.")
            if smaller:
                print("Your answer is wrong!")
                print("Your answer is smaller then the correct number.")
            lost_points = abs(secret_number - guess)
            points = points - lost_points

    print("The game has ended!")


if __name__ == "__main__":
    play()
