import pygame

pygame.init()
SWIDHT = 500
SHEIGHT = 400
screen = pygame.display.set_mode((SWIDHT,SHEIGHT))
mspeed = 1
background_image = pygame.transform.scale(pygame.image.load("backgroundspace.png"),(SWIDHT,SHEIGHT))
font = pygame.font.SysFont("Times New Roman", 72)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,path,h,w):
        super().__init__()
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
    def move(self,xchange,ychange):
        self.rect.x = max(min(self.rect.x +xchange,SWIDHT - self.rect.w),0)
        self.rect.y = max(min(self.rect.y +ychange,SHEIGHT - self.rect.h),0)
clock = pygame.time.Clock()

path = "dog.jpg " 
all_sprites = pygame.sprite.Group()
sprite1 =Sprite(path,20,20)
sprite1.rect.x = 200
sprite1.rect.y = 200
all_sprites.add(sprite1)

path = "dog food bowl.jpg"
sprite2 =Sprite(path,20,20)         
sprite2.rect.x = 100
sprite2.rect.y = 50
all_sprites.add(sprite2)

while True:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    keys = pygame.key.get_pressed()

    xchange = (keys[pygame.K_RIGHT]- keys[pygame.K_LEFT]) *mspeed
    ychange = (keys[pygame.K_DOWN]- keys[pygame.K_UP]) *mspeed
    sprite1.move(xchange,ychange)
    screen.blit(background_image,(0,0))
    all_sprites.draw(screen)
    if sprite1.rect.colliderect(sprite2.rect):

        win_text = font.render("You win!!!", True,pygame.Color('purple'))
        screen.blit(win_text,(200,200))
        all_sprites.remove(sprite2)

    pygame.display.flip()
    clock.tick(90)