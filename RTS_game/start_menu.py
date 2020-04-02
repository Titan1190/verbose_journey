from parent_classes.menu import menu

class start_menu(menu):
    def __init__(self):
        super().__init__([])

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
        self.menu_items = ["START", "HELP", "SETTINGS", "QUIT"]

        print('''
###################################################

        ------------- INPUTS -------------------

        "d" to move menu selection to right
        "a" to move menu selection to left
        ""  to select menu item

###################################################
        ''')

        index = super().run_menu(0, "")

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
