def Roman(n):
        m=n
        def Rdigit(i,v,x,r,n):
                #r=(i+(v*(n%2==0)or x))*(n%5==4)or(v*(n%10>4)+i*(n%5))+r
                r=i*(n%5==4)+(x*(n%10==9) or v*(3<n%10))+i*(n%5)*(0<n%5<4)+r
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
Roman(284)
