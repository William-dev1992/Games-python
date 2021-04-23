
def play():
    print("*********************************")
    print("Welcome to the guessing game!")
    print("*********************************")

    secret_word = "papaya"
    choked = False
    answered = False

    while not choked and not answered:
        guess = input("Which letter?")
        guess = guess.strip()

        index = 0
        for letter in secret_word:
            if guess.upper() == letter.upper():
                print("Letter {} on position {}".format(guess, index))
            index = index + 1

        print("playing")

    print("End game!")


if __name__ == "__main__":
    play()
