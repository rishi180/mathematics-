from cmath import pi, sin
def function(x):
    return (sin(x)).real
n=int(input("enter no. of intervals "))
upper=pi
lower=0
h=(upper-lower)/n
arr=[]
for i in range(n):
    arr.append(function(lower))
    lower+=h
sum3=0
for i in range(3,n-1,3):
    sum3+=arr[i]
sum=0
for i in range(1,n-1):
    if i%3!=0:
        sum+=arr[i]
ans=3*h*(arr[0]+arr[5]+2*(sum3)+3*(sum))/8
print(ans)