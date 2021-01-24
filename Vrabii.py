import math
with open('vrabii.in.txt','r')as f:
    n=eval(f.readline())
v=c=b=0
for i in range(2,int(n)+1):
    c=i
    for j in range(2,int(math.sqrt(c))+1):
        if(c%j!=0):
            b=0
        else:
            b=1
            break
    if(b==0):
        v+=1
with open('vrabii.out.txt','w')as f:
    f.write(str(v))