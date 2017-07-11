#Need to update move method to account for genetics
#Have accounte for movement in terms of the speed at which you move but this is 
#frustrating for the user
'''
Make a class that controls the movement of the sprite
After each movement the health is decreased by a small amount
'''

import Health
import pygame
import random

class Movement(Health.Health):
    #Initialize the Movement class as a child of the Health class
    def __init__(self,genome=[],x=100,y=100):
        Health.Health.__init__(self,genome=[],disease=0.0,injury=1.0)
        self.x=x
        self.y=y
        self.x_move=0
        self.y_move=0
        self.color=self.get_gene_color()

    #Check for button presses indicating movement
    def key_event(self,event):
        #Odds of moving is based on movement gene
        upper_lim=self.get_gene_movement()
        value=random.randint(1,upper_lim)
        if value == 1:
            if event.key==pygame.K_UP:
                self.x_move=0
                self.y_move=-1
            elif event.key==pygame.K_DOWN:
                self.x_move=0
                self.y_move=1
            elif event.key==pygame.K_LEFT:
                self.x_move=-1
                self.y_move=0
            elif event.key==pygame.K_RIGHT:
                self.x_move=1
                self.y_move=0
        else:
            self.x_move=0
            self.y_move=0

    #Move the sprite based on the key
    #Decrease the heatlh based on move_gene and size_gene
    def move(self):
        if self.x_move==0 and self.y_move==0:
            self.x+=self.x_move
            self.y+=self.y_move
        else:
            self.x+=self.x_move
            self.y+=self.y_move
            amount=0.01#The amount once calculated should be apporoximately this
            self.loss_health(amount)

    #Draw the sprite at its new location
    def draw(self, surface):
        surface.set_at((self.x,self.y),self.color)
