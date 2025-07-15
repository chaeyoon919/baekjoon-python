lst=[]
for i in range(1, 10):
	n = int(input())
	lst.append(n)

print(max(lst))
print(lst.index(max(lst))+1)
