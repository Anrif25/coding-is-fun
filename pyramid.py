class pyramid:
    #rows = int(input("enter the number of rows: "))
    def rightpyramid(rows):
        for i in range(1,rows+1):
            for j in range(1,i+1):
                print("*", end=" ")
            print("")
    def reversedrightpyramid(rows):
        for i in range(rows,0,-1):
            for j in range(1,i+1):
                print("*", end=" ")
            print()
    def leftpyramid(rows):
        for i in range(1,rows+1):
            for j in range(1,rows-i+1):
                print(" ",end =" ")
            for j in range(1,i+1):
                print("*", end = " ")
            print()
    
    def middlepyramid(rows):
        for i in range(1, rows +1 ):
            for j in range(rows - i):
                print(" ", end =" ")
            for j in range(1,i*2):
                print("*", end = " ")   
            print()
    def upsidedownpyramid(rows):
          for i in range(rows,0,-1):
            for j in range( rows - i):
                print(" ", end =" ")
            for j in range(1,i*2):
                print("*", end = " ")  
            print()
    #use something else beside upsidedownpyrmid and middlepyramid
    def diamond(rows):
        for i in range(0, rows+1):
            i = i - (rows//2 +1)
            if i < 0:
                i = -i
            print(" " * i + "*" * (rows - i*2) + " "*i)
            
pyramid()
pyramid.rightpyramid(4)
print("//////////////")
pyramid.reversedrightpyramid(4)
print("//////////////")
pyramid.leftpyramid(4)
print("//////////////")
pyramid.middlepyramid(4)
print("//////////////")
pyramid.upsidedownpyramid(4)
print("//////////////")
pyramid.diamond(4)
