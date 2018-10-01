"""
Recursive approach for merge sort.
Merge sort is based on divide and conquer approach
Steps:-
 - Divide the array in two parts recursively
 - Merge arrays in order
 - Return the result
"""


def merge(left_array, right_array):
    """
    1. Compare first element of both arrays and append the smaller element
    2. Increment the index for the array whose element has been pushed to merged array
    3. Follow steps 1 and 2 till either of two array is completely merged
    4. Whichever array has remaining elements merge that directly as that is already sorted.
    :param left_array: one part of array
    :param right_array: other part of array
    :return: merged_array in sorted form
    """
    left_n = len(left_array)
    right_n = len(right_array)
    i = 0
    j = 0
    merged_array = list()
    while True:
        if left_array[i] <= right_array[j]:
            merged_array.append(left_array[i])
            i += 1
        else:
            merged_array.append(right_array[j])
            j += 1
        if i == left_n:
            merged_array += right_array[j:right_n]
            break
        elif j == right_n:
            merged_array += left_array[i:left_n]
            break
    return merged_array


def merge_sort(arr):
    """
    1. Divide array in two parts recursively till there is only one element remaining in array
    2. Call merge routine for two arrays
    :param arr: An array to be sorted
    :return: sorted array
    """
    n = len(arr)
    if n == 1:
        return arr
    m = n//2
    left_array = merge_sort(arr[0:m])
    right_array = merge_sort(arr[m:n])
    new_array = merge(left_array, right_array)
    return new_array

if __name__ == "__main__":
    unsorted_array = [1, 2, 3, 6, 5, 6, 7, 8]
    sorted_array = merge_sort(unsorted_array)
    print(sorted_array)
