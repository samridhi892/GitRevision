
list_1 = [1,2,3,3,3,4,4,4,5,5,6]
new_list = []
ct = 0
d = {}
for i in set(list_1):
    print(f"{i} occurs {list_1.count(i)} times")

#Another method
for num in list_1:
    if num in d:
        d[num]+=1
    else:
        d[num]=1

print(d)
for k,v in d.items():
    print(f"{k} occurs {v} times")




