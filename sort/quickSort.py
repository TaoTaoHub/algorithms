#快速排序
def quickSort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    target = int(length/2)
    left = []
    right = []
    for i in range(length):
        if i != target:
            if arr[i] <= arr[target]:
                left.append(arr[i])
            else:
                right.append(arr[i])

    return quickSort(left)+[arr[target]]+quickSort(right)

testlist = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
sortList = quickSort(testlist)
print(sortList)
