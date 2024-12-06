a = [1,2,3,2,1,6,7,8,4,2]
mydict = {}

for i in a:
    # if i not in mydict:
    mydict[i] = a.count(i)

print(mydict)