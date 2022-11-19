import pyinputplus as pyip
import datetime
from words_modules import *
from time import sleep


class Stats:
    bulls = 0
    cows = 0
    attempts = 0

    def export_score(self):
        with open("highscore.txt", "a") as file:
            file.write(f"Game day:{datetime.datetime.now()} , bulls:{self.bulls} , cows:{self.cows} , "
                       f"attempts:{self.attempts}\n")
        print("\nExported !\n")


class Engine:
    stats = Stats()
    words_db = Dictionary()
    validator = Validator()

    difficulties = {"Easy": 1,
                    "Medium": 2,
                    "Hardcore": 3}
    difficulty = difficulties["Easy"]

    default_attempts = 3
    attempts = default_attempts

    def change_attempts(self, num_of_attempts):
        if num_of_attempts <= 0:
            self.attempts = 1
            self.default_attempts = 1
            print("Attempts can't be lower than 1.\n"
                  "Changed attempts to 1.")
        else:
            self.attempts = num_of_attempts
            self.default_attempts = num_of_attempts

    def change_difficulty(self, difficulty):
        if difficulty < 1 or difficulty > 3:
            print("Cannot change difficulty.")
        else:
            self.difficulty = difficulty

    def start_game(self):
        print("Computer is choosing word...")
        sleep(1)

        word = self.words_db.return_word(difficulty=self.difficulty)
        self.stats.bulls = 0
        self.stats.cows = 0

        print(f"Computer chose a word. Word length = {len(word)}")
        while self.attempts > 0:
            user_guess = pyip.inputStr("Have a guess:")
            if not self.validator.check_word(user_guess):
                print("Your word is not isogram !")
            else:
                for (user_char, word_char) in zip(user_guess, word):
                    if user_char in word:
                        if user_char == word_char:
                            self.stats.bulls += 1
                        else:
                            self.stats.cows += 1
                if self.stats.bulls == len(word):
                    print(f"You guessed right !\n"
                          f"On attempt {self.attempts}.")
                    self.stats.attempts = self.attempts
                    break
                else:
                    self.attempts -= 1
                    print(f"Bad guess !\n"
                          f"Bulls[{self.stats.bulls}] and Cows[{self.stats.cows}]\n"
                          f"Attempts[{self.attempts}]")
        print("! YOU LOST !\n"
              f"Bulls[{self.stats.bulls}] and Cows[{self.stats.cows}]\n"
              f"Attempts[{self.attempts}]\n")
        self.attempts = self.default_attempts
        print_menu()


def print_menu():
    print("Welcom to Bulls&Cows !\n"
          "Please select one of the options listed below.\n"
          "1 - New Game\n"
          "2 - Rules of The Game\n"
          "3 - Change the number of attempts\n"
          "4 - Change difficulty\n"
          "5 - Export score\n"
          "6 - Exit")


def print_rotg():
    print("Bulls and Cows is a 2 player game.\n"
          "One player thinks of a word, while the other player tries to guess it.")


engine = Engine()


def handle_menu_input():
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
            difficulty = pyip.inputNum(prompt="Difficulty:")
            engine.change_difficulty(difficulty)
        elif user_input == 5:
            engine.stats.export_score()
        elif user_input == 6:
            print("Bye !")
            exit(1)