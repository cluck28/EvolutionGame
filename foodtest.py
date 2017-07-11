#Test to see how the function find_food works

import find_food
import go_to_food
import pygame
import Movement_AI
import random
from numpy import *

#Initialize pygame
pygame.init()
#Create a font
font=pygame.font.Font(None, 17)

#Initialize the AI at random location
a=random.randint(100,540)
b=random.randint(100,300)
AI=Movement_AI.Movement_AI([],a,b)

#Window dimensions
width=640
height=400

#Graphics
screen=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
running=True

screen.fill((0,0,0))
AI.draw_AI(screen)

#Need an array
a1=random.randint(100,540)
b1=random.randint(100,300)
a2=random.randint(100,540)
b2=random.randint(100,300)
a3=random.randint(100,540)
b3=random.randint(100,300)
food_array = matrix([[a1,b1],[a2,b2],[a3,b3]])
screen.set_at((food_array[0,0],food_array[0,1]), (255,255,255))
screen.set_at((food_array[1,0],food_array[1,1]), (255,255,255))
screen.set_at((food_array[2,0],food_array[2,1]), (255,255,255))

pygame.display.flip()
eating_timer = 0
eat_flag = 0

while running:
    #Crash at borders
    if AI.x<=0 or AI.x>=width or AI.y<=0 or AI.y>=height:
        print 'Crash'
        running=False

    #Close on exit
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill((0,0,0))
    #Draw food locations
    screen.set_at((food_array[0,0],food_array[0,1]), (255,255,255))
    screen.set_at((food_array[1,0],food_array[1,1]), (255,255,255))
    screen.set_at((food_array[2,0],food_array[2,1]), (255,255,255))
    #Food stuff
    a,b=find_food.find_food(AI, food_array)
    flag=go_to_food.go_to_food(a,b,AI)
    #Movement
    AI.rand_event(flag)
    AI.move_AI()
    AI.draw_AI(screen)
    for i in range(len(food_array)):
        if AI.x == food_array[i,0] and AI.y == food_array[i,1]:
            food_array[i,0] = random.randint(100,540)
            food_array[i,1] = random.randint(100,540)

    pygame.display.flip()
    clock.tick(100)


