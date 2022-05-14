import json
s={}
s_name=input("enter your name: ")
with open("A.json","r") as A:
    fA = json.load(A)
with open("Q.json","r") as Q:
    fQ = json.load(Q)
stanswer=[]
for key,value in fQ.items():
    print(key)
    print(value)
    answer=input("enter answer")
    stanswer.append(answer)
x=0
for i in range(0,20):
    if stanswer[i]==fA[i]:
        x+=1
s[s_name]=count
print("the reselt " + str(x))
with open("save.json","w") as save:
    fm = json.dumps(s)
    save.write(fm)