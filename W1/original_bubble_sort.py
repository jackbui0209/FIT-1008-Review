def original_selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        smallest_pos = find_smallest(arr, i)
        if 
        swap_basic(arr, i, smallest_pos)#find in buuble_sort
    return arr

def find_smallest(arr, start):
    smallest_pos = start
    for i in range(start+1, len(arr)):
        if arr[i] < arr[smallest_pos]:
            smallest_pos = i
    return smallest_pos

def swap_advanced(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

def swap_basic(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = original_selection_sort(arr)
    print("Sorted array is:", sorted_arr)
