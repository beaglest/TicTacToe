class Board:

    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]

    def end_game(self):
        cnt = 0
        for j in range(3):
            cnt += self.board[j].count(' ')
        if cnt == 0:
            print("Draw. The game is over!")
            return True
        for i in range(3):

            column = [row[i] for row in self.board]
            if i == 0:
                cross = [self.board[0][0], self.board[1][1], self.board[2][2]]
            elif i == 1:
                cross = [self.board[0][2], self.board[1][1], self.board[2][0]]
            else:
                cross = [' ', ' ', ' ']

            if self.board[i].count('X') == 3 or column.count('X') == 3 or cross.count('X') == 3:
                print("Player X wins!")
                return True
            if self.board[i].count('O') == 3 or column.count('O') == 3 or cross.count('O') == 3:
                print("Player O wins!")
                return True

        return False

    def print_board(self):

        for i in range(3):
            for j in range(3):
                print(' ' + self.board[i][j]+' ', end='')
                if j != 2:
                    print('|', end='')
            if i != 2:
                print('\n------------')
        print('\n')

    def verify_input(self, r, c):

        if (r > 2 or r < 0) or (c > 2 or c < 0):
            print("Wrong input. You should select between 0 and 2\n")
            return False

        if self.board[r][c] == 'X' or self.board[r][c] == 'O':
            print("This cell is already occupied. You should select another\n")
            return False

        return True

    def user_input(self, user):
        u = user % 2 + 1

        ui = input(f"User{u}: Select your choice (a,b): ")
        x = ui.split(',')
        r, c = int(x[0]), int(x[1])

        while not self.verify_input(r, c):
            ui = input(f"User{u}: Select your choice (a,b): ")
            x = ui.split(',')
            r, c = int(x[0]), int(x[1])

        if u == 1 :
            self.board[r][c] = 'X'
        else:
            self.board[r][c] = 'O'
