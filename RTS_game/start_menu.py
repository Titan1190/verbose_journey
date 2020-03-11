from parent_classes.menu import menu

class start_menu(menu):
    def __init__(self):
        super().__init__(["START", "HELP", "SETTINGS", "QUIT"])

    def show_help():
        print('''
        # Game rules & Commands #

        START : Starts game
        HELP : Displays help
        SETTINGS: Displays settings
        QUIT: Ends game

        ''')

    def show_settings():
        print("UNDER CONSTRUCTION")

 # first input doesn't change index & when first run displays nothing

    def run_menu(self):
        index = 0
        while True:
            user_input = input("> ")
            index = super().run_menu(index, user_input)
            if user_input == "":
                if index == 0 :
                    # initiate game start
                    break
                elif index == 1:
                    show_help()
                elif index == 2:
                    show_settings()
                else:
                    break
