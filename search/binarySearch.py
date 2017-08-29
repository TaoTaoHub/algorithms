#二分查找
def binarySearch(arr, value, l, r):
    if l >= r:
        if arr[l] == value:
            return l
        else:
            return -1
    m = (l + r)//2
    if arr[m] == value:
        return m
    elif arr[m] > value:
        return binarySearch(arr, value, l, m - 1)
    else:
        return binarySearch(arr, value, m + 1, r)
    
testlist = [1,2,4,6,7,8,9,10,22,34]
result = binarySearch(testlist, 5, 0, len(testlist))
print(result)
