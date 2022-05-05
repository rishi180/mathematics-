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
sum2=0
for i in range(2,n-1,2):
    sum2+=arr[i]
sum3=0
for i in range(1,n-1,2):
    sum3+=arr[i]
ans=h*(arr[0]+arr[5]+2*(sum2)+4*(sum3))/3
print(ans)