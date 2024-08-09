from os import system, path
from random import randint


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checking if the given string is one alphabetic character, and if the given string didn't guessed before if so returning True, otherwise False.

    Parameters:
        letter_guessed (string): given input from the user.
        old_letters_guessed (list): list of letter the user already guessed.

    Returns:
        boolian: True if the string meets all requirements, False otherwise.
    """

    return (
        len(letter_guessed) == 1
        and letter_guessed.isalpha()
        and letter_guessed.lower() not in old_letters_guessed
    )


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Trying to update the list of letters guessed by the user if the given value is valid.
    If the given value is not valid then print error message, in addition print the list of the letters already guessed.

    Parameters:
        letter_guess (string): Given input from the user.
        old_letters_guessed (list): List of letters the user already guessed.

    Returns:
        boolian: True if the given value is valid and it managed to append it to the guessed letters list, False otherwise.
    """

    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True

    else:
        print(
            "X\nInvalid input, Here are the letters you already guessed:\n",
            " -> ".join(sorted(old_letters_guessed)),
        )
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    Returning the current state of the letters guessed from the secret word.

    Parameters:
        secret_word (string): The word the user needs to guess.
        old_letters_guessed (list): List of letter the user already guessed.

    Returns:
        string: string of the letters that already guessed.
    """

    return " ".join(
        [char if char in old_letters_guessed else "_" for char in secret_word]
    )


def check_win(secret_word, old_letters_guessed):
    """
    Checking if the user guessed all the letters.

    Parameters:
        secret_word (string): The word the user needs to guess.
        old_letters_guessed (list): list of letter the user already guessed.

    Returns:
        boolian: True if guessed all letters right, False otherwise.
    """

    return set(secret_word).issubset(old_letters_guessed)


def print_hangman(num_of_tries):
    """
    Printing the idle hangman ascii art according to the number of failed attempts of the user.

    Parameters:
        num_of_tries (int): Number of failed attempts to guess letters.

    Returns:
        None
    """

    print(HANGMAN_PHOTOS[num_of_tries])


def choose_word(file_path, index):
    """
    Choosing a word to play the game with.
    Selecting the word from a .txt file (words separated using space only-' ').

    Parameters:
        file_path (string): File path to file containing random words separated with space only(' ').
        index (int): The number of word to choose from the text (starting from 1 and can be bigger than the amount of words in the file- when true returns to the first position in the original word list in the file).

    Returns:
        tuple: (amount of words different from each other, chosen word)
    """

    with open(file_path, "r") as words_file:
        words = words_file.read().split()
        return (len(set(words)), words[(index % len(words)) - 1])


def print_start(max_tries):
    """
    Printing the start page of the game.

    Parameters:
        max_tries (int): Maximum number of tries for the user to guess wrong.

    Returns:
        None
    """

    print(
        """
            Welcome to the game Hangman
  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/
                     
            You have """,
        str(max_tries),
        """ tries""",
    )


def another_round():
    """
    Asking the user if he wants to play another round, the user must respond with y/n, if not responding correctly asking again.

    Parameters:

    Returns:
        boolian: True if the user wants to play again. False if not.
    """

    choice = input("\nYou wish to continue? (Y\\N): ").upper()
    if choice == "Y":
        return True

    elif choice == "N":
        return False

    else:
        print("\nInvalid input, please try again.\n")
        return another_round()


def check_if_path_exist(file_path):
    """
    Checking if the file path exists. If not, asking to write again.

    Parameters:
        file_path (string): Given file path by the user.

    Returs:
        string: Returning the file path if true, asking again if not.
    """

    if path.exists(file_path):
        return file_path
    else:
        return check_if_path_exist(input("\nInvalid path, please try again:\n"))


HANGMAN_PHOTOS = {
    0: "x-------x",
    1: """x-------x
 |
 |
 |
 |
 |""",
    2: """x-------x
|       |
|       0
|       
|
|""",
    3: """x-------x
|       |
|       0
|       |
|
|""",
    4: """x-------x
|       |
|       0
|      /|\\
|
|""",
    5: """x-------x
|       |
|       0
|      /|\\
|      /
|""",
    6: """x-------x
|       |
|       0
|      /|\\
|      / \\
|""",
}


def main(file_path=None):
    """
    The main function. The running of the code starts from here, creates all the necesary parameters like file path, maximum tries, secret word, number of tries etc.
    The while loop is the main loop of the script, there we asking the user for guesses, checking if true and keep going till the user gets the word right or fails and lose the game.
    The main function centralizes and makes use of all the functions accompanying the code.
    Here we also give the user the option to choose if he wants to continue or leave, if he wish to continue then the program will remeber the file path that the user inserted on the first round.

    Parameters:
        file_path (string): The file path which containing all the possible words to guess. By defult will be None but if was inserted before it will be remembered.

    Returns:
        None
    """
    MAX_TRIES = 6
    print_start(MAX_TRIES)
    path_to_text_file = (
        check_if_path_exist(input("\nenter your file path to txt file:\n"))
        if file_path == None
        else file_path
    )
    number_of_word_in_file = randint(0, 1000)
    secret_word = choose_word(path_to_text_file, number_of_word_in_file)[1]
    num_of_tries = 0
    old_letters_guessed = []

    print("\nLets go!\n")
    print_hangman(num_of_tries)
    print("\n", show_hidden_word(secret_word, old_letters_guessed))

    while num_of_tries != MAX_TRIES:
        letter_guess = input("\nGuess a letter: ")

        if try_update_letter_guessed(letter_guess, old_letters_guessed):
            print("\n", show_hidden_word(secret_word, old_letters_guessed), "\n")
            if check_win(secret_word, old_letters_guessed):
                print("\n YOU WON! \n")
                if another_round():
                    system("cls")
                    print("Ah sh*t.. Here we go again..\n")
                    main(path_to_text_file)
                else:
                    print("See Ya!")
                    exit()
            else:
                if letter_guess not in secret_word:
                    num_of_tries += 1
                    print(":(")
                    print_hangman(num_of_tries)
                else:
                    print("Good guess!\n")

                print("\nYou have ", str(MAX_TRIES - num_of_tries), " chances left\n")

    print("\n YOU LOSE!\nThe secret word was: " + secret_word)

    if another_round():
        system("cls")
        print("Ah sh*t.. Here we go again")
        main(path_to_text_file)
    else:
        print("See Ya!")
        exit()


if __name__ == "__main__":
    main()
