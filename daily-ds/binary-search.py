def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:  # use <= so it checks the last element too
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

def verify(index):  # pass index as parameter
    if index is not None:
        print("Target found at index", index)
    else:
        print("Target not found")

numbers = [x + 1 for x in range(20)]  # [1, 2, ..., 20]
res = binary_search(numbers, 12)
verify(res)
