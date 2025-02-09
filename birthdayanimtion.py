import pygame
pygame.init()
WIDTH=600
HEIGHT=600
TITLE="Birthday Animtion"
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

bg1=pygame.image.load("party room.jpg")

run=True
while run:
    screen.blit(bg1,(0,0))
    font=pygame.font.SysFont("Arial",50)
    text=font.render("happy birthday",True,"red")
    screen.blit(text,(300,300))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
