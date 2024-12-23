# A utility function to print an array
def print_array(arr):
    for num in arr:
        print (num)

# A utility function to get the digit at index d in an integer
def digit_at(x, d):
    return (x // (10 ** (d - 1))) % 10

# The main function to sort array using MSD Radix Sort recursively
def MSD_sort(arr, lo, hi, d):
    # Recursion break condition
    if hi <= lo:
        return

    count = [0] * (10 + 2)
    temp = {}

    # Store occurrences of most significant character from each integer in count[]
    for i in range(lo, hi + 1):
        c = digit_at(arr[i], d)
        count[c] += 1

    # Change count[] so that count[] now contains actual position of these digits in temp[]
    for r in range(10 + 1):
        count[r + 1] += count[r]

    # Build the temp
    for i in range(lo, hi + 1):
        c = digit_at(arr[i], d)
        temp[count[c + 1]] = arr[i]
        count[c + 1] += 1

    # Copy all integers of temp to arr[], so that arr[] now contains partially sorted integers
    for i in range(lo, hi + 1):
        arr[i] = temp.get(i - lo + 1, 0)

    # Recursively MSD_sort() on each partially sorted integers set to sort them by their next digit
    for r in range(10):
        MSD_sort(arr, lo + count[r], lo + count[r + 1] - 1, d - 1)

# Function to find the largest integer
def getMax(arr):
    mx = arr[0]
    for num in arr:
        if num > mx:
            mx = num
    return mx

# Main function to call MSD_sort
def radixsort(arr):
    # Find the maximum number to know the number of digits
    m = getMax(arr)

    # Get the length of the largest integer
    d = len(str(abs(m)))

    # Function call
    MSD_sort(arr, 0, len(arr) - 1, d)

# Driver Code
if __name__ == "__main__":
    # Input array
    arr = [9330, 9950, 718, 8977, 6790, 95, 9807, 741, 8586, 5710]

    print ("Unsorted array:")
    print_array(arr)

    # Function Call
    radixsort(arr)

    print ("Sorted array:")
    print_array(arr)