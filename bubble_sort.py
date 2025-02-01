# bubble sort algorithms
def bubble_sort(arr):
    flag = True
    n = len(arr)
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                flag = True
                arr[i - 1], arr[i] = arr[i], arr[i - 1]


arr = [-5, 3, 2, 1, 2, -3, -3, 3, 7]
bubble_sort(arr)
print(arr)
