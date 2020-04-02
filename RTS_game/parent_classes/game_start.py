from menu import menu

class game_start():

    def __init__(self):
        print('''
        ##########################################
            Welcome to the battle of the bands!
                ARE YOU READY TO ROCK??!!!!
        ##########################################
        ''')

    def choose_race(self):
        print("SELECT YOUR RACE")
        races = menu([" Classical ", " Alternative/Rock ", " Rap "])
        index = races.run_menu(0, "")

        while True:
            user_input = input("> ")
            index = races.run_menu(index, user_input)

            if index == 0 :
            # Classical Description
            elif index == 1 :
            # Description
            else:
            # Description
            if user_input == "":
                self.race = races.menu_items
                break
