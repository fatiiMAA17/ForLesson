def product_list(arr):
    if not arr:
        return 1
    return arr[0] * product_list(arr[1:])
