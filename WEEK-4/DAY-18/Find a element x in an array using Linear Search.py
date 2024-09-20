def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

if __name__ == '__main__':
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))[:N]
    Target = int(input().strip())
    result = linear_search(arr, Target)
    print(result)
