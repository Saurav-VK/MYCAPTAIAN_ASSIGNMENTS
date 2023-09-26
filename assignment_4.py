inp=input("Enter a word: ")
d={}
max=1
for i in inp:
    if i in d:
        d[i]=d[i]+1
    else:
       d[i]=1
sorted_freq = sorted(d.items(), key=lambda x: x[1], reverse=True)
for letter, freq in sorted_freq:
    print(f"{letter}: {freq}")





