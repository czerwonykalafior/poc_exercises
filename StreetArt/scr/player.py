"""
Player
"""
import pprint

__author__ = 'CzerwonyKalafior'
__project__ = 'StreetArt'


# Constants representation of genre
ROCK = 1
POP = 2
JAZZ = 3
TECHNO = 4

CLASSIC = 50
ACOUSTIC = 90
AMP = 150

# Map constants for printing
STRMAP = {ROCK: "Rock",
          POP: "Pop",
          JAZZ: "Jazz",
          TECHNO: "Techno"}


class Player:
    """
     Player's class which consist of : pocket ($), skills, volume (range)
    """
    def __init__(self):
        """
        pocket: money gain so far
        skills: 0 - classic (owned) 80dB , 1 - acoustic 100dB, 2 - amp 150dB
        volume: 0 - Rock, 1 - Pop, 2 - Jazz, 3 - Techno
        """
        self.pocket = 0

        self.skills = {ROCK: 1,
                       POP: 1,
                       JAZZ: 0,
                       TECHNO: 1}

        self.volume = {CLASSIC: 1,
                       ACOUSTIC: 0,
                       AMP: 0}

        self.now_playing = TECHNO

    def __str__(self):
        """
        Override __str__ method
        """
        pp = pprint.PrettyPrinter(indent=4)
        return str(pp.pprint(STRMAP))

    def change_genre(self, genre):
        """
        Change actual genre
        :param genre:
        :return:
        """
        self.now_playing = genre

player1 = Player()
print player1
