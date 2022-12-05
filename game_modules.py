import pyinputplus as pyip
import datetime
from words_modules import *
from time import sleep


class Stats:

    def __init__(self, attempts=0):
        self.bulls = 0
        self.cows = 0
        self.attempts = attempts

    def export_score(self):
        with open("highscore.txt", "a") as file:
            file.write(f"Game day:{datetime.datetime.now()} , bulls:{self.bulls} , cows:{self.cows} , "
                       f"attempts:{self.attempts}\n")
        print("\nExported !\n")


class Engine:

    def __init__(self):
        self.default_attempts = 3
        self.stats = Stats(self.default_attempts)
        self.words_db = Dictionary()
        self.validator = Validator()
        self.difficulty = 1

    def change_attempts(self, num_of_attempts):
        if num_of_attempts <= 0:
            self.stats.attempts = 1
            self.default_attempts = 1
            print("Attempts can't be lower than 1.\n"
                  "Changed attempts to 1.")
        else:
            self.default_attempts = num_of_attempts
            self.stats.attempts = self.default_attempts

    def change_difficulty(self, diff):
        if diff < 1 or diff > 3:
           print("Cannot change difficulty.")
        else:
            self.difficulty = diff

    @staticmethod
    def check_user_word(stats, user_guess, word):
        for (user_char, word_char) in zip(user_guess, word):
            if user_char in word:
                if user_char == word_char:
                    stats.bulls += 1
                else:
                    stats.cows += 1
        return stats.bulls, stats.cows

    @staticmethod
    def check_guess_conditions(stats, word):
        if stats.bulls == len(word):
            return True, stats.attempts
        else:
            stats.attempts -= 1
            return False, stats.attempts

    def start_game(self):
        print(self.difficulty)
        print("Computer is choosing word...")
        sleep(1)

        word = self.words_db.return_word(self.difficulty)
        print(f"Computer chose a word. Word length = {len(word)}")
        while self.stats.attempts > 0:
            self.stats.bulls = 0
            self.stats.cows = 0
            user_guess = pyip.inputStr("Have a guess:")
            if not self.validator.check_word(user_guess):
                print("Your word is not isogram !")
            else:
                Engine.check_user_word(self.stats, user_guess, word)

                guess_value, self.stats.attempts = Engine.check_guess_conditions(self.stats, word)
                if guess_value:
                    print(f"You guessed right !\n"
                          f"On attempt {self.stats.attempts}.")
                    sleep(1)
                    print_menu()
                    break
                else:
                    if self.stats.attempts == 0:
                        print("! YOU LOST !\n"
                            f"Bulls[{self.stats.bulls}] and Cows[{self.stats.cows}]\n"
                            f"Attempts[{self.stats.attempts}]\n"
                            f"The word:{word}\n")
                        self.stats.attempts = self.default_attempts
                        sleep(1)
                        print_menu()
                        break
                    else:
                        print(f"Bad guess !\n"
                              f"Bulls[{self.stats.bulls}] and Cows[{self.stats.cows}]\n"
                              f"Attempts[{self.stats.attempts}]")


def print_menu():
    print("Welcom to Bulls&Cows !\n"
          "Please select one of the options listed below.\n"
          "1 - New Game\n"
          "2 - Rules of The Game\n"
          "3 - Change the number of attempts\n"
          "4 - Change difficulty\n"
          "5 - Export score\n"
          "6 - Exit\n")


def print_rotg():
    print("Bulls and Cows is a 2 player game.\n"
          "One player thinks of a word, while the other player tries to guess it.\n")


def handle_menu_input(engine):

    user_input = pyip.inputNum(prompt=">?")
    while user_input not in range(1, 7):
        print(f"Bad Input:({user_input})")
        user_input = pyip.inputNum(prompt=">?")
    else:
        if user_input == 1:
            engine.start_game()
        elif user_input == 2:
            print_rotg()
        elif user_input == 3:
            attempts = pyip.inputNum(prompt="Attempts:")
            engine.change_attempts(attempts)
        elif user_input == 4:
            print("1.Easy\n"
                  "2.Medium\n"
                  "3.Hardcore\n")
            difficulty = pyip.inputNum(prompt="Difficulty:")
            engine.change_difficulty(difficulty)
        elif user_input == 5:
            engine.stats.export_score()
        elif user_input == 6:
            print("Bye !")
            exit(1)