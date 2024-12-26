a = [1,2,3,4,5,6,7]


def binary_search(a,target):
    i,j = 0,len(a)-1

    while i<=j:
        mid = (i + j)// 2
        if a[mid] == target:
            return mid
        elif a[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    return -1

print(binary_search(a,10))