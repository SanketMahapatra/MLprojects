matrix=[]

value=0
for i in range(10):
    coloumn=[]
    for j in range(10):
        coloumn.append(value)
        value += 1
        matrix.append(coloumn)
        
        print("10x10 matrix :")
        for coloumn in matrix:
            print(coloumn)