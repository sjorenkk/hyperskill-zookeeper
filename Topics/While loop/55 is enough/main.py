n = 0
lim = 55
num_list = []
while n != lim:
    n = int(input())
    num_list.append(n)
num_list.remove(lim)
print(len(num_list))
print(sum(num_list))
print(round(sum(num_list) / len(num_list)))
