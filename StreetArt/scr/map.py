"""
Map for a game
"""
__author__ = 'CzerwonyKalafior'
__project__ = 'StreetArt'

# Map constants
MAP_HEIGHT = 10
MAP_WIDTH = 10
GRID_FILL = 0


class Map:
    """
    Map class represented as a grid with MAP_HEIGHT and MAP_WIDTH global constants.
    """
    def __init__(self):
        self.grid = [[GRID_FILL for _ in range(MAP_HEIGHT)] for _ in range(MAP_WIDTH)]

    def __str__(self):
        pp_map = ""
        for row in self.grid:
            pp_map += str(row) + '\n'
        return pp_map

    def player_range(self, position, range):
        """
        Set the player's position and his range
        :return: None
        """


map1 = Map()
print map1
