"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
__author__ = 'CzerwonyKalafior'
__project__ = 'poc_fifteen_template'
"""
import poc_fifteen_gui


class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        s = [[str(e) for e in row] for row in self._grid]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        pp_grid = '\n'.join(table)

        return pp_grid + "\n"

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return row, col
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Travers the rest of the game grid starting from (target_row, target_col) checking if it's solved
        Returns a boolean
        """

        tile_zero_pos = self.current_position(0, 0)
        if tile_zero_pos != (target_row, target_col):
            return False

        row = tile_zero_pos[0]
        col = tile_zero_pos[1] + 1
        while row < self._height and col < self._width:
            if not self.solved(row, col):
                return False
            if col < self._width - 1:
                col += 1
            else:
                col = 0
                row += 1
        return True

    def solved(self, target_row, target_col):
        """
        Helper function. Return True if tail is on its place.
        :param target_row:
        :param target_col:
        :return: boolean
        """

        return (target_row, target_col) == self.current_position(target_row, target_col)

    def go_to_position(self, target_row, target_col, avoid_target=None):
        """
        Helper function. Moving the zero tile to given position. If 'avoid_target' given it's gets messy.
        Maybe later divide it in two functions.
        :type avoid_target: tuple
        :param avoid_target: Not crossing the target. Cyclic move.
        :param target_col: :param target_row:
        :return: strings: left = 'l', right = 'r', up = 'u', down = 'd'
        """
        result = ''
        assert (target_row, target_col) != avoid_target, "You said I should avoid it"
        while (target_row, target_col) != self.current_position(0, 0):
            move = ''
            zero_tile_pos = self.current_position(0, 0)
            row = target_row - zero_tile_pos[0]
            col = target_col - zero_tile_pos[1]

            if row < 0 and (zero_tile_pos[0] - 1, zero_tile_pos[1]) != avoid_target:
                move += 'u'
            elif col < 0 and (zero_tile_pos[0], zero_tile_pos[1] - 1) != avoid_target:
                move += 'l'
            elif col > 0 and (zero_tile_pos[0], zero_tile_pos[1] + 1) != avoid_target:
                move += 'r'
            elif row > 0 and (zero_tile_pos[0] + 1, zero_tile_pos[1]) != avoid_target:
                move += 'd'
            else:
                if zero_tile_pos[0] == 0:
                    self.go_to_position(avoid_target[0] + 1, avoid_target[1], avoid_target)
                elif zero_tile_pos[0] == avoid_target[0]:
                    self.go_to_position(avoid_target[0] - 1, avoid_target[1], avoid_target)
                else:
                    self.go_to_position(avoid_target[0], avoid_target[1] - 1, avoid_target)
            self.update_puzzle(move)
            result += move
        return result

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string

        zero_tail go_to_position(target_row, target_col)
        assert lower_row_invariant(target_row, target_col)
        target_is = current_position(target_row, target_col)
        go_to_position(target) don't cross the solved tiles
        target_is = current_position(target_row, target_col)
        set the column first :
        go_to_position(target_is[row], target[col + 1) or -1 (on it's left or right) don't cross the target
        go_to_position(target) don't cross the solved tiles
        set the row:
        go_to_position(target_is[row - 1], target[col]
        go_to_position(target) don't cross the solved tiles

        """
        self.go_to_position(target_row, target_col)
        assert self.lower_row_invariant(target_row, target_col)

        while not self.solved(target_row, target_col):
            target_position = self.current_position(target_row, target_col)
            self.go_to_position(target_position[0], target_position[1])


        return ""

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""


# Start interactive simulation
# poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))

i_grid = [[0, 10, 9, 1],
          [6, 13, 15, 11],
          [5, 12, 2, 7],
          [3, 8, 14, 4]]

pzl = Puzzle(4, 4, i_grid)
pzl.solve_interior_tile(3, 3)
print pzl

# print pzl.current_position(3, 2)
# print pzl.lower_row_invariant(0, 0)
# print pzl.solve_interior_tile(4,4)
# print pzl.solved(3, 3)
#
# for row in range(4):
#     for col in range(4):
#         pzl = Puzzle(4, 4, i_grid)
#         avoid = (pzl.current_position(3, 3))
#         if (row, col) == avoid:
#             continue
#         print (row, col), pzl.go_to_position(row, col, avoid)
#         print pzl

# print pzl.go_to_position(0, 2, avoid)
# print pzl