def bubbleSort(lis):
    n = len(lis)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lis[j] > lis[j + 1]:
                swapped = True
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
         
        if not swapped:
            return
lis =list(map(int ,input().split()))
 
bubbleSort(lis)
 
print("Sorted lisay is:")
for i in range(len(lis)):
    print("% d" % lis[i], end=" ")