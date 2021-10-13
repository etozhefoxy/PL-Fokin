a=int(input())
s1=1
s2=1
s3=0
for i in range(3,a+1):
    s3=s1+s2
    s1=s2
    s2=s3
print(s3)
