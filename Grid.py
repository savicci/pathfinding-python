#!usr/bin/python3
import pygame

colors = {
    "RED": (252, 3, 3),
    "BLUE": (3, 3, 252),
    "BLACK": (0, 0, 0),
    "GREY": (140, 140, 140),
    "WHITE": (255, 255, 255),
    "GREEN": (97, 235, 52),
    "LIGHTGREEN": (66, 245, 191),
}

class Grid:
    def __init__(self, screen, x, y, rows, columns, boxSize):
        self.screen = screen
        self.boxSize = boxSize
        self.x = x
        self.y = y
        self.rows = rows
        self.columns = columns

        self.grid = self.createGrid()

    def createGrid(self):
        return [[0 for i in range(self.columns)] for i in range(self.rows)]

    def draw(self, start, end):
        for iidx, row in enumerate(self.grid):
            for jidx, column in enumerate(row):
                if (iidx, jidx) == start:
                    self.drawRect(colors['RED'], iidx, jidx)
                elif (iidx, jidx) == end:
                    self.drawRect(colors['BLUE'], iidx, jidx)
                elif self.grid[iidx][jidx] == 0:
                    pygame.draw.rect(self.screen, colors['BLACK'], (self.x + jidx*self.boxSize, self.y + iidx*self.boxSize, self.boxSize, self.boxSize), 1)
                elif self.grid[iidx][jidx] == 1:
                    self.drawRect(colors['GREY'], iidx, jidx)
                elif self.grid[iidx][jidx] == 2:
                    self.drawRect(colors['GREEN'], iidx, jidx)
                elif self.grid[iidx][jidx] == 3:
                    self.drawRect(colors['LIGHTGREEN'], iidx, jidx)


    def drawRect(self, color, iidx, jidx):
         pygame.draw.rect(self.screen, color, (self.x + jidx*self.boxSize, self.y + iidx*self.boxSize, self.boxSize, self.boxSize))


    def updateBlock(self, pos, mode, start, end):
        row = 0
        col = 0

        while True:
            if (pos[0] >= self.x + col*self.boxSize + self.boxSize):
                col +=1
            else: break

        while True:
            if(pos[1] >= self.y + row*self.boxSize + self.boxSize):
                row +=1
            else: break
        
        if mode == 'Start':
            start = (row, col)
        elif mode == 'End':
            end = (row, col)
        elif mode == 'Block':
            if self.grid[row][col] == 1:
                self.grid[row][col] = 0
            else: 
                self.grid[row][col] = 1
        else:
            pass

        return (start, end)
    
    def clear(self):
        self.grid = self.createGrid()