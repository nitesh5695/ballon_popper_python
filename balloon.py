import pygame
import sys
import random
pygame.init()
height=600
width=650
score =0
i=0
archer_x=10
archer_y=550
archer_size=50
target_x=random.randint(380,580)
target_y=500
target2_x=random.randint(380,500)
target2_y=target_y + 50
arrow_x=0
arrow_y = 0
target2_image=pygame.image.load("yballoon.png")
target2_image=pygame.transform.scale(target2_image,(40,100))
archer_image = pygame.image.load("archer.png")
archer_image = pygame.transform.scale(archer_image,(100,150))
arrow_image = pygame.image.load("arrow.png")
arrow_image = pygame.transform.scale(arrow_image,(50,30))
target_image = pygame.image.load("target.png")
target_image = pygame.transform.scale(target_image,(100,100))
screen = pygame.display.set_mode((width,height))
bgballon = pygame.image.load("bg_ballon.jpg")
bgballon = pygame.transform.scale(bgballon,(width,height))
gameover = False
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)
def screen_text(text,color,x,y):
    display_text = font.render(text,True,color)
    screen.blit(display_text,[x,y])
def update():
    pygame.display.update()
screen_text("balloon game",(255,0,255),100,110)

exit_game = False

while not exit_game :


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                archer_y -=20
            if event.key == pygame.K_RIGHT:
                arrow_x=archer_x + 40
                arrow_y=archer_y + 30
            if event.key == pygame.K_DOWN:
                archer_y +=20
    if abs(arrow_x - target_x)<20 and abs(arrow_y - target_y)<30:

        score +=10
        print("sccore=",score)
        target_x=random.randint(380,500)
        target_y=550
        arrow_x=archer_x
        arrow_y=archer_y
    if abs(arrow_x - target2_x)<30 and abs(arrow_y - target2_y)<40:
        target2_x=random.randint(380,500)
        target2_y=500
        arrow_x=archer_x
        arrow_y=archer_y



    screen.blit(bgballon,(0,0))

    screen.blit(target_image,(target_x,target_y))
    screen.blit(target2_image,(target2_x,target2_y))
    screen.blit(arrow_image,(arrow_x,arrow_y))
    print(target_y,arrow_x)
    arrow_x +=25
    target2_y -=15

    target_y -=10
    if target_y <10:
        target_y = 500
        target_x=random.randint(380,580)
    elif target2_y < 10:
        target2_x=random.randint(350,580)
        target2_y = 500

    screen.blit(archer_image,(archer_x,archer_y))
    screen_text("balloon game",(255,0,255),100,110)

    clock.tick(5)
    update()

