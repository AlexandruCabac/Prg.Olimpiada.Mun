with open('bomboane.in.txt','r')as f:
    n,k,p=f.readline().split()
s=0
d=1
for i in range(0,int(n)):
    s+=int(k)
    if(i==(int(p)*d)-1):
        d+=1
        k=int(k)+1
        if(s%2==0):
            s=s//2
        else:
            s=(s-1)//2
with open('bomboane.out.txt','w')as f:
    f.write(str(s))