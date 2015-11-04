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

    result = minimax(board,player)
    # if player == provided.PLAYERX:
    #     result = sorted(result, reverse= True)
    #
    # else:
    #     result = sorted(result)
    return result


def minimax(board, player, lvl = 0 ):
    score_possible_move = []
    result = []
    if len(board.get_empty_squares()) == 0:
        return (0, (-1, -1))
    else:

        empty_squares = board.get_empty_squares()
        for possible_move in empty_squares:

            print possible_move
            clone_board = board.clone()
            # print clone_board
            clone_board.move(possible_move[0], possible_move[1], player)

            if clone_board.check_win() != None:
                print "end", clone_board.check_win()
                print clone_board
                score_possible_move.extend([(SCORES[clone_board.check_win()], possible_move)])
                print "result:", score_possible_move, player
                if player == provided.PLAYERX:
                    result = sorted(score_possible_move, reverse= True)
                    score_possible_move = result[0]

                else:
                    result = sorted(score_possible_move)
                    score_possible_move = result[0]
            else:
                score_possible_move.append(minimax(clone_board, provided.switch_player(player)))

        return score_possible_move


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
list_board = [[3,2,1],[3,2,1],[1,3,2]]
board1 = provided.TTTBoard(3, False,list_board)

print "Start"
t = mm_move(board1, provided.PLAYERX)
print "Output:", t
# provided.play_game(move_wrapper, 1, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
