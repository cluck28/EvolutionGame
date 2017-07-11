'''
A method that returns the location of the nearest food pixel to a
Movement_AI object
The input is the AI and a matrix of pixel coordinates (food) and this program 
should return the coordinates of the nearest food pixel
'''
import Movement_AI


import pygame
from numpy import *

#Returns a value corresponding to the direction the Movement_AI object should move
def find_food(AI,matrix):
    #Location of the Movement_AI object
    x=AI.x
    y=AI.y
    #Keep track of nearest food space
    a=1
    b=1
    #Shortest distance between the AI and the food
    r=1000
    #Loop through all values and find the shortest distance
    row=0
    while row<len(matrix):
        r1=sqrt((matrix[row,0]-x)**2+(matrix[row,1]-y)**2)
        if r1<=r:
            a=matrix[row,0]
            b=matrix[row,1]
            r=r1
        row+=1
    return a,b
