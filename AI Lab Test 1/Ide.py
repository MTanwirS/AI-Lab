import random
import sys

def cboard():

    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return board


# Check for empty places on board

def possibility(board):
    p = []

    for i in range(len(board)):
        for j in range(len(board)):

            if board[i][j] == 0:
                p.append((i, j))
    return p


def randomplay(board, player):
    selection = possibility(board)
    location = random.choice(selection)
    print(location)
    board[location[0]][location[1]] = player
    return board


def row(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[x][y] != player:
                win = False
                continue

        if win == True:
            return win
    return win


def column(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue

        if win == True:
            return win
    return win


def diagonal(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x][x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x][y] != player:
                win = False
    return win


def evaluate(board):
    winner = 0

    for player in [1, 2]:
        if row(board, player) or column(board, player) or diagonal(board, player):

            winner = player
            return winner 
    winner = -1 
    
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 0:
                winner = 0

    return winner

def play():
    (board, winner, counter) = (cboard(), 0, 1)
    print (board)

    while winner == 0:
        for player in [1, 2]:
            board = randomplay(board, player)
            print (board)
            print("Player "+str(player))
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


def main():
    print ("Hello")
    winner = play()
    print("Winner is Player" + str(winner))
main()