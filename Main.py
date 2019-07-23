import pygame
from pygame.locals import *

def main():

    pantalla = pygame.display.set_mode((400,600),0,32)
    pygame.display.set_caption("Modulo de fuentes")


    fuente = pygame.font.Font(None, 30)
    texto1 = fuente.render("G", 0, (255, 255, 255))
    x = 50
    y = 50
    vel = 5




    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        reloj = pygame.time.Clock()
       
        y += vel
        pantalla.fill((0,0,0))

        reloj.tick(20)

        pantalla.blit(texto1, (x,y))

        pygame.draw.line(pantalla, (40, 210, 250), (0, 500), (400, 500), 1)
        pygame.display.update()



if __name__ == '__main__':
    pygame.init()
    main()