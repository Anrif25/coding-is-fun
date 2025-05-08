import random
#basic search
class search:
    def __init__(self):
        self.find = int(input("nhập vào số cần tìm: "))
        self.list= []
        for i in range(1,10):
            self.list.append(random.randrange(1,10))
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

if __name__== "__main__":
    s = search()
    print(s.linesearch())
    print(s.usingfor())