def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n-1):  # Outer loop just presents the number of traversals needed
        for j in range(n-1):  # Inner loop to traverse the array and compare elements
            if arr[j] > arr[j+1]:  # Compare the adjacent elements
                swap_basic(arr, j, j+1)  # Swap if the element found is greater than the next element
                # swap_advanced(arr, j, j+1)  # Alternative swap method using tuple unpacking
    return arr  # Return the sorted array

def swap_advanced(arr, i, j):
    """Proffesoner using tuple unpacking"""
    arr[i], arr[j] = arr[j], arr[i]  # Swap elements using tuple unpacking
    return arr  # Return the array (not necessary, but included for consistency)

def swap_basic(arr, i, j):
    """Beginner-friendly swap method using a temporary variable"""
    temp = arr[i]  # Store the value of arr[i] in a temporary variable
    arr[i] = arr[j]  # Assign the value of arr[j] to arr[i]
    arr[j] = temp  # Assign the value stored in temp to arr[j]
    return arr  # Return the array (not necessary, but included for consistency)

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]  # Example array to be sorted
    sorted_arr = bubble_sort(arr)  # Call the bubble_sort function
    print("Sorted array is:", sorted_arr)  # Print the sorted array