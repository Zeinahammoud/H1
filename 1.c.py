L=["Network" , "Math" , "Programming", "Physics" , "Music"]
sp=[]
for i in L:
    if i[0] == 'P':
        sp.append(i)
x=len(sp)
print("there is " + str(x) +" start with p" + str(sp))