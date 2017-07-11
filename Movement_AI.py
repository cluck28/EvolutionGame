#Need to update move method to account for genetics
'''
Make a class that controls the movement of the AI
After each movement the health is decreased by a small amount
'''

import Health
import pygame
import random

class Movement_AI(Health.Health):
    #Initialize the Movement_AI class as a child of the Health class
    def __init__(self,genome=[],x=100,y=100):
        Health.Health.__init__(self,genome=[],disease=0.0,injury=1.0)
        self.x=x
        self.y=y
        self.x_move=0
        self.y_move=0
        self.color=self.get_gene_color()

    #Generate random number to simulate button presses
    def rand_event(self,flag=0):
        #Account for movement genetics in terms of speed
        upper_lim=self.get_gene_movement()
        new_val=random.randint(1,upper_lim)
        if new_val == 1:
            if flag==0:
                value=random.randint(1,4)
                if value==1:
                    self.x_move=0
                    self.y_move=-1
                elif value==2:
                    self.x_move=0
                    self.y_move=1
                elif value==3:
                    self.x_move=-1
                    self.y_move=0
                elif value==4:
                    self.x_move=1
                    self.y_move=0
            elif flag==1: #Food is located to the right
                value=random.randint(1,16)
                if value==1:
                    self.x_move=0
                    self.y_move=-1
                elif value==2:
                    self.x_move=0
                    self.y_move=1
                elif value==3:
                    self.x_move=-1
                    self.y_move=0
                else:
                    self.x_move=1
                    self.y_move=0
            elif flag==2: #Food is located to the left
                value=random.randint(1,16)
                if value==1:
                    self.x_move=0
                    self.y_move=-1
                elif value==2:
                    self.x_move=0
                    self.y_move=1
                elif value==3:
                    self.x_move=1
                    self.y_move=0
                else:
                    self.x_move=-1
                    self.y_move=0
            elif flag==3: #Food is located up
                value=random.randint(1,16)
                if value==1:
                    self.x_move=1
                    self.y_move=0
                elif value==2:
                    self.x_move=0
                    self.y_move=1
                elif value==3:
                    self.x_move=-1
                    self.y_move=0
                else:
                    self.x_move=0
                    self.y_move=-1
            elif flag==4: #Food is located down
                value=random.randint(1,16)
                if value==1:
                    self.x_move=0
                    self.y_move=-1
                elif value==2:
                    self.x_move=1
                    self.y_move=0
                elif value==3:
                    self.x_move=-1
                    self.y_move=0
                else:
                    self.x_move=0
                    self.y_move=1
        else:
            self.x_move=0
            self.y_move=0

    #Move the AI based on the random number
    #As health decreases move less
    def move_AI(self):
        if self.x_move!=0 or self.y_move!=0:
            #Amount should be approx 0.01
            if self.health<=0.5:
                #do nothing/sleep when implemented
                self.rec_health(2.5)
                self.x=self.x
                self.y=self.y
            elif self.health<=1.0:
            #Have a 1 in 40 chance of moving
                if random.randint(1,40)==1:
                    self.x+=self.x_move
                    self.y+=self.y_move
                    amount=0.01
                    self.loss_health(amount)
            elif self.health<=1.5:
            #Have a 1 in 20 chance of moving
                if random.randint(1,20)==1:
                    self.x+=self.x_move
                    self.y+=self.y_move
                    amount=0.01
                    self.loss_health(amount)
            elif self.health<=2.0:
            #Have a 1 in 10 chance of moving
                if random.randint(1,10)==1:
                    self.x+=self.x_move
                    self.y+=self.y_move
                    amount=0.01
                    self.loss_health(amount)
            elif self.health<=2.5:
            #Have a 1 in 5 chance of moving
                if random.randint(1,5)==1:
                    self.x+=self.x_move
                    self.y+=self.y_move
                    amount=0.01
                    self.loss_health(amount)
            else:
            #Have a 1 in 1 chance of moving
                if random.randint(1,1)==1:
                    self.x+=self.x_move
                    self.y+=self.y_move
                    amount=0.01
                    self.loss_health(amount)

    #Draw the AI at its new location
    def draw_AI(self, surface):
        surface.set_at((self.x,self.y),self.color)
        
