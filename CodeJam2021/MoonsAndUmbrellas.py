#If you want to clear the 3rd test set as well to get an addition marks then you have to create a additional logic to
#claculate if in case the prices of 'CJ' and 'JC' are negative

#solution for question 2 code jam 2021
def Cost(s,x,y):
    return s.count('cj')*x+s.count('jc')*y
def reduce(x,y,s):
    s=s.lower()
    cost=0
    if('j' in s and 'c' in s):
        while('????' in s):
            s=s.replace("????","???")
        
        
        while('jj' in s):
            s=s.replace('jj','j')
        while('cc' in s):
            s=s.replace('cc','c')
        
        if(s[:2]=='cj'or s[:2]=='jc'):
            cost+=(s[:2]=='cj')*x+(s[:2]=='jc')*y
            s=s[1:]
        
       
        if(s[-2:]=='cj'or s[-2:]=='jc'):
            cost+=(s[-2:]=='cj')*x+(s[-2:]=='jc')*y
            s=s[:-1]
        
        while(s[-1]=='?'):
            s=s[:-1]
        while(s[0]=='?'):
            s=s[1:]
        while('c??c' in s):
            s=s.replace("c??c",'c')
            
        while('j??j' in s):
            s=s.replace("j??j",'j')
            
        while('c???c' in s):
            s=s.replace("c???c",'c')
            
        while('j???j' in s):
            s=s.replace("j???j",'j')
            
        while('j??c' in s):
            s=s.replace('j??c','jc')
            
        while('c??j' in s):
            s=s.replace('c??j','cj')
        
        while('c?c' in s):
            s=s.replace('c?c','c')
            
        while('j?j' in s):
            s=s.replace('j?j','j')
    
        s=s.replace('j?c','jc')
        
        s=s.replace('c?j','cj')
        
        while('j???c' in s or 'c???j' in s):
            if('j???c' in s):
                #code
                cost+=s.count('j???c')*min([0,x+y])
                s=s.replace('j???c','jc')
            elif('c???j' in s):
                cost+=s.count('c???j')*min([0,x+y])
                s=s.replace('c???j','cj')
                #code
        
        cost+=Cost(s,x,y)
        return cost
    else:
        return 0
    
T=int(input())
l=[]
for t in range(T):
    X,Y,S=list(input().split(" "))
    X=int(X)
    Y=int(Y)
    l.append([X,Y,S])
for q in range(T):
    print("Case #"+str(q+1)+": "+str(reduce(l[q][0],l[q][1],l[q][2])))
