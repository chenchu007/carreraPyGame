import pygame
import sys
import random

class Runner():
    __custom = ('turtle','fish','moray','octopus')
    def __init__(self, x=0, y=0, custom='turtle'):
        try:
            self.custom = pygame.image.load("images/{}.png".format(custom))
            self.name = custom
        except:
            xCustom = self.__custom[(random.randint(0,3))]
            self.custom = pygame.image.load("images/{}.png".format(xCustom))
            self.name = xCustom
        self.position = [x, y]

    def avanza(self):
        self.position[0] += random.randint(1, 6)

class Game():
    runners = []
    __posY = (160, 200, 240, 280)
    __names = ('Speedy','Lucera','Alonso','Torcuata')
    __startLine = -30
    __finishLine  = 600

    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption('Carrera de Tortugas')
        self.background = pygame.image.load('images/background.png')

        for i in range(4):
            theRunner = Runner(self.__startLine,self.__posY[i],'')
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)


    def competir(self):
        endGame = False
        while not endGame:
            # Comprobación de los eventos en pyhame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Renderizado/Refresco de la pantalla
            self.__screen.blit(self.background, (0,0))
            for runner in self.runners:
                runner.avanza()  ## Avanza el corredor
                self.__screen.blit(runner.custom, runner.position)  ## Pintar el corredor
                if runner.position[0] >= self.__finishLine:  ## Comprueba si ha ganado el corredor
                    print("{} ha ganado".format(runner.name))
                    endGame = True

            pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()