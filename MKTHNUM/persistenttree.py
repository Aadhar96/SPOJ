from math import ceil,log
from bisect import bisect_left
from sys import stdin,stdout

class Node:
    def __init__(self,a=0,b=None,c=None):
        self.count=a
        self.le=b
        self.ri=c

def make(a,b,c):
    if(b==c):
        seg[a].le=None
        seg[a].ri=None
        return a
    tmp=2*a
    mid=(b+c)//2
    seg[a].le=make(tmp,b,mid)
    seg[a].ri=make(tmp+1,mid+1,c)
    return a

def update(a,b,c,d,e):
    if(b==c):
        seg[ho+e].count=1
        seg[ho+e].le=None
        seg[ho+e].ri=None
        return
    mid=(b+c)//2
    tmp=2*a
    if(mid>=d):
        seg[ho+e].count=seg[a].count+1
        seg[ho+e].le=ho+e+1
        seg[ho+e].ri=seg[a].ri
        update(seg[a].le,b,mid,d,e+1)
    else:
        seg[ho+e].count=seg[a].count+1
        seg[ho+e].le=seg[a].le
        seg[ho+e].ri=ho+e+1
        update(seg[a].ri,mid+1,c,d,e+1)

def query(a,b,c,d,e):
    if(d==c):
        return c
    mid=(c+d)//2
    tmp=seg[seg[b].le].count-seg[seg[a].le].count
    if(tmp>=e):
        return query(seg[a].le,seg[b].le,c,mid,e)
    else:
        return query(seg[a].ri,seg[b].ri,mid+1,d,e-tmp)


x=stdin.readline().split()
a=[int(i) for i in stdin.readline().split()]
le=len(a)
b=sorted(a)
c=[]
ho=2**(ceil(log(le,2))+1)-1
bo=ceil(log(le,2))+1
lo=ho+1
for i in a:
    c.append(bisect_left(b,i)+1)
seg=[Node(0,0,0) for _ in  range(lo)]
seg+=[Node(0,0,0) for _ in range(bo*le)]
make(1,1,le)
update(1,1,le,c[0],1)
ho+=bo
for i in c[1:]:
    update(ho-bo+1,1,le,i,1)
    ho+=bo
for _ in range(int(x[1])):
    inp=[int(i) for i in stdin.readline().split()]
    if(inp[0]==1):
        tmp=1
    else:
        tmp=lo+bo*(inp[0]-2)
    stdout.write(str(b[query(tmp,lo+bo*(inp[1]-1),1,le,inp[2])-1])+'\n')
