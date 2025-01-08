ls = [1, 2, 3, 4, 5, 6, 7, 8]
odd_ls = []
even_ls = []
# d = {}
c = 0
for i in ls:
    if i % 2 == 0:
        even_ls.append(i)
    else:
        odd_ls.append(i)
# for i in odd_ls:
#     for j in range(0, len(even_ls)-1):
#         d[i] = even_ls[j+c]
#         c += 1
#         break
d = {k: v for k, v in zip(odd_ls, even_ls)}
print(d)


def dic_merge(ls1):
    odd_ls1 = []
    even_ls1 = []
    for i in ls1:
        if i % 2 == 0:
            even_ls1.append(i)
        else:
            odd_ls1.append(i)

    d1 = {k: v for k, v in zip(odd_ls1, even_ls1)}
    print(d1)


dic_merge([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

numbers = [1, 2, 2, 3, 4, 4, 5, 6]
unique_list = []
d = {}
for num in numbers:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1
for k, v in d.items():
    if v == 1:
        unique_list.append(k)
print(unique_list)
