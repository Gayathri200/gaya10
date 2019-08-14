x,y=map(int,input().split())
s=map(int,input().split())
a=list(s)
b=len(a)
r=0
if(x==b):
  for i in range(0,b):
    if(a[i]!=y):
      print(a[i],end=" ")
    elif(a[i]==y):
      r=r+1
      if(r==x):
        print('empty')  
