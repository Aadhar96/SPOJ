from bisect import bisect_left as b1
from bisect import bisect_right as b2
from math import log,ceil
from sys import stdin,stdout
def tree(a,b,c):
    if(b==c):
        seg[a]=[ele[b-1][1]]
        return
    mid=(b+c)//2
    tmp=2*a
    tree(tmp,b,mid)
    tree(tmp+1,mid+1,c)
    seg[a]=merge(seg[tmp],seg[tmp+1])
def merge(a,b):
    ans=[]
    i=0
    j=0
    flag=0
    lol1=len(a)-1
    lol2=len(b)-1
    while(True):
        if(i>lol1):
            flag=1
            break
        if(j>lol2):
            flag=2
            break
        if(a[i]<=b[j]):
            ans.append(a[i])
            i+=1
        else:
            ans.append(b[j])
            j+=1
    if(flag==1):
        ans+=b[j:]
        return ans
    if(flag==2):
        ans+=a[i:]
        return ans
def query(a,b,c,d,e,f):
    if(b==c):
        return tmp[seg[a][0]]
    tmp1=2*a
    mid=(b+c)//2
    lol=b2(seg[tmp1],e)-b1(seg[tmp1],d)
    if(lol>=f):
        return query(tmp1,b,mid,d,e,f)
    else:
        return query(tmp1+1,mid+1,c,d,e,f-lol)
x=stdin.readline().split()
tmp=stdin.readline().split()
le=len(tmp)
ele=[0]*le
for i in range(le):
    ele[i]=[int(tmp[i]),i]
ele.sort()
seg=[[]]*(2**(ceil(log(le,2))+1))
tree(1,1,le)
for _ in range(int(x[1])):
    inp=[int(i) for i in stdin.readline().split()]
    stdout.write(query(1,1,le,inp[0]-1,inp[1]-1,inp[2])+'\n')
