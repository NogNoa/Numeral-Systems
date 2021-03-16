def Roman(n):
        m=n
        def Rdigit(i,v,x,r,n):
                half=n%10>4
                if n%5==4:
                        r=i+(x*half or v)+r
                else:
                        r=i*(n%5)+r
                        r=(v*half)+r
                return r
        if n<=0:
                print('Haec numerus ridicula est'.upper())
                return str(n)
        r=''
        il=['I','X','C','M'] #i list
        vl=['V','L','D'] #v list
        for id in range(3):                
                if n==0:
                        break
                r=Rdigit(il[id],vl[id],il[id+1],r,n)
                n=n//10             
        if n>4:
                r='...MMMM'+r
        else:
                r='M'*n+r
        print (m,' in Roman numerals is ',r)
        return r