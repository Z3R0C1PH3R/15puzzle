from random import randint
from copy import deepcopy
from time import sleep, perf_counter
class Board:
    def __init__ (self, n):
        self.n = n
        self.board = [[1+j+n*i for j in range(n)] for i in range(n)]
        self.board[n-1][n-1] = "--"
        self.x, self.y = n-1,n-1
        self.solved = deepcopy(self.board)
    
    def __str__(self):
        return "\n".join([" ".join([f"{j: >2}" for j in i]) for i in self.board])

    def move(self, direction:int, printing=True):
        """1-Right, 2-Left, 3-Down, 4-Up"""
        if direction==1 and self.x < self.n-1:
            self.board[self.y][self.x], self.board[self.y][self.x+1] = self.board[self.y][self.x+1], self.board[self.y][self.x]
            self.x += 1 

        elif direction==2  and self.x > 0:
            self.board[self.y][self.x], self.board[self.y][self.x-1] = self.board[self.y][self.x-1], self.board[self.y][self.x]
            self.x -= 1 

        elif direction==3  and self.y < self.n-1:
            self.board[self.y][self.x], self.board[self.y+1][self.x] = self.board[self.y+1][self.x], self.board[self.y][self.x]
            self.y += 1 

        elif direction==4 and self.y > 0:
            self.board[self.y][self.x], self.board[self.y-1][self.x] = self.board[self.y-1][self.x], self.board[self.y][self.x]
            self.y -= 1 
        if printing:
            pass
            print('\033[1A'*(self.n+1))
            print(b)
            sleep(0.0001)


    def shuffle(self, i:int=500):
        for _ in range(i):
            self.move(randint(1,4), False)
        for _ in range(self.x, self.n):
            self.move(1, False)
        for _ in range(self.y, self.n):
            self.move(3, False)

    def isSolved(self):
        return self.board == self.solved

def isOnSide(x,y,i,j,k,l):
    return (x in range(i,k) and (y == j or y == l)) or (y in range(j,l) and (x == i or x == k)) or (x == k and y == l)

def find(current, board):
    for j in range(b.n):
        for i in range(b.n):
            if board[j][i] == current:
                return i,j

def circle(i,j):
    for _ in range(i,b.n-1):
        b.move(2)
    for _ in range(j,b.n-1):
        b.move(4)
    for _ in range(i,b.n-1):
        b.move(1)
    for _ in range(j,b.n-1):
        b.move(3)

def shell():
    # moves = ["","d","a","s","w",]
    while 1:
        # b.move(moves.index(input()))
        b.move(int(input()))
        print(b)


if __name__ == "__main__":
    n = int(input())
    b = Board(n)
    print(b)
    print()
    b.shuffle(100*n**2)
    print(b)
    sleep(1)
    print("\n"*b.n)
    
    t = perf_counter()
    for edge in range(b.n):
        if edge == b.n-2:
            break
        for col in range(edge, b.n): #row
            i = edge*b.n+col+1

            cur = find(i, b.board)
            end = find(i, b.solved)
            if cur == end:
                continue
            while not isOnSide(cur[0], cur[1], col, edge, b.n-1, b.n-1):
                if min(cur) != edge:
                    circle(min(cur), min(cur))
                elif max(cur) != b.n-1:
                    circle(*cur)
                else:
                    circle(edge,edge+1)
                cur = find(i, b.board)
            if col != b.n-1:
                while cur != end:
                    circle(*end)
                    cur = find(i, b.board)
            else:
                while cur != (end[0], end[1]+1) and cur!=end:
                    circle(end[0]-1, end[1]+1)
                    cur = find(i, b.board)
                b.move(2)
                b.move(2)
                for _ in range(b.n-1-edge):
                    b.move(4)
                b.move(1)
                b.move(1)
                b.move(3)
                b.move(2)
                b.move(4)
                b.move(2)
                for _ in range(b.n-1-edge):
                    b.move(3)
                b.move(1)
                b.move(1)

        for row in range(edge+1, b.n): #col
            i = edge+1 + row*b.n
            cur = find(i, b.board)
            end = find(i, b.solved)
            if cur == end:
                continue
            while not isOnSide(cur[0], cur[1], edge, row, b.n-1, b.n-1):
                if min(cur) > edge:
                    circle(min(cur), min(cur))
                elif max(cur) != b.n-1:
                    circle(*cur)
                else:
                    circle(edge,edge+1)
                cur = find(i, b.board)
            if row != b.n-1:
                while cur != end:
                    circle(*end)
                    cur = find(i, b.board)
            else:
                while cur != (end[0]+1, end[1]) and cur!=end:
                    circle(end[0]+1, end[1]-  1)
                    cur = find(i, b.board)
                b.move(4)
                b.move(4)
                for _ in range(b.n-1-edge):
                    b.move(2)
                b.move(3)
                b.move(3)
                b.move(1)
                b.move(4)
                b.move(2)
                b.move(4)
                for _ in range(b.n-1-edge):
                    b.move(1)
                b.move(3)
                b.move(3)
    while b.board != b.solved:
        circle(b.n-2,b.n-2)
    print()
    print("Time: ", perf_counter() - t)
