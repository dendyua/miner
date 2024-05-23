import random

class Minesweeper:
    def __init__(self, size, mines):
        self.size = size
        self.mines = mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.visible_board = [['x' for _ in range(size)] for _ in range(size)]
        self.mine_locations = set()
        self.generate_mines()
        self.update_counts()

    def generate_mines(self):
        while len(self.mine_locations) < self.mines:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            self.mine_locations.add((x, y))

    def update_counts(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for x, y in self.mine_locations:
            self.board[x][y] = 'M'
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] != 'M':
                    if self.board[nx][ny] == ' ':
                        self.board[nx][ny] = '1'
                    else:
                        self.board[nx][ny] = str(int(self.board[nx][ny]) + 1)

    def print_board(self, reveal=False):
        board_to_print = self.board if reveal else self.visible_board
        header = '   ' + '    '.join([str(i) for i in range(self.size)])
        separator = '   ' + ' '.join([' - ' for _ in range(self.size)])
        print(header)
        print(separator)
        for i, row in enumerate(board_to_print):
            print(f'{i} | ' + ' | '.join(row) + ' |')
        print(separator)

    def open_cell(self, x, y):
        if (x, y) in self.mine_locations:
            return False
        self.reveal_cell(x, y)
        return True

    def reveal_cell(self, x, y):
        if self.visible_board[x][y] == 'x':
            self.visible_board[x][y] = self.board[x][y]
            if self.board[x][y] == ' ':
                directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size and self.visible_board[nx][ny] == 'x':
                        self.reveal_cell(nx, ny)

    def play(self):
        while True:
            self.print_board()
            x, y = map(int, input("Enter the coordinates (x y): ").split())
            if not self.open_cell(x, y):
                print("Game Over! You hit a mine.")
                self.print_board(reveal=True)
                break
            if self.check_win():
                print("Congratulations! You won.")
                break

    def check_win(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] != 'M' and self.visible_board[x][y] == 'x':
                    return False
        return True

# Uncomment the line below to start the game.
game = Minesweeper(size=5, mines=5)
game.play()
