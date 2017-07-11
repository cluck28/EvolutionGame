'''
A method to give the direction the AI should travel in to arrive at food.
This returns a flag:
flag=1 => the food is to the right
flag=2 => the food is to the left
flag=3 => the food is located above
flag=4 => the food is located below

This flag is then passed to the rand_event() method of Movement_AI
This does not need to be changed
'''

import Movement_AI

#Inputs are the location of the nearest food
def go_to_food(x,y,AI):
    flag=0
    x_pos=AI.x
    y_pos=AI.y
    if x_pos-x !=0:
        if x_pos-x<0:
            flag=1 #Go right
        else:
            flag=2 #Go left
    elif y_pos-y !=0:
        if y_pos-y<0:
            flag=4 #Go down
        else:
            flag=3 #Go up
    else:
        flag=0
    return flag
