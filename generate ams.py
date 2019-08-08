n,k=map(int,input().split())
for i in range(n,k):
  n=i
  s=0
  while(n>0):
    r=n%10
    s=s+(r**3)
    n=n//10
  if(s==i):
    print(i,end=" ")    
