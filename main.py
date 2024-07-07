from board import Board


if __name__ == '__main__':
    board = Board()
    board.print_board()
    j = 0
    end_of_game = False
    while not end_of_game:
        board.user_input(j)
        board.print_board()
        end_of_game = board.end_game()
        j += 1
