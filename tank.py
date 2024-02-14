import pygame, sys, random, math
tank_size=(50,50)
img=pygame.image.load("tank_1.png")
img2=pygame.image.load("tank_2.png")
tank_1=pygame.transform.scale(img,tank_size)
tank_2=pygame.transform.scale(img2,tank_size)

class Tank(pygame.sprite.Sprite):
    def __init__(self,x,y,tank_img):
        super(Tank, self).__init__()
        self.image= tank_img
        self.image.convert_alpha()
        self.rect = self.image.get_rect(center = (x,y))
        self.ch_angle = 0
    
    def move(self,deltax,deltay):
        if self.rect.left<=0 or self.rect.right>1200:
            deltax *=-4
        if self.rect.top<=0 or self.rect.bottom>600:
            deltay*=-4 
        self.rect.centerx+=deltax
        self.rect.centery+=deltay
    def rot(self,tank_img):
        self.ch_angle
        self.ch_angle += 90
        self.image = pygame.transform.rotate(tank_img, self.ch_angle)
        self.rect = self.image.get_rect(center=self.rect.center)
    


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,color,velocity):
        super(Bullet,self).__init__()
        self.image=pygame.surface((10,10),pygame.SRCALPHA,32)
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x,y))
        self.deltax = velocity
    def move(self):
        p_list = pygame.sprite.spritecollide(self,tanks,False)
        if p_list:
            self.deltax *= -1
            self.image.fill(p_list[0].color)

            self.rect.centerx += self.deltax*2
            self.rect.centery += self.deltay*2
    


class Wall(pygame.sprite.Sprite):
    def __init__ (self,x,y,l,w):
        super(Wall, self).__init__()
        self.image= pygame.Surface((l,w),pygame.SRCALPHA,32)
        self.image.convert_alpha()
        self.image.fill("white")
        self.rect = self.image.get_rect(center = (x,y))



pygame.init()

screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("tanks")
clock = pygame.time.Clock()


p1=Tank(1000,300,tank_1)
p2=Tank(200,300,tank_2)
tanks=pygame.sprite.Group()
tanks.add(p1)
tanks.add(p2)

wall_1=Wall(600,150,200,20)
wall_2=Wall(600,450,200,20)
wall_3=Wall(600,300,20,200)
walls=pygame.sprite.Group()
walls.add(wall_1)
walls.add(wall_2)
walls.add(wall_3)




# Set up the screen dimensions



running= True

while running:
    # Event handling

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((50,0,0))
    keys = pygame.key.get_pressed()
    key = pygame.key.set_repeat(2)

    if keys[pygame.K_j]:
        p1.move(-2,0)
        p_list = pygame.sprite.spritecollide(p1,walls,False)
        if p_list:
            p1.move(2,0)
    if keys[pygame.K_l]:
        p1.move(2,0)
        p_list = pygame.sprite.spritecollide(p1,walls,False)
        if p_list:
            p1.move(-2,0)
    if keys[pygame.K_i]:
        p1.move(0,-2)
        p_list = pygame.sprite.spritecollide(p1,walls,False)
        if p_list:
            p1.move(0,2)
    if keys[pygame.K_k]:
        p1.move(0,2)
        p_list = pygame.sprite.spritecollide(p1,walls,False)
        if p_list:
            p1.move(0,-2)
    if key[pygame.K_u]:
          p1.rot(tank_1)

    # if keys[pygame.K_n]:

        


    if keys[pygame.K_a]:
        p2.move(-2,0)
        p_list = pygame.sprite.spritecollide(p2,walls,False)
        if p_list:
            p2.move(2,0)
    if keys[pygame.K_d]:
        p2.move(2,0)
        p_list = pygame.sprite.spritecollide(p2,walls,False)
        if p_list:
            p2.move(-2,0)
    if keys[pygame.K_w]:
        p2.move(0,-2)
        p_list = pygame.sprite.spritecollide(p2,walls,False)
        if p_list:
            p2.move(0,2)
    if keys[pygame.K_s]:
        p2.move(0,2)
        p_list = pygame.sprite.spritecollide(p2,walls,False)
        if p_list:
            p2.move(0,-2)
    
    # if keys[pygame.k_e]:
    #     shoot
    tanks.draw(screen)
    walls.draw(screen)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()