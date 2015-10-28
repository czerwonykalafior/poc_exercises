__author__ = 'CzerwonyKalafior'
__project__ = 'StreetArt'

class Player:
    """ Player's class which consist of : pocket ($), skills, volume (range)
    """
    def __init__(self):
        self.pocket  = 0
        # 0 - Rock, 1 - Pop, 2 - Jazz, 3 - Techno
        self.skills = {0 : 1,
                       1 : 1,
                       2 : 0,
                       3 : 1}
        # 0 - classic (owned) 50dB , 1 - acoustic 100dB, 2 - amp 150dB
        self.volume = {0 : 1,
                       1 : 0,
                       2 : 0}
