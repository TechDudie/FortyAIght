# With a big tip of the hat to Ali for rewriting and optimizing my crappy code!

import numpy as np

class Game2048:
    def __init__(self):
        self.board = np.zeros((4, 4), dtype=np.uint16)
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()

    def slide(self, row: np.ndarray, right: bool = False) -> np.ndarray:
        if right:
            row = row[::-1]
        merged = False
        for i in range(len(row)-1):
            if row[i] == row[i+1]:
                self.score += row[i] * 2
                row[i] <<= 1
                row[i+1] = 0
                merged = True
        row = row[row != 0]
        row = np.concatenate((row, np.zeros(len(self.board) - len(row), dtype=np.uint16)))
        if right:
            row = row[::-1]
        return row, merged

    def add_new_tile(self):
        empty_cells = np.where(self.board == 0)
        if len(empty_cells[0]) == 0:
            return False
        i = np.random.randint(len(empty_cells[0]))
        value = np.random.choice([2, 4], p=[0.75, 0.25])
        self.board[empty_cells[0][i], empty_cells[1][i]] = value
        return True

    def play_move(self, move: int):
        prev_board = self.board.copy()
        if move == 0:
            self.board = self.board.T
            for n, i in enumerate(self.board):
                self.board[n], merged = self.slide(i)
            self.board = self.board.T
        elif move == 1:
            for n, i in enumerate(self.board):
                self.board[n], merged = self.slide(i, True)
        elif move == 2:
            self.board = self.board.T
            for n, i in enumerate(self.board):
                self.board[n], merged = self.slide(i, True)
            self.board = self.board.T
        elif move == 3:
            for n, i in enumerate(self.board):
                self.board[n], merged = self.slide(i)
        else:
            return False
        if not np.array_equal(self.board, prev_board):
            if not self.add_new_tile():
                print(f"Game over. Score: {self.score}")
        return True

    def play_game(self):
        while True:
            print(self.board)
            move = int(input(f"Score: {self.score} Your move (0: up, 1: right, 2: down, 3: left): "))
            if not self.play_move(move):
                print("Invalid move. Please try again.")

game = Game2048()
game.play_game()

'''
import random

board = [
    [2, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 2]
]
global score
score = 0

def shift(start: list, index: int) -> list:
    start.pop(index)
    start.append(0)
    return start

def slide(row: list, right=False) -> list:
    global score
    if right: row = row[::-1]
    row = [i for i in row if i != 0]
    for i in range(0, 4 - len(row)): row.append(0)
    for i in range(0,3):
        repeat = True
        j = 0 
        while repeat:
            if row[i] == row[i + 1]:
                row = shift(row, i)
                row[i] *= 2
                score += row[i]
                j += 1
                if j > 3: repeat = False
                continue
            repeat = False
    if right: row = row[::-1]
    return row

while True:
    print(board)
    move = int(input(f"Score: {score} Your move (0: up, 1: right, 2: down, 3: left): "))
    prev = board
    if move == 0:
        copy = list(zip(*board[::-1]))
        for n, i in enumerate(copy): copy[n] = slide(copy[n], True)
        board = list(zip(*copy))[::-1]
    if move == 1:
        for n, i in enumerate(board): board[n] = slide(board[n], True)
    if move == 2:
        copy = list(zip(*board[::-1])) 
        for n, i in enumerate(copy): copy[n] = slide(copy[n])
        board = list(zip(*copy))[::-1]
    if move == 3:
        for n, i in enumerate(board): board[n] = slide(board[n])
    for n, i in enumerate(board): board[n] = list(board[n])
    if board != prev:
        new_tile = False
        while not new_tile:
            new_x = random.randint(0, 3)
            new_y = random.randint(0, 3)
            if board[new_y][new_x] == 0:
                board[new_y][new_x] = 2 if random.random() < 0.75 else 4
                new_tile = True
'''
