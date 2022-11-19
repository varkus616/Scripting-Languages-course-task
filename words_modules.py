import random
import os


class Dictionary:
    def __init__(self, file_name="dictionary.txt"):
        try:
            if not os.path.exists(os.getcwd() + '\\' + file_name):
                print("File:" + os.getcwd() + '\\' + file_name + " is not existing")
                exit(1)
            else:
                with open('dictionary.txt', 'r') as file:
                    self.data = list(file.read().split())
                    if len(self.data) < 10:
                        print("DATABASE TOO SMALL")
                        exit(1)
        except FileNotFoundError:
            print("ERROR: CANNOT OPEN WORDS DATABASE !!!")
            exit(1)

    def return_word(self, difficulty=1) -> str:
        if difficulty == 1:#easy
            easy_data = [word for word in self.data if len(word) <= 4]
            return random.choice(easy_data)
        elif difficulty == 2:#medium
            medium_data = [word for word in self.data if len(word) <= 7]
            return random.choice(medium_data)
        elif difficulty == 3:#hardcore
            return random.choice(self.data)


class Validator:

    @staticmethod
    def check_word(word="") -> bool:
        return len(set(word.lower())) == len(word.lower())