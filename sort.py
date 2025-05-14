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
    
    def _swap(self, i, j):
        self.list[i], self.list[j] = self.list[j], self.list[i]

    def selectionsort(self):
        for i in range(self.leght):
            min= self.list[i]
            for j in range(i+1,self.leght):
                if self.list[j]< min:
                    min = self.list[j]
                    self._swap(i,j)

        print(f"selectionsort: {self.list}")
    
    def insertsort(self):
        for i in range(1,self.leght):
            key = self.list[i]
            j=i-1
            while(j>=0 and self.list[j]> key):
                self.list[j+1] = self.list[j]
                j -=1
            self.list[j+1]= key
        print(f"insertsort: {self.list}")
    
    #shellsort kinda "better insertsort"
    def shellsort(self):
        gap = int(self.leght/2)
        while gap >0: 
            for i in range(int(gap),self.leght):
                key=self.list[i]
                j=i
                while (j >= gap and self.list[j-gap] > key):
                    self.list[j] = self.list[j-gap]
                    j -=gap
                self.list[j]= key
            gap =int(gap/2)
            print(gap)
        print(f"shellsort: {self.list}")        
    
    def quicksort(self):
        def _partition(lo,hi):
            pivot = self.list[hi]
            i = lo-1
            
            for j in range(lo,hi):
                if self.list[j] <= pivot:
                    i+=1
                    self._swap(i,j)
                
            self.list[i+1], self.list[hi] = self.list[hi], self.list[i+1]
            return i+1
        def _quick(lo,hi):
            if lo<hi:
                p = _partition(lo,hi)    

                _quick(lo,p-1)
                
                _quick(p+1,hi)
        _quick(0,self.leght-1)
        
        print(f"quicksort: {self.list}")
                       
if __name__== "__main__":
    s = sort()
    #s.bubblesort()
    #s.interchangesort()
    #s.selectionsort()
    #s.insertsort()
    #s.shellsort()
    s.quicksort()
        
        