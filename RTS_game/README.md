Summary of game:

l    l-----> - <-----l    l
l <> l-----> - <-----l <> l
l    l-----> - <-----l    l

Game Map Example

Base & 3 rows + reflection
Each player has own race with specific upgrades, units & advantages
Turn taken, player can make as many upgrades as wanted & deploy 1 troop per row | waits for both inputs
After turn is taken, all units move up 1 toward opponenet
When base attacked, player lose life & unit is attacked for base defence value
Game ends when player defeats opponenet

Classes:
  Player():
  - Name, Race, Hp, Recourses
  - Able to take turn
    - Upgrade
    - Deploy unit
    - End turn

  Race():
    - Track current values of each upgrade
    race_name():
      - Units
      - Benefits
      - Upgrades

  Map():
    row():
      - Displays map
      - Displays units
      - Moves units forward when turn ends
      // Perhaps a list

  Units():
    - HP, Race, Dmg, Range, abilities
    - Each race should have a unit in each category & a unique unit
