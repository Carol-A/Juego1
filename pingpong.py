import pygame

def main():
    pygame.init() 
    size = 800,600 
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Mi primer juego")

    width, height = 800,600
    speed = [2, 2]
    white = 255, 255, 255
    barrasize = 20, 150
    ballsize = 50,50
    mitad_x = width/2-ballsize[0]/2
    mitad_y = height/2-ballsize[1]/2
    score = [0, 0]

    fuente = pygame.font.Font(None, 50)
    marcador = fuente.render("Score", True, (0, 0, 0))
    puntaje1 = fuente.render(str(score[0]), True, (0,0,0))
    puntaje2 = fuente.render(str(score[1]), True, (0,0,0))

    ball = pygame.image.load('ball.png')
    ball = pygame.transform.scale(ball, ballsize)
    ballrect = ball.get_rect();
    ballrect.move_ip(mitad_x, mitad_y)

 
    barra = pygame.image.load('bar.jpg')
    barra = pygame.transform.scale(barra, (barrasize))
    barrarect = barra.get_rect()

   
    barrarect.move_ip(50,height/2-barrasize[1]/2)
        
    barra2 = pygame.image.load('bar2.jpg')
    barra2 = pygame.transform.scale(barra2, (barrasize))
    barrarect2 = barra2.get_rect()

    #se ubica la barra a la mita de la ventana
    barrarect2.move_ip(width-50,height/2-barrasize[1]/2)

    run = True
    while run:
        pygame.time.delay(5) #delay que contralará la velocidad            
        
        for event in pygame.event.get(): #se captura el evento que se produce
            if event.type == pygame.QUIT:
                run = False

        #se detecata si se ha pulsado alguna tecla
        keys = pygame.key.get_pressed()


        if keys[pygame.K_w] and barrarect.top > 0:
            barrarect = barrarect.move(0, -2)

        if keys[pygame.K_s] and barrarect.bottom < height:
            barrarect = barrarect.move(0, 2)

        if keys[pygame.K_UP] and barrarect2.top > 0:
            barrarect2 = barrarect2.move(0, -2)

        if keys[pygame.K_DOWN] and barrarect2.bottom < height:
            barrarect2 = barrarect2.move(0, 2)

        #se detemina si hay colisiones 
        if barrarect.colliderect(ballrect):
            speed[0] = -speed[0]
        if barrarect2.colliderect(ballrect):
            speed[0] = -speed[0]

        ballrect = ballrect.move(speed) #se mueve el objeto
        #se determinan los límites del objeto
        if ballrect.left < 0 or ballrect.right > width:
            multiplicador = 1
            if(ballrect[1]>mitad_y):
                multiplicador = -1

            if ballrect.left < 0:
                score[0] += 1
                puntaje2 = fuente.render(str(score[0]), True, (0,0,0))
            if ballrect.right > width:
                score[1] = score[1]+1
                puntaje1 = fuente.render(str(score[1]), True, (0,0,0))
            
            ballrect = ballrect.move(-1*ballrect[0]+mitad_x, mitad_y+multiplicador*ballrect[1])
            pygame.time.delay(800)

        

        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]


        #se borra la pantalla anterior con el fondo blanco
        screen.fill(white)
        screen.blit(marcador, (width/2-50, 50))
        screen.blit(puntaje1, (width/2-100, 50))
        screen.blit(puntaje2, (width/2+100, 50))
        screen.blit(ball, ballrect)
        screen.blit(barra,barrarect)
        screen.blit(barra2,barrarect2)
        pygame.display.flip()
    pygame.quit() #se termina el juego

if __name__ == "__main__":
    main()
