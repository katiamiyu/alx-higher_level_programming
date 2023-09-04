#!/usr/bin/python3
import sys


def solutionQueen(n):
    col = set()
    posdiag = set()
    negdiag = set()
    board = [["_"] * n for i in range(n)]

    def getposition(board):
        pos = []
        n = len(board)
        for x in range(n):
            for y in range(n):
                if board[x][y] == "Q":
                    pos.append([x, y])
        print(pos)

    def back(row):
        if row == n:
            getposition(board)
        for c in range(n):
            if c in col or row + c in posdiag or row - c in negdiag:
                continue
            board[row][c] = "Q"
            col.add(c)
            posdiag.add(row + c)
            negdiag.add(row - c)
            back(row + 1)
            board[row][c] = "_"
            col.remove(c)
            posdiag.remove(row + c)
            negdiag.remove(row - c)

    back(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutionQueen(n)
