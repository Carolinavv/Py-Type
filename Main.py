import pygame
from pygame.locals import *

def main():

    pantalla = pygame.display.set_mode((450,300),0,32)
    pygame.display.set_caption("Modulo de fuentes")

    reloj = pygame.time.Clock()

    fuente = pygame.font.Font(None, 30)
    texto1 = fuente.render("G", 0, (255, 255, 255))
    x = 50
    y = 50
    vel = 5


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= vel

        if keys[pygame.K_RIGHT]:
            x += vel

        if keys[pygame.K_UP]:
            y -= vel

        if keys[pygame.K_DOWN]:
            y += vel

        reloj.tick(20)
        pantalla.blit(texto1, (x,y))
        pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    main()