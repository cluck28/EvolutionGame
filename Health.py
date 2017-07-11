'''
Make a class that contains the health object.
The health is controlled based on a number of factors:
1. Activity - Movement equates to a loss in health
2. Sleep - Recovers health
3. Food - Recovers health
4. Injury/Disease - Decreases health
5. Genetics - Determine impacts of 1-4
 i. Strong - High health, low injury rate, low activity cost, food/water recover low
 ii. Moderate - Med health, med injury rate, med activity cost, food/water recover med
 iii. Weak - Low health, high injury rate, high activity cost, food/water recover high
'''

import Genome

#Controls the health object
class Health(Genome.Genome):
    #Initialize the health object as a child of the genome
    def __init__(self,genome=[],disease=0,injury=1):
        Genome.Genome.__init__(self,genome=[])
        self.injury=injury #Injury [1,5] 5 is worst
        self.disease=disease #Disease [0,1] 1 is worst
        if self.genome==[]:
            self.set_genome()
        if self.get_gene_health()==1:
            self.max_health=5.0
        elif self.get_gene_health()==2:
            self.max_health=4.0
        elif self.get_gene_health()==3:
            self.max_health=3.0
        self.health=3.0

    #Increase maximum health
    def incr_max_health(self):
        self.max_health+=(1.0/self.get_gene_health())
     
    #Raise injury level
    def injured(self):
        if self.injury==5:
            self.injury=self.injury
        else:
            self.injury+=1
        print 'You were injured'

    #Return current injury level
    def get_injury(self):
        return self.injury

    #Raise sickness level
    def sick(self):
        if self.disease==1:
            self.disease=self.disease
        else:
            self.disease+=0.1
        print 'You got sick'

    #Returns the current value of the disease
    def get_sick(self):
        return self.disease

    #Returns the current value of health
    def get_health(self):
        return self.health

    #Makes health decrease
    def loss_health(self,amount):
        new_health=self.health-amount*self.injury*self.get_gene_health()/3.0-0.1*self.disease
        if new_health<=0:
            self.health=self.max_health
            print 'You died'
        else:
            self.health=new_health

    #Makes health increase
    def rec_health(self,amount):
        new_health=self.health+amount*self.injury*self.get_gene_health()/3.0
        if self.injury==1:
            if new_health>=self.max_health:
                self.health=self.max_health
            else:
                self.health=new_health
        elif self.injury==2:
            if new_health>=self.max_health:
                self.health=self.max_health
                self.injury-=1
            else:
                self.health=new_health/self.injury
                self.injury-=1
        elif self.injury==3:
            if new_health>=self.max_health:
                self.health=self.max_health
                self.injury-=1
            else:
                self.health=new_health/self.injury
                self.injury-=1
        elif self.injury==4:
            if new_health>=self.max_health:
                self.health=self.max_health
                self.injury-=1
            else:
                self.health=new_health/self.injury
                self.injury-=1
        elif self.injury==5:
            if new_health>=self.max_health:
                self.health=self.max_health
                self.injury-=1
            else:
                self.health=new_health/self.injury
                self.injury-=1
