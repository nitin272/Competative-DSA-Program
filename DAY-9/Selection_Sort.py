def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])

size = int(input())
data = list(map(int, input().split()))[:size]

selectionSort(data, size)
print('')
print(" ".join(map(str, data)))
