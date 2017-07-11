'''
An object that encodes all of the genetic information 
about a sprite. Also allows for random mutations.
There are 5 categories in the genome:
1. Sex - The objects sex/gender
2. Health - The objects health ~ 1,2,3 are categories
3. Movement - The objects movement ability
4. Color - The objects color, impacts predation
5. Size - The objects size, impacts predation, mobility, reproduction
'''

import random

class Genome():
    #Initialize the genome
    def __init__(self, genome=[]):
        self.genome=genome
        if self.genome != []:
            self.gene_sex=self.genome[0]+self.genome[1]
            self.gene_health=self.genome[2]+self.genome[3]
            self.gene_movement=self.genome[4]+self.genome[5]
            self.gene_color=self.genome[6]+self.genome[7]
            self.gene_size=self.genome[8]+self.genome[9]

    #Set the genome
    def set_genome(self):
        self.genome=[]
        for i in range(10):
            self.genome.append(random.randint(1,9))
        self.gene_sex=self.genome[0]+self.genome[1]
        self.gene_health=self.genome[2]+self.genome[3]
        self.gene_movement=self.genome[4]+self.genome[5]
        self.gene_color=self.genome[6]+self.genome[7]
        self.gene_size=self.genome[8]+self.genome[9]

    #Get all ten bits of the genome
    def get_genome(self, lower=0, upper=9):
        genome=[]
        for i in range(lower,upper+1):
            genome.append(self.genome[i])
        return genome

    #Get the value of the sex gene
    #1~female
    #2~male
    def get_gene_sex(self):
        if self.gene_sex<9:
            converted_sex=1#Female
        elif self.gene_sex>9:
            converted_sex=2#Male
        else:
            chance=random.randint(1,2)
            if chance==1:
                converted_sex=1#Female
            else:
                converted_sex=2#Male
        return converted_sex

    #Get the value of the health gene
    #1~Strong
    #2~Med
    #3~Weak
    def get_gene_health(self):
        if self.gene_health<=6:
            converted_gene_health=1#Strong
        elif self.gene_health<=11:
            converted_gene_health=2#Med
        else:
            converted_gene_health=3#Weak
        return converted_gene_health

    #Get the value of the movement gene
    def get_gene_movement(self):
        if self.gene_movement<=6:
            converted_gene_movement=1#Fast
        elif self.gene_movement<=11:
            converted_gene_movement=2#Med
        else:
            converted_gene_movement=3#Slow
        return converted_gene_movement

    #Get the value of the color gene
    def get_gene_color(self):
        if self.gene_color<=3:
            converted_gene_color=(255,255,255)#WHITE
        elif self.gene_color<=6:
            converted_gene_color=(127,52,0)#BROWN
        elif self.gene_color<=11:
            converted_gene_color=(255,0,0)#RED
        elif self.gene_color<=17:
            converted_gene_color=(25,255,247)#BLUE
        else:
            converted_gene_color=(255,255,255)#WHITE
        return converted_gene_color

    #Get the value of the size gene
    def get_gene_size(self):
        return self.gene_size

    #A one in ten chance to alter on element of the genome
    def mutate(self):
        chance=random.randint(1, 10)
        if chance==1:
            up_down=random.randint(1,2)
            which_el=random.randint(0,9)
            if self.genome[which_el]==9:
                if up_down==1:
                    self.genome[which_el]=8
                else:
                    self.genome[which_el]=1
            elif self.genome[which_el]==1:
                if up_down==1:
                    self.genome[which_el]=9
                else:
                    self.genome[which_el]=2
            else:
                if up_down==1:
                    self.genome[which_el]-=1
                else:
                    self.genome[which_el]+=1


