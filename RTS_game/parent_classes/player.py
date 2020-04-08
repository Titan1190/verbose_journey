# user_variables = {name, hp = 100, gold = 0, wood = 0, race, currentUprgrades[types of upgrades]}

'''
Player():
  - Name, Race, Hp, Recourses, Upgrades
  - Able to take turn
    - Upgrade
    - Deploy unit
    - End turn
'''


class player:
  def __init__(self, race, **kwargs):
    self.race = race
    self.hp = 100
    self.gold = 0
    self.wood = 0
    for key, value in kwargs.items():
      setattr(self, key, value)
