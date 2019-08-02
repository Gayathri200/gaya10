x=input()
n=len(x)
for i in range(0,n):
  if(i==0):
    a=x[i]
    i=i+1
    c=x[i]
    w=(c+a)
  if(i==2):
    e=x[i]
    i=i+1
    f=x[i]
    z=(f+e)
    print(w+z)   
