__author__ = 'CzerwonyKalafior'
__project__ = 'StreetArt'

MAP_HEIGHT = 600
MAP_WIDTH = 800
GRID_FILL = 0

class Map:
    """ Create a grid with MAP_HEIGHT and MAP_WIDTH global constants.
    """
    def __init__(self):
        __grid__ = [[GRID_FILL for dummy_h in range(MAP_HEIGHT)] for dummy_w in range(MAP_WIDTH)]

