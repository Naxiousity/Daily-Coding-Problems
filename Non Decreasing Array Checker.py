###
#  Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.
# For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.
# Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
###

# Function that returns true if the array
# can be made strictly decreasing
# with at most one change
def check(arr, n):
 
    modify = 0
     
    # Check whether the last element needs
    # to be modify or not
    if (arr[n - 1] >= arr[n - 2]):
        arr[n-1] = arr[n-2] - 1
        modify += 1
     
    # Check whether the first element needs
    # to be modify or not
    if (arr[0] <= arr[1]):
        arr[0] = arr[1] + 1
        modify += 1
 
    # Loop from 2nd element to the 2nd last element
    for i in range(n-2, 0, -1):
 
        # Check whether arr[i] needs to be modified
        if (arr[i - 1] <= arr[i] and arr[i + 1] <= arr[i]) or \
        (arr[i - 1] >= arr[i] and arr[i + 1] >= arr[i]):
 
            # Modifying arr[i]
            arr[i] = (arr[i - 1] + arr[i + 1]) // 2
            modify += 1
             
            # Check if arr[i] is equal to any of
            # arr[i-1] or arr[i + 1]
            if (arr[i] == arr[i - 1] or arr[i] == arr[i + 1]):
                return False
 
 
    # If more than 1 modification is required
    if (modify > 1):
        return False
 
    return True
 
# Driver code
if __name__ == "__main__":
    arr = [10, 5, 11, 3]
    n = len(arr)
 
    if (check(arr, n)):
        print("Yes")
    else:
        print("No")