"""
Different listeners sub-classes of Listener class
"""
__author__ = 'CzerwonyKalafior'
__project__ = 'StreetArt'


class Listener(object):
    """
    Parent class for listeners
    """

    def __init__(self, name, genre, cash, speed, probability):

        self.name = name
        self.genre = genre
        self.speed = speed
        self.cash = cash
        self.probability = probability

    def __str__(self):
        pp_listener = "And his name will be: %s.\nGenre: %s, Speed: %i, cash: %i$, Probability: %.2f"\
                      % (self.name, self.genre, self.speed, self.cash, self.probability)
        return pp_listener

    def give_money(self, in_range, genre):
        """
        Give money if have any to a musician- as long as he can hear it and a musician is playing
        :param genre: bool
        :param in_range: bool
        """

        if in_range and genre:
            self.cash -= 10
        return

    def move(speed):
        """
        Moving listener on the map
        :param speed: do know if it's needed yet
        """
        pass


class Chav(Listener):
    """
    Initialize a chav
    """

    def __init__(self):
        super(Chav, self).__init__("Waldek", "Techno", 100, 50, 0.3)

dres = Chav()
print dres
dres.give_money(True, True)
print dres
