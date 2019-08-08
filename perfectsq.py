x,y=map(int,input().split())
s=0
for n in range(x,(y+1)):
  a=(n)**0.5
  if(n%a==0):
    s=s+1
print(s)    
