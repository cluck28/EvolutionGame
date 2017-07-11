#Make it so reproduction occurs where the mother is

'''
A class that combines the genome of two different objects. Incorporates random
mutations into the reproduction process
'''

import random
import Movement_AI
import Movement

class Reproduce():
    #Create an instance of the reproduce class
    def __init__(self):
        self.genome1=[]
        self.genome2=[]

    #Combines two genomes into one
    #Randomly selects on digit from each pair representing a gene
    def repro(self, genome1, genome2):
        self.genome1=genome1.get_genome()
        self.genome2=genome2.get_genome()
        self.x=genome1.x
        self.y=genome1.y
        genome=[]
        for i in range(5):
            chancea=random.randint(1,2)
            chanceb=random.randint(1,2)
            even=2*i
            odd=2*i+1
            if chancea==1 and chanceb==1:
                genome.append(self.genome1[even])
                genome.append(self.genome2[even])
            elif chancea==1 and chanceb==2:
                genome.append(self.genome1[even])
                genome.append(self.genome2[odd])
            elif chancea==2 and chanceb==1:
                genome.append(self.genome1[odd])
                genome.append(self.genome2[even])
            else:
                genome.append(self.genome1[odd])
                genome.append(self.genome2[odd])
        new=Movement_AI.Movement_AI(genome,self.x,self.y)
        new.mutate()
        return new

            
        
        
