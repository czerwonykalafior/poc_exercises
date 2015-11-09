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

    def go_to_target(self, target_row, target_col):
        """
        Moving to index taken my given tile. e.g '15'
        :param target_row:
        :param target_col:
        :return:
        """
        tuple_idx_row = self.current_position(target_row, target_col)[0]
        tuple_idx_col = self.current_position(target_row, target_col)[1]
        move = self.go_to_position(tuple_idx_row, tuple_idx_col)
        return move

    def go_to_position(self, target_row, target_col):
        """
        Move to given index e.g [3][3]
        :param target_row:
        :param target_col:
        :return:
        """

        row_diff = target_row - self.current_position(0, 0)[0]
        col_diff = target_col - self.current_position(0, 0)[1]

        move = ''
        move += 'lr'[col_diff > 0] * abs(col_diff)
        move += 'ud'[row_diff > 0] * abs(row_diff)
        self.update_puzzle(move)
        return move

    def round_tile(self, target_row, target_col, clockwise=None):
        """
        Go around with clockwise direction a solving tile.
        :type clockwise: boolean
        :param target_row:
        :param target_col:
        :return:
        """

        zero_position = self.current_position(0, 0)
        row = self.current_position(target_row, target_col)[0]
        col = self.current_position(target_row, target_col)[1]
        loop = 'ruullddr'
        position_order = {(row + 1, col    ): 0,
                           (row + 1, col + 1): 1,
                           (row    , col + 1): 2,
                           (row - 1, col + 1): 3,
                           (row - 1, col    ): 4,
                           (row - 1, col - 1): 5,
                           (row,     col - 1): 6,
                           (row + 1, col - 1): 7,}

        if clockwise:
            loop = 'luurrddl'
            position_order = { (row + 1, col    ): 0,
                               (row + 1, col + 1): 7,
                               (row    , col + 1): 6,
                               (row - 1, col + 1): 5,
                               (row - 1, col    ): 4,
                               (row - 1, col - 1): 3,
                               (row,     col - 1): 2,
                               (row + 1, col - 1): 1,}

        move = loop[position_order[zero_position]:]
        self.update_puzzle(move)
        return move

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

        move = ''
        clockwise = False
        move += self.go_to_position(target_row, target_col)
        assert self.lower_row_invariant(target_row, target_col)
        move += self.go_to_position(self.current_position(target_row, target_col)[0], self.current_position(0, 0)[1])

        # column solving
        # on the left
        turn = 'urrd'
        if self.current_position(target_row, target_col)[0] == 0:
            turn = 'drru'
        # on the right
        if self.current_position(0, 0)[1] - self.current_position(target_row, target_col)[1] < 0:
            turn = 'ulld'
            if self.current_position(target_row, target_col)[0] == 0:
                turn = 'dllu'
                clockwise = True
        move += self.go_to_target(target_row, target_col)
        while target_col != self.current_position(target_row, target_col)[1]:
            move += turn
            self.update_puzzle(turn)
            move += self.go_to_target(target_row, target_col)

        # row solving
        if not self.solved(target_row, target_col):
            move += self.round_tile(target_row, target_col, clockwise)
            move += self.go_to_target(target_row, target_col)
            while target_row != self.current_position(target_row, target_col)[0]:
                move += self.round_tile(target_row, target_col, False)
                move += self.go_to_target(target_row, target_col)
        move += self.go_to_position(target_row, target_col - 1)
        assert self.lower_row_invariant(target_row, target_col - 1)

        return move

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

i_grid = [[12, 3, 4,13],
          [1, 6, 2, 9],
          [5, 8, 11, 0],
          [10, 7, 14, 15]]

pzl = Puzzle(4, 4, i_grid)

print pzl
# print pzl.go_to_target(3, 3)
# print pzl.round_tile(3, 3, True)
print pzl.solve_interior_tile(3, 1)
print pzl