# TO-DO: complete the helpe function below to merge 2 sorted leftys
def merge( left, right ):
        merged_arr = []
        while len(left) > 0 and len(right) > 0 :
            if left[0] < right[0]:
                merged_arr.append(left[0])
                left.remove(left[0])
            else:
                merged_arr.append(right[0])
                right.remove(right[0])
        while len(left) > 0:
            merged_arr.append(left[0])
            left.remove(left[0])
        while len(right) > 0:
            merged_arr.append(right[0])
            right.remove(right[0])

        return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    else:
        mid_list = len(arr) // 2
        left = merge_sort(arr[:mid_list])
        right = merge_sort(arr[mid_list:])
        arr = merge(left, right)
        return arr

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
