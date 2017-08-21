#插入排序
def insertSort(arr):
    length = len(arr)
    for i in range(1, length):
        for j in range(i):
            if arr[j]>arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


testlist = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 100]
sortList = insertSort(testlist)
print(sortList)