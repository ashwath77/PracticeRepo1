#1 Find the sum of the second largest number in a sub-list => Input = [[1, 2, 3], [2, 4, 1, 0]] Output = 2+2 = 4

Input = [[1, 2, 3], [2, 4, 1, 0]]
l=[]
l1=[]
sum=0
for i in Input:
    i.sort(reverse=True)
    l.append(i[0])
    l1.append(i[1])
    sum+=i[1]
print("First element in sublist: ",l)
print("Second element in sublist: ",l1)
print("sum of the second largest",sum)