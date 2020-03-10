class menu:

    def __init__(self, menu_items):
        self.menu_items = menu_items

    def disp_menu(self, pos):
        copy = self.menu_items[0:]
        copy[pos] = "<" + copy[pos] + ">"
        print (copy)

    def run_menu(self):
        index = 0
        while True:
            user_input = input("> ")

            if (user_input == "a"):
                index = index - 1

            elif (user_input == "d"):
                index = index + 1


            disp_menu(self, index % len(self.menu_items))
