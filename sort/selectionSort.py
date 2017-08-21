#选择排序算法
def selectionSort(arr):
    length = len(arr)
    for i in range(length-1):
        min_index = i
        for j in range(i+1, length):
            if arr[min_index] > arr[j]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

testlist = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
sortList = selectionSort(testlist)
print(sortList)