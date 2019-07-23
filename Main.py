import pygame
import random
from pygame.locals import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    elif key == K_ESCAPE:
        pygame.quit()
        run = False

    else:
        return("")

   
    

    


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
    fuenteinfo = pygame.font.Font(None, 20)
    puntaje = fuente.render("Puntaje", 10, (255, 0, 255))
    informacion = fuenteinfo.render("Para finalizar presione esc ", 10 , (155,155,155))
    palabraUsuario = ""
    puntos = 0
    juego = True
   
    file=open('Extracto.txt','r')
    data=file.readlines()
    datos = []
    
    for renglon in data:
        for a in renglon.split(' '):
            datos.append(a)

    while juego:
        aa = random.choice(datos)    
        texto = fuente.render(aa, 10, (255, 255, 255))#texto ingresado por el usuario
        x = (random.randint(0,300))#posicion random a x
        y = 0
        vel = 5
        run = True

                
        while run:
            reloj = pygame.time.Clock()
            y += vel#Incrementa a "y" en cada vuelta
            pantalla.fill((0,0,0))#PantallaNegra
            

            reloj.tick(20)

            for e in pygame.event.get():
                if e.type == KEYDOWN:
                        letra = dameLetraApretada(e.key)
                        if type(letra) == str:
                            palabraUsuario += letra#concatena las letras presionadas 

            pantalla.blit(texto, (x,y)) #Muestra el texto en las posiciones x e y
            pantalla.blit(puntaje,(280,12)) #Palabra puntaje esquina superior
            pantalla.blit(informacion, (2,580)) #Informacion
            pantalla.blit(fuente.render(str(puntos), 10, (255,0,0)),(360,12))
            pygame.draw.line(pantalla, (40, 210, 250), (0, 500), (400, 500), 1) #Linea = Pantalla, color, start_pos, end_pos, Ancho
            pantalla.blit(fuente.render(palabraUsuario,10, (255,0,0)),(0,0)) #Muestra la palabra escrita por el usuario
            pygame.display.update() #Actualiza la pantalla
            
            if palabraUsuario == aa:
                puntos += 10
                vel = 0
                palabraUsuario = ""
                break

            if len(palabraUsuario) >= len(aa) :
                    palabraUsuario = ""
                    break

            if y >= 490:
                vel = 0
                puntos -=10
                if len(palabraUsuario) <= len(aa) :
                    palabraUsuario = ""
                    break
                break


if __name__ == '__main__':
  
    main()
    