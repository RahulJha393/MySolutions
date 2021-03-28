#CodeJam 2021 question 1 solution in python
T=int(input())
for x in range(T):
    le=int(input())
    li=[int(x) for x in input().split()]
    co=0
    for i in range(0,le-1):
        co+=len(li[i:li.index(min(li[i:]))+1])
        li=li[:i]+li[i:li.index(min(li[i:]))+1][::-1]+li[li.index(min(li[i:]))+1:]
    print("Case #"+str(x+1)+": "+str(co))
