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
    print SCORES[player]
    if board.check_win() != None:
        return (SCORES[board.check_win()], None)
    elif player == provided.PLAYERX:
        best = ( -2, None)
        empty_squers = board.get_empty_squares()
        for possible_move in empty_squers:
            clone = board.clone()
            clone.move(possible_move[0], possible_move[1], player)
            value = mm_move(clone, provided.switch_player(player))
            if value[0] > best[0]:
                best = (value[0], (possible_move))
        return best
    else:
        best = (2, None)
        empty_squers = board.get_empty_squares()
        for possible_move in empty_squers:
            clone = board.clone()
            clone.move(possible_move[0], possible_move[1], player)
            value = mm_move(clone, provided.switch_player(player))
            if value[0] < best[0]:
                best = (value[0], (possible_move))
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
list_board = [[1,1,1],[1,1,1],[1,1,1]]
board1 = provided.TTTBoard(3, False,list_board)

print "Start"
t = mm_move(board1, provided.PLAYERX)
print "Output:", t
# provided.play_game(move_wrapper, 1, False)
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
