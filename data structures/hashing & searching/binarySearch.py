import snoop
import math

'''def binary(array ,value):
    start=0
    end=len(array)-1
    mid=math.floor((start+end)/2)
    print(start,mid,end)
    print(array[start],array[mid],array[end])
    while not(array[mid]==value) and start<=end:
        if value< array[mid]:
            end=mid-1
            print(array[end])
        else:
            start=mid+1
        mid=math.floor((start+end)/2)
        print(start,mid,end)
        print(array[start],array[mid],array[end])
    if array[mid]==value:
        return mid
    else:
        return -1
    
   
Carray=[1,2,3,4,5,6,7,8,9,10]
print(binary(Carray,8)) '''
    























    

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1
        
arr = [2, 3, 4, 10, 40]
x = 10

result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")