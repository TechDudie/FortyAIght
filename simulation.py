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
