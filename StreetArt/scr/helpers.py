"""
Classes and methods that make things easier
"""
__author__ = 'CzerwonyKalafior'
__project__ = 'StreetArt'


class Queue:
    """
    A simple implementation of a FIFO queue.
    """

    def __init__(self):
        """
        Initialize the queue.
        """
        self._items = []

    def __len__(self):
        """
        Return the number of items in the queue.
        """
        return len(self._items)

    def __iter__(self):
        """
        Create an iterator for the queue.
        """
        for item in self._items:
            yield item

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(self._items)

    def enqueue(self, item):
        """
        Add item to the queue.
        :param item:
        """
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the least recently inserted item.
        """
        return self._items.pop(0)

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._items = []

EMPTY = 0
FULL = 1


class Grid(object):
    """
    Implementation of 2D grid of cells
    Includes boundary handling
    """

    def __init__(self, grid_height, grid_width):
        """
        Initializes grid to be empty, take height and width of grid as parameters
        Indexed by rows (left to right), then by columns (top to bottom)
        """
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._cells = [[EMPTY for _ in range(self._grid_width)]
                       for _ in range(self._grid_height)]

    def __str__(self):
        """
        Return multi-line string represenation for grid
        """
        ans = ""
        for row in range(self._grid_height):
            ans += str(self._cells[row])
            ans += "\n"
        return ans

    def get_grid_height(self):
        """
        Return the height of the grid for use in the GUI
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Return the width of the grid for use in the GUI
        """
        return self._grid_width

    def clear(self):
        """
        Clears grid to be empty
        """
        self._cells = [[EMPTY for _ in range(self._grid_width)]
                       for _ in range(self._grid_height)]

    def set_empty(self, row, col):
        """
        Set cell with index (row, col) to be empty
        :param col:
        :param row:
        """
        self._cells[row][col] = EMPTY

    def set_full(self, row, col):
        """
        Set cell with index (row, col) to be full
        :param col:
        :param row:
        """
        self._cells[row][col] = FULL

    def is_empty(self, row, col):
        """
        Checks whether cell with index (row, col) is empty
        :param row:
        :param col:
        """
        return self._cells[row][col] == EMPTY

    def set_val(self, row, col, val):
        """
        Setting
        :param row:
        :param col:
        :param val:
        """
        self._cells[row][col] = val

    def get_val(self, row, col):
        """
        Returning the value
        :param row:
        :param col:
        """
        return self._cells[row][col]

    def set_all_val_to(self, val):
        """
        Fill grid with given value
        :param val:
        """
        self._cells = [[val for _ in range(self._grid_width)]
                       for _ in range(self._grid_height)]

    def four_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col)
        :param row:
        :param col:
        """
        ans = []
        if row > 0:
            ans.append((row - 1, col))
        if row < self._grid_height - 1:
            ans.append((row + 1, col))
        if col > 0:
            ans.append((row, col - 1))
        if col < self._grid_width - 1:
            ans.append((row, col + 1))
        return ans

    def eight_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col) as well as
        diagonal neighbors
        :param row:
        :param col:
        """
        ans = []
        if row > 0:
            ans.append((row - 1, col))
        if row < self._grid_height - 1:
            ans.append((row + 1, col))
        if col > 0:
            ans.append((row, col - 1))
        if col < self._grid_width - 1:
            ans.append((row, col + 1))
        if (row > 0) and (col > 0):
            ans.append((row - 1, col - 1))
        if (row > 0) and (col < self._grid_width - 1):
            ans.append((row - 1, col + 1))
        if (row < self._grid_height - 1) and (col > 0):
            ans.append((row + 1, col - 1))
        if (row < self._grid_height - 1) and (col < self._grid_width - 1):
            ans.append((row + 1, col + 1))
        return ans

    def clone(self):
        """
        Return a copy of the grid.
        """
        return Grid(self._grid_height, self._grid_width)

    @staticmethod
    def get_index(point, cell_size):
        """
        Takes point in screen coordinates and returns index of
        containing cell
        :param point:
        :param cell_size:
        """
        return point[1] / cell_size, point[0] / cell_size
