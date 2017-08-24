#归并排序
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    num = int(len(arr)/2)
    left = mergeSort(arr[:num])
    right = mergeSort(arr[num:])
    return merge(left, right)

def merge(left, right):
    l = len(left)
    r = len(right)
    i, j = 0, 0
    result = []
    while i<l and j<r:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result




testlist = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
sortList = mergeSort(testlist)
print(sortList)