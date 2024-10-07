def removeDuplicates(array):
    if not array:
        return 0

    i = 0
    for j in range(1, len(array)):
        if array[j] != array[i]:
            i += 1
            array[i] = array[j]

    return i + 1

# Example with hardcoded input for video or demo
arr = [1, 1, 2, 2, 3, 4, 4, 5]
length = removeDuplicates(arr)
print("Array after removing duplicates:", arr[:length])
print("Length of array after removing duplicates:", length)
