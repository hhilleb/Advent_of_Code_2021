class Board():
    def __init__(self, layout):
        self.layout = layout
        self.marked = [[False for i in range(len(layout[0]))] for j in range(len(layout))]
        self.bingo = False

    def cross_number(self, drawn_number):
        for i in range(len(self.layout[0])):
            for j in range(len(self.layout)):
                if self.layout[i][j] == drawn_number:
                    self.marked[i][j] = True

    def check_bingo(self):
        for row in self.marked:
            if row == [True for i in range(len(self.marked[0]))]:
                self.bingo = True
                return True
        for col in [[row[i] for row in self.marked] for i in range(len(self.marked))]:
            if col == [True for i in range(len(self.marked))]:
                self.bingo = True
                return True
        return False

    def score(self, drawn_number):
        score = 0
        for i in range(len(self.layout[0])):
            for j in range(len(self.layout)):
                if self.marked[i][j] == False:
                    score += self.layout[i][j]
        return score * drawn_number

    def __str__(self):
        return '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.layout]) + "\n"


with open('inputs/aoc_2021_input_4.txt') as f:
    drawn_numbers = [int(s) for s in f.readline().split(",")]
    boards = []
    board = []
    f.readline()
    for line in f:
        if line == "\n":
            boards.append(Board(board))
            board = []
        else:
            board.append([int(s) for s in line.split() if s.isdigit()])
    boards.append(Board(board))

def play_bingo(drawn_numbers, boards):
    first_winner = -1
    last_winner = -1
    for number in drawn_numbers:
        for board in boards:
            if board.bingo == False:
                board.cross_number(number)
                if board.check_bingo():
                    score = board.score(number)
                    if first_winner == -1:
                        first_winner = score
                    last_winner = score
    return first_winner, last_winner


first, last = play_bingo(drawn_numbers, boards)
print("Part 1: " + str(first))
print("Part 2: " + str(last))