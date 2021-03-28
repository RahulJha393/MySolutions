#Solution for the reverse sort engineering google code jam 2021
def pal(l,i,n):
         return l[:i]+l[i:i+n][::-1]+l[i+n:]
def givel(l,n):
    def ret(l,n):
        l=[x for x in range(1,l+1)][::-1]
        i=len(l)-1
        while(sum(l)!=n):
            if((l[i]==1 and i<len(l)-1) or (l[i]==0 and i==len(l)-1)):
                i-=1
            else:
                l[i]-=1
        return l
    Q=ret(l,n)
    L=[x for x in range(1,l+1)]
    for x in range(l):
        L=pal(L,l-1-x,Q[l-1-x])
    return L
for x in range(1,int(input())+1):
         l,s=(int(x) for x in input().split())
         if(s<l-1 or s>int(l*(l+1)/2)-1):
                  print("Case #"+str(x)+": "+"IMPOSSIBLE")
         else:
                  print("Case #"+str(x)+": "+givel(l,s).__str__().replace("[","").replace("]","").replace(",",""))
