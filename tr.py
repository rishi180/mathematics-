from cmath import pi, sin
def function(x):
    return (sin(x)).real
n=int(input("enter the no of interval "))
upper=pi
lower=0
h=(upper-lower)/n
arr=[]
for i in range(n):
    arr.append(function(lower))
    lower+=h
sum=0
for i in range(1,n-1):
    sum+=arr[i]
ans=h*((arr[0]+arr[n-1])+2*(sum))/2
print(ans)