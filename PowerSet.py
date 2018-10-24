import math; 
  
def powerSet(LIST,SIZE): 
    sizeOfAll = (int) (math.pow(2, SIZE))
    i = 0
    binary = 0
    print("Φ")
    for i in range(1, sizeOfAll):
        binary = format(i,'0'+str(SIZE)+'b')
        j=0
        for j in range(0,SIZE):
            if binary[j] == '1':
                print(LIST[j],end="")
        print()

powerSet(['a', 'b', 'c','d'], 4)
