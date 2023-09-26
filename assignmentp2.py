a=input('Enter the list elements with a spaace in between each element: ')
b=a.split()
l=[]
ln=[]
for i in b:
    l.append(i)
for e in l:
    if int(e)<0:
        ln.append(e)
print('The negative elements are:\n')
print(ln)


