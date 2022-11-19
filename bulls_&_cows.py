from game_modules import *
import unittest

#  To use this project you need to install pyinputplus
#  Open CLI and type 'python pip install --user pyinputplus'

#  Unit Tests


#class ValidatorTest(unittest.TestCase):                         # This class checks if a word is a isogram
#    def test_check_word(self):                                  # so it's very important to test.
#        test_validator = Validator()
#        self.assertTrue(test_validator.check_word("abc"))  # True
#        self.assertFalse(test_validator.check_word("abbc"))  # False


#val_test = ValidatorTest()

#val_test.test_check_word()

print_menu()
while True:
    handle_menu_input()
