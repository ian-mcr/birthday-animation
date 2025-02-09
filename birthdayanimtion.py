import pygame
pygame.init()
WIDTH=600
HEIGHT=600
TITLE="Birthday Animtion"
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

bg1=pygame.image.load("party room.jpg")
bg2=pygame.image.load("party cake.jpg")
bg3=pygame.image.load("present.jpg")
run=True
while run:
    screen.blit(bg1,(0,0))
    font=pygame.font.SysFont("Arial",50)
    text=font.render("happy birthday",True,"red")
    screen.blit(text,(180,270))
    pygame.display.update()
    pygame.time.delay(1000)

    screen.blit(bg2,(0,0))
    font=pygame.font.SysFont("times new roman",50)
    text=font.render("make a wish",True,"red")
    screen.blit(text,(180,50))
    pygame.display.update()
    pygame.time.delay(1000)

    screen.blit(bg3,(0,0))
    font=pygame.font.SysFont("verdana",45)
    text=font.render("open the the presents",True,"orange")
    screen.blit(text,(60,50))
    pygame.display.update()
    pygame.time.delay(1000)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
