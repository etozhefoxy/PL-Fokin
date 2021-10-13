n=int(input())
k=int(input())
s1=1
s2=1
s3=0
sum=0
for i in range(3,n+1):
    if i<=k:
       s3=s1+s2
    sum=s1+s2
    s1=s2
    s2=sum
print(sum+s3)
