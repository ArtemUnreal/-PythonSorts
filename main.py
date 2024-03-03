


#5 3 9 1 4 2 8 7
#3 1 4 2   1 2 3 4
#9 8 7     7 8 9
#1 2 3 4 5 7 8 9

#[5, 1,2]
#[1,2]
#[]

def quickSort(arr:[int]) -> [int]:
    if len(arr) == 0:
        return arr
    arr1 = []
    arr2 = []
    first = arr[0]
    first_count = 0
    for i in range(len(arr)):
        if first > arr[i]:
             arr1.append(arr[i])
        if first < arr[i]:
             arr2.append(arr[i])
        if first == arr[i]:
            first_count += 1

    arr1 = quickSort(arr1)
    arr2 = quickSort(arr2)
    #arr1.append(first)
    res = arr1 + [first]*first_count + arr2

    return res


arr = [5, 3, 9, 1, 4, 2, 8, 7, 1, 1]

sorted_arr = quickSort(arr)

print(sorted_arr)

# Scala, Clojure, Erlang
# reverse(reverse(x))==x


#5 8 1 0 6 2 8 3 7
#5 8 1 0   
#6 2 8 3 7  
#0 1 2 3 5 6 7 8 8


def merge(arr1:[int], arr2:[int]) -> [int]:
    res = []
    while (len(arr1) != 0 and len(arr2) != 0):

        if arr1[0] < arr2[0]:
            res += [arr1[0]]
            del arr1[0]
        else:
            res += [arr2[0]]
            del arr2[0]

    res = res + arr1 + arr2 
    return res 


def mergeSort(arr:[int])->[int]:
    if len(arr) == 0 or len(arr) == 1:
        return arr

    size = len(arr)
    i = int(size / 2)
    arr1 = arr[:i]
    arr2 = arr[i:]

    arr1 = mergeSort(arr1)
    arr2 = mergeSort(arr2)
    
    res = merge(arr1, arr2)
    return res

#arr1 = [0, 1, 5, 8]
#arr2 = [2, 3, 6, 7, 8]

#res = merge(arr1, arr2)
arr = [2, 0, 3, 1, 6, 5, 8, 7, 8]

arr = mergeSort(arr)

print(arr)



