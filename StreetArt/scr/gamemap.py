"""
Map for a game
"""
import helpers

__author__ = 'CzerwonyKalafior'
__project__ = 'StreetArt'

# Map constants
MAP_HEIGHT = 10
MAP_WIDTH = 10
GRID_FILL = 0


class GameMap(helpers.Grid):
    """
    Map class represented as a grid with MAP_HEIGHT and MAP_WIDTH global constants.
    """

    def __init__(self):
        super(GameMap, self).__init__(MAP_HEIGHT, MAP_WIDTH)

    def players_audibility(self, position, volume):
        """
        Set the player's position and his range using BFS. Changing the value of the grid to a distance value,
        which may
        :param position: Grid index selected by the player
        :param volume: Current volume of music (range)
        :return: Distance map, subclass of helpers.Grid
        """

        dist_map = self.clone()
        boundary = helpers.Queue()
        boundary.enqueue(position)

        while len(boundary) != 0:
            cell = boundary.dequeue()
            neighbors = dist_map.eight_neighbors(cell[0], cell[1])

            for nbr in neighbors:
                empty = dist_map.is_empty(nbr[0], nbr[1])
                not_to_far = dist_map.get_val(cell[0], cell[1]) < volume

                if empty and not_to_far:
                    dist_map.set_full(nbr[0], nbr[1])
                    boundary.enqueue(nbr)
                    dist_map.set_val(nbr[0], nbr[1], dist_map.get_val(cell[0], cell[1]) + 1)

        return dist_map

map1 = GameMap()
print map1.players_audibility((0, 0), 30)

