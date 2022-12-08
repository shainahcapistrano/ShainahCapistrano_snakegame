import random
BLANK = " "
COMPUTER = "o"
PLAYER = "x"

class Tic_Tac_Toe_logic:

    def __init__(self, width, height):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    ## This method returns any move that will let the chosen player when
    ## side should be passed either "x" or "o"
    def find_winning_move(self, side):
        for row in range(2):
            print("Here we want to check if any row could give us a win")

        for col in range(2):
           print("Here we want to check if any column could give us a win")

        ## diagonal
        if self.board[0][0] == self.board[1][1] == side \
                and self.board[2][2] == BLANK:
            return (2, 2)
        elif self.board[0][0] == self.board[2][2] == side \
                and self.board[1][1] == BLANK:
            return (1, 1)
        elif self.board[1][1] == self.board[2][2] == side \
                and self.board[0][0] == BLANK:
            return (0, 0)
        ## diagonal
        elif self.board[0][2] == self.board[1][1] == side \
                and self.board[2][0] == BLANK:
            return (2, 0)
        elif self.board[0][2] == self.board[2][0] == side \
                and self.board[1][1] == BLANK:
            return (1, 1)
        elif self.board[1][1] == self.board[2][0] == side \
                and self.board[0][2] == BLANK:
            return (0, 2)
        else:
            return ()



    def find_best_move(self):
        move = self.find_winning_move(COMPUTER)
        if move == ():
            move = self.find_winning_move(PLAYER)

        if move == ():
            optimal_moves = [(1, 1), (0, 0), (0, 2), (2, 0), (2, 2), (0, 1), (1, 0), (1, 2), (2, 1)]
            for possible_move in optimal_moves:
                if self.board[possible_move[0]][possible_move[1]] == BLANK:
                    return possible_move
            return ()
        else:
            return move



    def control_board(self, position, side):
        row = position[0]
        column = position[1]

        if self.is_open((row,column)):
            self.board[row][column] = side
            return (row,column)
        else:
            return(-1,-1)


    def is_open(self, move):
        if self.board[move[0]][move[1]] == BLANK:
            return True
        else:
            return False

    def test_for_winner(self):
        # print("Test for winner")
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] \
                    and self.board[row][0] != BLANK:
                return self.board[row][0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] \
                    and self.board[0][col] != BLANK:
                return self.board[0][col]
        ##diagonal 1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] \
                and self.board[0][0] != BLANK:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] \
                and self.board[0][2] != BLANK:
            return self.board[0][2]

        return BLANK

    def test_for_draw(self):
        # print("Test for Draw")
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == BLANK:
                    return False
        return True

    def draw_board(self):

        for row in range(2,-1,-1):
            for col in range(3):
                print(self.board[row][col], end = " ")
                if col < 2:
                    print(" |", end  = " ")
            print()
            if row > 0:
                print("---|----|---")
        print("---------------------------------")

def tester():
    logic = Tic_Tac_Toe_logic(600,600)
    print(logic)

if __name__ == "__main__":
    tester()

