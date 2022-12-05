from game_modules import *

#  To use this project you need to install pyinputplus
#  Open CLI and type 'python pip install --user pyinputplus'

engine = Engine()
print_menu()
while True:
    handle_menu_input(engine)
