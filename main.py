from random import randint
from copy import deepcopy
class Board:
    def __init__ (self, n):
        self.side = n
        self.board = [[1+j+n*i for j in range(n)] for i in range(n)]
        self.board[n-1][n-1] = "--"
        self.x, self.y = 4,4
        self.solved = deepcopy(self.board)
        print(self.board)
    
    def __str__(self):
        return "\n".join([" ".join([f"{j: >2}" for j in i]) for i in self.board])

    def move(self, direction:int):
        """1-Left, 2-Right, 3-Down, 4-Up"""
        if direction==1 and self.x < self.side-1:
            self.board[self.y][self.x], self.board[self.y][self.x+1] = self.board[self.y][self.x+1], self.board[self.y][self.x]
            self.x += 1 

        elif direction==2  and self.x > 0:
            self.board[self.y][self.x], self.board[self.y][self.x-1] = self.board[self.y][self.x-1], self.board[self.y][self.x]
            self.x -= 1 

        elif direction==3  and self.y < self.side-1:
            self.board[self.y][self.x], self.board[self.y+1][self.x] = self.board[self.y+1][self.x], self.board[self.y][self.x]
            self.y += 1 

        elif direction==4 and self.y > 0:
            self.board[self.y][self.x], self.board[self.y-1][self.x] = self.board[self.y-1][self.x], self.board[self.y][self.x]
            self.y -= 1 


    def shuffle(self, i:int=100):
        for _ in range(i):
            self.move(randint(1,4))
        for _ in range(self.x, self.side):
            self.move(1)
        for _ in range(self.y, self.side):
            self.move(3)

    def isSolved(self):
        return self.board == self.solved

if __name__ == "__main__":
    b = Board(5)
    print(b)
    print(b.isSolved())
    b.shuffle(5)
    print(b)
    print(b.isSolved())
    moves = ["","d","a","s","w",]
    while 1:
        b.move(moves.index(input()))
        # print('\033[3A'*b.side)
        print(b)
        if b.isSolved():
            print("WOOHOO")
            break
