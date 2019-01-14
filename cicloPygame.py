#Ciclo básico de pygame.

import pygame, sys #sys es la librería del sistema

width = 648
height = 480

screen = pygame.display.set_mode((width, height)) #Creamos una ventana del juego y la asignamos a la variable screen.
screen.fill(246, 147, 48) #Le aplicamos el color roja a la pantalla.
pygame.display.set_caption("Ciclo básico de Pygame")

pygame.font.init() #Iniciamos Pygame. Empieza a recoger eventos.

gameOver = False
while not gameOver
    for event in pygame.event.get(): #Para cada evento de Pygame
        if event.type == pygqme.QUIT:
            gameOver = True
    
    pygame.display.flip() #Este método refresca la imagen.
            
pygame.quit()

