# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i+1, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x
        # TO-DO: swap
        if smallest_index != i:
            arr[smallest_index], arr[i] = arr[i], arr[smallest_index]               
    return arr

print(selection_sort([5, 1, 3, 7, 9, 2, 4, 6]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr