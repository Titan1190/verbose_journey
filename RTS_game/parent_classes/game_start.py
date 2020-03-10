from menu import menu

class game_start:

    def __init__(self):
        print('''
        ##########################################
        Welcome to the battle of the bands!
        ARE YOU READY TO ROCK??!!!!
        ##########################################
        ''')
        self.start = menu(["START", "HELP", "SETTINGS", "QUIT"])
