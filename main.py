import pygame, sys
import random #Para utilizar el random en el avance de los corredores.

#Nos vamos a crear un clase corredor, que dibuje un corredor y lo mueva por la pantalla.
class Runner():
    __custome = ('turtle', 'fish', 'prawn', 'moray', 'octopus') #Creamos tupla con los 5 tipos de personajes que podemos tener.
    
    def __init__(self, x=0, y=0):

        ixCustome =random.randint(0,4) #Los muevo al azar.

        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome])) #Cargo la imagen al azar.
        self.position = [x, y] #Es una lista, porque tiene que ser mutable, van a cambiar.
        self.name = custome
    
    def avanzar(self):
        self.position[0] += random.randint(1, 6)
    

class Game():
    runners = [] #Es una lista de corredores, en un array.
    __posY = (160, 200, 240, 280) #Posición de salida de los corredores.
    __names = ('Speedy', 'Lucera', 'Alonso', 'Torcuata')
    __startLine = 5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480)) #La hacemos privada.
        self.background = pygame.image.load("images/background.png") #En el fondo de la pantalla cargamos una imagen.
        pygame.displany.set_caption("Carrera de bichos")
        
        
        for i in range (4):
            theRunner = Runner(self.__startLine, self.__posY[i])     
            theRunner.name = self.__names[i]
            self.runners.append(theRunner) #Añade a mi lista de corredores, mi primer correr, que lo he instanciado en la fila 25.
    
    def close(self):       
        pygame.quit()
        sys.exit()
    
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get(): #Para cada evento de Pygame
                if event.type == pygame.QUIT:
                    gameOver = True
            
            
            
            for activeRunner in self.runners: #runner es una variable que sólo la voy a utilizar en el contexto de competir. Self es para las variables que están en la clase, siempre.
                activeRunner.avanzar()
                if activeRunner.position[0] >=self.__finishLine:
                    print("{} ha ganado".format(activeRunner.name))
                    gameOver = True
            
            self.__screen.blit(self.__background, (0,0))
             #Me coges la imagen del corredor 0 y la posición del corredor 0.
            
            for runner in self.runners:
               self.__screen.blit(runner.custome, runner[0].position)
            
            pygame.display.flip() #Con esto refresca.
            
        while True: #Cuando se produce un ganador, para que me siga refrescando. Va limpiando los eventos y no se queda tostada.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
        
        
if __name__== '__main__':
    game = Game()
    pygame.font.init()
    game.competir()