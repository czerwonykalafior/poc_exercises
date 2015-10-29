__author__ = 'CzerwonyKalafior'
__project__ = 'TTT'

"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
#
# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    # print board

    if board.check_win():
        print "if", (SCORES[board.check_win()])
        return (SCORES[board.check_win()])

    empty = board.get_empty_squares()

    for possible_move in empty:
        best = -2
        temp_board = board.clone()
        temp_board.move(possible_move[0], possible_move[1], player )
        val =  (mm_move(temp_board, provided.switch_player(player)))

        if player == 2:
            if val > best:
                best = val
        else:
            if val < best:
                best = val
        return best

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.
list_board = [[3,2,3],[3,2,1],[1,3,2]]
board1 = provided.TTTBoard(3, False,list_board)

print mm_move(board1, provided.PLAYERX)

#provided.play_game(move_wrapper, 1, False)
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
