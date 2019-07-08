from itertools import combinations
string=input()
for i in range(1,len(string)+1):
    maximum=0
    val=list(combinations(string,i))
    for j in val:
        count=0
        li=[]
        for k in j:
            if(k not in li):
                li.append(k)
        if(len(li)>maximum):
            maximum=len(li)            
print(maximum)
