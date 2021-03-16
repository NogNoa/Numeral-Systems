def Roman(n):
        m=n
        def Rdigit(i,v,x,r,n):
                if (n%10)//5==0:
                        x=v #the 4/9 role
                        v='' #the >5 role
                if n%5==4:
                        r=i+x+r
                        n=n//10
                        return r
                while n%5>0:
                        r=i+r
                        n-=1
                r=v+r
                return r
        if n==0:
                return n
        r=''
        id=0 #index
        il=['I','X','C','M','X̄','C̄','M̄'] #i list
        vl=['V','L','D','V̄','L̄','D̄'] #v list
        for i in range(6):
                if n==0:
                        break
                r=Rdigit(il[i],vl[i],il[i+1],r,n)
                n=n//10
        if n>4:
            r='?M̄M̄M̄M̄'+r
            print (m,' in Roman numerals is ',r)
            return r
        while n>0:
                r='M̄'+r
                n-=1
        print (m,' in Roman numerals is ',r)
        return r
Roman(999999)
