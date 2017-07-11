'''
A method that allows either the user or AI to eat food and recover a set amount of health.
If the recovered health is greater than max_health, max_health is set

This will need to be rewritten to acount for the change of the food object to an image
'''

import pygame
import Movement
import Movement_AI
import random

def eat_food(movement, pixarray):
    #Remove food from PixelArray for the surface
    i=movement.x
    j=movement.y
    pixarray[i][j]=surface.map_rgb((0,0,0))#Make the pixel black
    #Make new food
    x=random.randint(10,surface.get_width()-10)
    y=random.randint(10,surface.get_height()-10)
    pixarray[x][y]=surface.map_rgb((77,255,51))
    pygame.display.flip()
    
