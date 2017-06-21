from math import ceil,log
import bisect
from sys import stdin,stdout
def tree(a,b,c):
    if(b==c):
        seg[a]=[lol[b-1]]
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
    if(b>c or d>c or b>e):
        return 0
    if(d<=b and c<=e):
        ans=bisect.bisect(seg[a],f)
        return ans
    mid=(b+c)//2
    tmp=2*a
    return query(tmp,b,mid,d,e,f)+query(tmp+1,mid+1,c,d,e,f)
def wrapper(a,b,c,d):
    lo=1
    hi=a
    while(lo<=hi):
        mid=(lo+hi)//2
        ans=query(1,1,a,b,c,mid)
        if(ans>=d):
            ans1=mid
            hi=mid-1
        else:
            lo=mid+1
    return ans1-1
x=stdin.readline().split()
ele=[int(i) for i in stdin.readline().split()]
ele1=sorted(ele)
lol=[]
le=len(ele)
for i in ele:
    lol.append(bisect.bisect_left(ele1,i)+1)
seg=[[]]*(2**(ceil(log(le,2))+1))
tree(1,1,le)
for _ in range(int(x[1])):
    inp=[int(i) for i in stdin.readline().split()]
    stdout.write(str(ele1[wrapper(le,inp[0],inp[1],inp[2])])+'\n')
