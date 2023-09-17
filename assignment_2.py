a=input("Input the Filename: ")
b=a.index(".")
if(a[b:]==".py"):
    print('The extension of the file is: \'python\'')
else:
    print("The extension is not python")