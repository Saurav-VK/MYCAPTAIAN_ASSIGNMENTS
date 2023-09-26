n=int(input("Enter the number of terms in the fibonacci series: "))
i=1
a=0
b=1
print(a)
print(b)
while i<=n:
    c=a+b
    print(c)
    a=b
    b=c
    i=i+1