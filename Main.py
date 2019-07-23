import pygame
import random
from pygame.locals import *

def dameLetraApretada(key):
    dicc = {

    }

def main():
    pygame.init()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
    key = pygame.key.get_pressed()
    pantalla = pygame.display.set_mode((400,600),0,32)
    pygame.display.set_caption("Prueba")
    fuente = pygame.font.Font(None, 30)
    puntaje = fuente.render("Puntaje", 0, (255, 0, 0))
    lista = ["casa","hola","mano","jamon"]
    palabraUsuario = ""
    puntos = 0
   
    for palabra in lista:
        
        texto = fuente.render(palabra, 0, (255, 255, 255))
       

        puntos = 0
        
        x = (random.randint(0,420))
        y = 0
        vel = 2
        run = True
        
        
                
        while run:
            reloj = pygame.time.Clock()
            y += vel#Incrementa a "y" en cada vuelta
            pantalla.fill((0,0,0))#PantallaNegra
            

            reloj.tick(20)

            for e in pygame.event.get():
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra

            pantalla.blit(texto, (x,y))#Muestra el texto en las posiciones x e y
            pantalla.blit(puntaje,(300,12))#Palabra puntaje esquina superior
            pygame.draw.line(pantalla, (40, 210, 250), (0, 500), (400, 500), 1)#Linea = Pantalla, color, start_pos, end_pos, Ancho
            pantalla.blit(fuente.render(palabraUsuario,1, (255,0,0)),(0,0))
            pygame.display.update()#Actualiza la pantalla
            if palabraUsuario == palabra:
                puntos += 10
                vel = 0
                palabraUsuario = ""
                break

            if y == 500:
                vel = 0
                puntos -=10
                break

   
   



if __name__ == '__main__':
  
    #main()
    

    dicc = {
        92: "a",
        93: "b",
        94:"c",
        95: ""

    }

    dicc[92]