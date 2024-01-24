#1 Find the sum of the second largest number in a sub-list => Input = [[1, 2, 3], [2, 4, 1, 0]] Output = 2+2 = 4

Input = [[1, 2, 3], [2, 4, 1, 0]]
sum=0
for i in Input:
    i.sort(reverse=True)
    sum+=i[1]
print("sum of the second largest",sum)