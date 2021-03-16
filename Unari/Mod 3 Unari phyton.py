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
    except:
        print('please type a number')
#In=[1,1,1,1,1,"#",1,1,"#",1,1,1,"Δ","Δ","f"]
t=False
Work=[]
r=0
q=0
while t==False:
    if In[r]==1:
       q+=1
    else:
       Work.append(q)
       q=0
       if In[r]=="Δ":
           t=True
    r+=1
print('My output is ',Work[Work[0]%3])
