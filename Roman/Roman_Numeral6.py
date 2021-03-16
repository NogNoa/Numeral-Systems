def Roman(n):
        m=n
        def Rdigit(i,v,x,r,n):
                if n%10==9:
                        r=i+x+r
                elif n%10==4:
                        r=i+v+r
                elif 4<n%10:
                        r=v+i*(n%5)+r
                else:
                        r=i*(n%5)+r
                return r
        if n<=0:
                print('Haec numerus ridicula est'.upper())
                return ''
        r=''
        id=0 #index
        il=['I','X','C','M'] #i list
        vl=['V','L','D'] #v list
        for i in range(3):
                
                if n==0:
                        break
                r=Rdigit(il[i],vl[i],il[i+1],r,n)
                n=n//10             
        if n>4:
            r='?MMMM'+r
            print (m,' in Roman numerals is ',r)
            return r
        while n>0:
                r='M'+r
                n-=1
        print (m,' in Roman numerals is ',r)
        return r
Roman(195)
