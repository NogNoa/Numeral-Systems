In=[]
a=3
while a>0:
    try:
        b=int(input())
        while b>0:
            In.append(1)
            b-=1
        a-=1
        if a>0:
            In.append("#")
        else:
            In.append("Δ")
        print(In) 
    except:
        print('please type a number')
j=input()
#In=[1,1,1,1,1,"#",1,1,"#",1,1,1,"Δ","Δ","f"]
m="i"
r=0
q=False
while q==False:
    print("be ",r,"=",In[r])
    print(m)
    if m=="i":
        if In[r]==1:
            In[r]="x"
            r+=1
            m="b"
        elif In[r]=="#":
            In[r]="Δ"
            r+=1
            m="p"
    elif m=="p":
        if In[r]==1 or In[r]==2 or In[r]==3 or In[r]=="#":
            In[r]="Δ"
            r+=1
        elif In[r]=="y":
            In[r]="Δ"
            r+=1
            m="g"
        elif In[r]=="Δ":
            q=True
    elif m=="a":
        if In[r]==1:
            r+=1
            m="b"
        elif In[r]=="#":
            In[r]="y"
            r-=1
            m="d"
    elif m=="b":
        if In[r]==1:
            In[r]=int(2)
            r+=1
            m="c"
        elif In[r]=="#":
            In[r]="y"
            r-=1
            m="d"
    elif m=="c":
        if In[r]==1:
            In[r]=int(3)
            r+=1
            m="a"
        elif In[r]=="#":
            In[r]="y"
            r-=1
            m="d"
    elif m=="d":
        if In[r]==1:
            r-=1
            m="e"
        elif In[r]==2:
            r-=1
            m="j"
        elif In[r]==3:
            m="x"
        elif In[r]=="x":
            In[r]="Δ"
            r+=1
            m="p"
    elif m=="e":
        if In[r]==1 or In[r]==2 or In[r]==3:
            r-=1
        elif In[r]=="x":
            In[r]="Δ"
            r+=1
            m="p"
    elif m=="g":
        if In[r]==1:
            r+=1
        elif In[r]=="#":
            In[r]="Δ"
            r+=1
            m="p"
        elif In[r]=="Δ":
            q=True
        elif In[r]=="y":
            In[r]="Δ"
            r+=1
            m="k"
    elif m=="j":
        if In[r]==1 or In[r]==2 or In[r]==3:
            r-=1
        elif In[r]=="x":
            In[r]="Δ"
            r+=1
            m="f"
    elif m=="f":
        if In[r]==1 or In[r]==2 or In[r]==3 or In[r]=="y":
            In[r]="Δ"
            r+=1
        elif In[r]=="#":
            In[r]="Δ"
            r+=1
            m="g"
    elif m=="x":
        if In[r]==1:
            r-=1
        elif In[r]==2 or In[r]==3:
            In[r]=int(1)
            r-=1
        elif In[r]=="Δ":
            q=True
        elif In[r]=="x":
            In[r]=int(1)
            r+=1
            m="g"
    elif m=="k":
        if In[r]==1 or In[r]=="#":
            In[r]="Δ"
            r+=1
            m="v"
        elif In[r]=="Δ":
            q=True
    elif m=="v":
        if In[r]==1:
            In[r]="Δ"
            r+=1
        elif In[r]=="#":
            In[r]="Δ"
            r+=1
            m="p" 
    #print("af ",r,"=",In[r]) 
print("list:")
#r=0
#while not In[r]=="f":
    #print(In[r])
    #r+=1
print(In)
j=input()
