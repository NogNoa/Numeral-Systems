def Roman(n):
        def Rdigit(i,v,x,r,d):
                if d//5==0:
                        x=v #the 4/9 role
                        v='' #the >5 role
                if d%5==4:
                        r=i+x+r
                        return r
                while d%5>0:
                        r=i+r
                        d-=1
                r=v+r
                return r
        if n==0:
                return n
        r=''
        r=Rdigit('I','V','X',r,n%10)
        d=n//10
        if d>0:
                r=Rdigit('X','L','C',r,d%10)
                d=d//10
                if d>0:
                        r=Rdigit('C','D','M',r,d%10)
                        if d>40:
                                r='?MMMM'+r
                                return r
                        while d>9: #We don't need to divide by 10. So instead of 'not <1' being >0 'not <10' is >9. Below we subtract 10 each tick.
                                r='M'+r
                                d-=10
        return r
Roman(555)
print (555,' in Roman numerals is ',r)
