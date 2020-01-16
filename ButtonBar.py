#!usr/bin/python3
import pygame

modes = {
    'START': 'Start',
    'END': 'End',
    'BLOCK': 'Block',
    'RUN': 'Run',
    'CLEAR': 'Clear'
}

colors = {
    "RED": (252, 3, 3),
    "BLUE": (3, 3, 252),
    "BLACK": (0, 0, 0),
    "GREY": (140, 140, 140),
    "WHITE": (255, 255, 255)
}


class ButtonBar:
    def __init__(self, screen, width, height):
        self.mode = modes['START']
        self.width = width
        self.height = height
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 25)
        
        self.startButton = None
        self.endButton = None
        self.blockButton = None
        self.runButton = None
        self.clearButton = None

    def draw(self):
        self.startButton = pygame.draw.rect(self.screen, colors['RED'], (40, 10, 80, 40))
        self.screen.blit(self.font.render('Start', True, colors['BLACK'], None), (60, 20))

        self.endButton = pygame.draw.rect(self.screen, colors['BLUE'], (140, 10, 80, 40))
        self.screen.blit(self.font.render('End', True, colors['BLACK'], None), (165, 20))

        self.blockButton = pygame.draw.rect(self.screen, colors['GREY'], (240, 10, 80, 40))
        self.screen.blit(self.font.render('Block', True, colors['BLACK'], None), (260, 20))

        self.runButton = pygame.draw.rect(self.screen, colors['BLACK'], (340, 10, 80, 40))
        self.screen.blit(self.font.render('Run', True, colors['WHITE'], None), (365, 20))

        self.clearButton = pygame.draw.rect(self.screen, colors['BLACK'], (440, 10, 80, 40))
        self.screen.blit(self.font.render('Clear', True, colors['WHITE'], None), (460, 20))

        self.screen.blit(self.font.render('Mode chosen: {}'.format(self.mode), True, colors['BLACK'], None), (565, 20))

        pygame.display.update()

    def changeMode(self, pos):
        if self.startButton.collidepoint(pos[0], pos[1]):
            self.mode = 'Start'
        elif self.endButton.collidepoint(pos[0], pos[1]):
            self.mode = 'End'
        elif self.blockButton.collidepoint(pos[0], pos[1]):
            self.mode = 'Block'
        elif self.runButton.collidepoint(pos[0], pos[1]):
            self.mode = 'Run'
        elif self.clearButton.collidepoint(pos[0], pos[1]):
            self.mode = 'Clear'