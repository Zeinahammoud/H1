dec_num=int(input("enter a decimal nimber: "))
bin_num=[]
x=""
while dec_num!=0:
    y= dec_num % 2
    bin_num.append(y)
    dec_num= dec_num // 2
bin_num.reverse()
for i in bin_num:
    x=x+str(i)
print("the binary number of the " +x)