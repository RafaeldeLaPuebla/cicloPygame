#Vamos a controlar las teclas.

import pygame, sys
from pygame.locals import*
import random

class Runner():
    __custome = ('turtle', 'fish', 'prawn', 'moray', 'octopus') #Creamos tupla con los 5 tipos de personajes que podemos tener.
    
    def __init__(self, x=0, y=0):

        ixCustome =random.randint(0,4) #Los muevo al azar.

        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome])) #Cargo la imagen al azar.
        self.position = [x, y] #Es una lista, porque tiene que ser mutable, van a cambiar.
        self.name = ""
        
class Game():
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480)) #La hacemos privada.
        self.background = pygame.image.load("images/background.png") #En el fondo de la pantalla cargamos una imagen.
        pygame.displany.set_caption("Carrera de bichos")
        
        self.runner = Runner(320, 240)
        
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get(): #Para cada evento de Pygame
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.runner.position[1] += 5
                        
                        #mover hacia arriba runner
                    elif event.key == K_DOWN:
                        self.runner.position[1] -= 5
                    
                        #mover hacia abajo runner
                    elif event.key == K_LEFT:
                        self.runner.position[0] -= 5
                        #mover hacia la izquierda
                    elif event.key == K_RIGHT:
                        self.runner.position[0] += 5
                        #mover hacia la derecha
                    else:
                        pass
        
            self.__screen.blit(self.__background, (0,0))
            self.__screen.blit(self.runner.custome, self.runner.position) #Esto me lo carga.
            
            pygame.display.flip() #Esto me lo refresca.
            
if __name == '__main__':
    game = Game
    pygame.font.init()
    game.start()