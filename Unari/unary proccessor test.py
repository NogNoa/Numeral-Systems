print("Please enter 4 digits with no spaces or punctuation")
while True:
    Bub=list(input())
    try:
        Bub=[int(i) for i in Bub[:4]]
        if len(Bub)==4:
            break
        else:
            print("Please at least 4 numbers")
    except:
        print("Please enter numbers only")
Check=(Bub[1]+Bub[0])*(Bub[2]**Bub[3])
Bub.append('Empty')
A=4000
def Load(i,j):
    return Bub[i]+Bub[j]*10
def Store(i,j):
    global A
    A=A%100
    Bub[i]=A%10
    Bub[j]=A//10
    Bub[4]='Empty'
    return Bub
A=Load(0,1)   
A=(A%10)+(A//10)
Bub=Store(0,1)
A=Load(2,3)
A=(A%10)**(A//10)
Bub=Store(2,3)
A=Load(0,3)
A=(A%10)*(A//10)
Bub=Store(3,4)
A=Load(1,2)
A=(A%10)*(A//10)
Bub=Store(1,4)
A=Load(0,2)
A=(A%10)*(A//10)
Bub=Store(0,2)
A=Load(1,3)
A=A%10+A//10
Bub=Store(1,4)
A=Load(1,2)
A=A%10+A//10
Bub=Store(1,4)
Mem=str(Bub[1])+str(Bub[0])
print('Memory',Mem)
print('Check', Check%100)
