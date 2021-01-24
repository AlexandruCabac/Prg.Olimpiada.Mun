with open('cangur.in.txt','r') as f:
    a,b=f.readline().split()
c=[int(a)]
s=int(a)
for i in range(1,int(b)):
    c.extend([c[i-1]*10+c[0]])
    s+=c[i]
with open('cangur.out.txt','w') as f:
    f.write(str(s))