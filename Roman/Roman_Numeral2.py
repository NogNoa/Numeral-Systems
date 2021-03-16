def Roman(n):
        m=n
        def Rdigit(i,v,x,r,n,id):
                id+=1
                if (n%10)//5==0:
                        x=v #the 4/9 role
                        v='' #the >5 role
                if n%5==4:
                        r=i+x+r
                        n=n//10
                        if n>0 and id<3:
                                print (r,'a')
                                r=Rdigit(il[id],vl[id],il[id+1],r,n,id)
                        return r
                while n%5>0:
                        r=i+r
                        n-=1
                r=v+r
                n=n//10
                if n>0 and id<3:
                        print (il[id],' 2 ',vl[id])
                        r=Rdigit(il[id],vl[id],il[id+1],r,n,id)
                return r
        if n==0:
                return n
        r=''
        id=0 #index
        il=['I','X','C','M'] #i list
        vl=['V','L','D'] #v list
        r=Rdigit(il[id],vl[id],il[id+1],r,n,id)
        if n>4000:
            r='?MMMM'+r
            print (n,' in Roman numerals is ',r)
            return r
        while n>999:
                r='M'+r
                n-=1000
        print (m,' in Roman numerals is ',r)
        return r
Roman(4999)
