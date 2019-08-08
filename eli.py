a,b,c=list(map(str,input().split()))
z=int(c)
q=len(a)
s=0
for i in range(0,q):
  if(a[i]!=b[i]):
    s=s+1
if(z==s):
  print("yes")
else:
  print("no")   
