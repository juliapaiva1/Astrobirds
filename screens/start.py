import pygame
from screens.game import Game

class Start:
    ''' Classe que renderiza a tela inicial. Apenas recebe eventos para redirecionar o jogo ou para instruções.'''

    def __init__(self, status, screen):
        self.background = pygame.image.load('assets/startScreen.png')
        self.status = status
        self.screen = screen
        self.playBtn = pygame.Rect((345, 450), (505,60))
        self.instructionBtn = pygame.Rect((435, 510), (330,60))

    def run(self, window):
        '''Faz a chamada de todas as funcoes necessarias para renderizar a essa tela.'''
        self.draw()
        self.getEvents(window)

    def getEvents(self,window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status["running"] = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.setupGame(window)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if self.playBtn.collidepoint(mouse):
                    self.setupGame(window)
                if self.instructionBtn.collidepoint(mouse):
                    self.status["current"] = "instructions"
    
    def setupGame(self, window):
        self.status["gameStart"] = pygame.time.get_ticks()
        window["game"] = Game(self.status, self.screen) 
        self.status["current"] = "game"
    
    def draw(self):
        self.screen.blit(self.background, (0,0))

