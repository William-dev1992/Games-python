import guess
import hangman


def choose_game():
    print("*********************************")
    print("*******Choose your game!*********")
    print("*********************************")

    print("[1]Hangman [2]Guess the number")

    game = int(input("Choose one: "))

    if game == 1:
        hangman.play()
    elif game == 2:
        guess.play()
    else:
        print("You can only choose between 1 and 2.")


if __name__ == "__main__":
    choose_game()

