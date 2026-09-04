import pygame
pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Image window")
screen.fill("pink")

bg_surf = pygame.transform.scale(pygame.image.load("image1.png").convert(),(400,400))

done =  False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bg_surf,(0,0))

    pygame.display.update()
