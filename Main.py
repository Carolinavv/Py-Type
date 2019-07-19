import sys, pygame
from pygame.locals import *

WIDTH = 600

HEIGHT = 600

def main():
    Pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Test")


if __name__ == '__main__':
    pygame.init()
    main()