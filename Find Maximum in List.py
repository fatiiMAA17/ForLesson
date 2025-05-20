def find_max(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    return max(arr[index], find_max(arr, index + 1))
