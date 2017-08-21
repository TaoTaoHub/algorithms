#插入排序
def insertSort(arr):
    length = len(arr)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


testlist = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 0]
sortList = insertSort(testlist)
print(sortList)