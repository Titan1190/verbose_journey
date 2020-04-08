from menu import menu
import player as pl

class game_start():

    def __init__(self):
        print('''
        ##########################################
            Welcome to the battle of the bands!
                ARE YOU READY TO ROCK??!!!!
        ##########################################
        ''')
        race = self.choose_race()
        user = pl.player(race)
        print(user.race)

    def choose_race(self):
        print("SELECT YOUR RACE")
        races = menu([" Classical ", " Alternative ", " Rap " , " Jazz "])
        index = races.run_menu(0, "")

        while True:
            user_input = input("> ")
            index = races.run_menu(index, user_input)

            # Description
            if user_input == "":
                return races.menu_items[index]
                break

            if index == 0 :
                # Classical Description
                print('''
                Musical purists, classical is where all music springs.
                Devoted to clarity & with a bit too much coin in their pocket
                the Classists progress slowly but reach the epitome of music.
                ''')

            elif index == 1 :
                # Alternative Description
                print('''
                Original, fresh and bold; alternative turns creativity into sound.
                With a need for experentation & unafraid to try something new
                their music can range from terrible to fantastic depending on their
                creative fancies.
                ''')

            elif index == 2:
                # Rap Description
                print('''
                What up homie? Rap is about speed & lyricism. Music is meant to
                hit the listener, with their words and realities. Cash comes fast,
                beats go flying but few last forever.
                ''')

            elif index == 3:
                # Jazz Description
                print('''
                Jazz. That golden swing that never grows old. Jazz is steady, its
                original. It just don't stop. Bringing in some steady cash &
                some solid peices but never failing to feel new & fresh. Jazz is
                the music of the soul.
                ''')
