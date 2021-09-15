import pygame, random

ANCHO = 900
ALTO = 585
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

def texto(texto, tam=20, color=(0, 0, 0)):
    fuente = pygame.font.Font(None, tam)
    return fuente.render(texto, True, color)


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load('C:/Users/arrie/OneDrive/Documentos/imgJUEGO/Laser.png').convert()
        self.image1.set_colorkey(negro)
        self.image = pygame.transform.scale(self.image1, (20,30))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 5


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('C:/Users/arrie/OneDrive/Documentos/imgJUEGO/Nave1.png').convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x -= 2
        
        if self.rect.x < 0:
            self.rect.x = 900 
   


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('C:/Users/arrie/OneDrive/Documentos/imgJUEGO/nave2.png').convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
    
    def  update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = 500

    
negro = 0,0,0
blanco = 255,255,255

def main():
    pygame.init()
    screen = pygame.display.set_mode([900,600])

    clock = pygame.time.Clock()
    run = True
    score = 0

    fondo1 = pygame.image.load('C:/Users/arrie/OneDrive/Documentos/imgJUEGO/fondo.jpg')
    fondo = pygame.transform.scale(fondo1, (900,850))
    fondorect = fondo.get_rect();

    all_sprite_list = pygame.sprite.Group()
    meteor_list = pygame.sprite.Group()
    laser_list = pygame.sprite.Group()

    for i in range(20):
        meteor = Meteor()
        meteor.rect.x = random.randrange(800)
        meteor.rect.y = random.randrange(400)

        meteor_list.add(meteor)
        all_sprite_list.add(meteor)

    player = Player()
    all_sprite_list.add(player)

    while run:
        for event in pygame.event.get(): #se captura el evento que se produce
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                laser = Laser()
                laser.rect.x = player.rect.x + 90
                laser.rect.y = player.rect.y - 20

                all_sprite_list.add(laser)
                laser_list.add(laser)
    
        all_sprite_list.update() #actualiza el movimiento de los sprite
        #se definen las colisiones
        for laser in laser_list:
            meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True) # el true es para que desaparezcan
            #para eliminar el laser en las colisiones
            for meteor in meteor_hit_list:
                all_sprite_list.remove(laser)
                laser_list.remove(laser)
                score += 1
                print(score)
            if laser.rect.y < 0:
                all_sprite_list.remove(laser)
                laser_list.remove(laser)
        
        #screen.fill(blanco)
        screen.blit(fondo, fondorect)
        all_sprite_list.draw(screen) #se pintan todos los sprites
        screen.blit(texto("Score:", 60, BLANCO), (ANCHO / 3, 10))
        screen.blit(texto(str(score), 60, BLANCO), (ANCHO / 2, 10))


        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()



if __name__ == "__main__":
    main()