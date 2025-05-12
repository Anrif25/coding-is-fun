#check the complexity at: https://www.bigocheatsheet.com/

import random



class sort:
    def __init__(self):
        self.list = []
        self.list = random.sample(range(1, 10), k=9)
        self.leght = len(self.list)
        print(self.list)
    
    def bubblesort(self):
        
        j= self.leght -1
        for i in range(self.leght):
            for j in range(0,self.leght-i - 1):
                if self.list[j] > self.list[j+1]:
                    temp = self.list[j]
                    self.list[j]= self.list[j+1]
                    self.list[j+1]= temp
        print(f"bubble sort: {self.list}")
    
     
    def interchangesort(self):
        print(self.list)
        for i in range(self.leght):
            for j in range(self.leght):
                if self.list[i] < self.list[j]:
                    temp = self.list[j]
                    self.list[j]= self.list[i]
                    self.list[i]= temp
        print(f"interchange sort: {self.list}")
                    

if __name__== "__main__":
    s = sort()
    #s.bubblesort()
    s.interchangesort()
        
        