import pygame
from pygame.locals import *

def main():
    pygame.init()

    pantalla = pygame.display.set_mode((400,600),0,32)
    pygame.display.set_caption("Prueba")


    fuente = pygame.font.Font(None, 30)
    texto1 = fuente.render("G", 0, (255, 255, 255))
    x = 50
    y = 50
    vel = 5
    run = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            
    while run:
        reloj = pygame.time.Clock()
        y += vel#Incrementa a "y" en cada vuelta
        pantalla.fill((0,0,0))#PantallaNegra

        reloj.tick(20)

        pantalla.blit(texto1, (x,y))#Muestra el texto en las posiciones x e y

        pygame.draw.line(pantalla, (40, 210, 250), (0, 500), (400, 500), 1)#Linea = Pantalla, color, start_pos, end_pos, Ancho
        pygame.display.update()#Actualiza la pantalla
        if y == 500:
            vel = 0

    pygame.quit()



if __name__ == '__main__':
  
    main()