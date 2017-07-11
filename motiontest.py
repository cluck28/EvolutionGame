#A simple program to test the implementation of the graphics thus far
#and reproduction

import Movement
import Movement_AI
import Reproduce
import random
import pygame

#Initialize pygame
pygame.init()
pygame.key.set_repeat(100,100)

#Initialize the player
chris=Movement.Movement()
print chris.get_gene_movement()

#Initialize the AI
AI_array=[]
for i in range(25):
    x=random.randint(100,540)
    y=random.randint(100,300)
    AI=Movement_AI.Movement_AI([],x,y)
    AI_array.append(AI)

#Enable reproduction
empty=Reproduce.Reproduce()

#Create a font
font=pygame.font.Font(None, 17)

#Window dimensions
width=640
height=400

#Graphics
screen=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
running=True
chris.draw(screen)
for AI in AI_array:
    AI.draw_AI(screen)
baby_timer=0

while running:
    #Crash at borders
    if chris.x<=0 or chris.x>=width or chris.y<=0 or chris.y>=height:
        print 'Crash'
        running=False
    for AI in AI_array:
        if AI.x<=0 or AI.x>=width or AI.y<=0 or AI.y>=height:
            print 'Crash'
            running=False

    #User reproduce with AI
    for AI in AI_array:
        if baby_timer==100:
            if chris.x==AI.x and chris.y==AI.y:
                if chris.get_gene_sex()!=AI.get_gene_sex():
                    baby=empty.repro(chris,AI)
                    AI_array.append(baby)
                    baby_timer=0
                    chris.rec_health(1.5)

    #AI reproduce with AI
    for AI in AI_array:
        for AI1 in AI_array:
            if AI1 != AI:
                if baby_timer==100:
                    if AI.x==AI1.x and AI.y==AI1.y:
                        AIbaby=empty.repro(AI,AI1)
                        AI_array.append(AIbaby)
                        baby_timer=0

    #Movement
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            chris.key_event(event)
            chris.move()
    screen.fill((0,0,0))
    for AI in AI_array:
        AI.rand_event()
        AI.move_AI()
        AI.draw_AI(screen)
    chris.draw(screen)
    text=font.render(str(chris.health),True,(255,255,255),(0,0,0))
    screen.blit(text,(0,0))
    #Timer between births
    if baby_timer!=100:
        baby_timer+=1
    else:
        text_baby=font.render('Baby making time',True,(255,255,255),(0,0,0))
        screen.blit(text_baby,(500,0))
        baby_timer=baby_timer
    #Update screen
    pygame.display.flip()
    clock.tick(100)
