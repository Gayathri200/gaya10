s=int(input())
x=map(int,input().split())
a=list(x)
c=sorted(a)
b=len(c)
if(b==s):
  for i in range(1,b):
    print(c[i],end=" ")
