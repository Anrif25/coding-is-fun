import random

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


if __name__== "__main__":
    s = search()
    print(s.linesearch())