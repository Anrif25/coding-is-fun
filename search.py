import random
#basic search
class search:
    def __init__(self):
        self.find = int(input("nhập vào số cần tìm: "))
        self.list= []
        self.list = random.sample(range(1, 10), k=9)
        print(self.list)
        
    def linesearch(self):
        if self.find in self.list:
             return (f"found {self.find} in list")
        else:
            return (" not found in list")
        
    def usingfor(self):
        #using enumerate
        for idx, val in enumerate(self.list):
            if self.find == val:
                return f"found it at position {idx+1}"
        return "not found it"
    
    def binarysearch(self):
        left = 0 
        right = len(self.list) -1
        
        self.list.sort()
        print(self.list)
        while(left<right or left == right):
            mid = int(left + right /2)
            print(self.list[mid])
            if self.find == self.list[mid]:
                return("found using binary search1 ")
            elif(self.list[mid] > self.find):
                left = mid +1
            else:
                right = mid - 1
            return("not found using binary search")
                
                
                

if __name__== "__main__":
    s = search()
    print(s.linesearch())
    print(s.usingfor())
    print(s.binarysearch())