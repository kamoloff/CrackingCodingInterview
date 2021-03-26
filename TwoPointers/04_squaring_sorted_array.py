def squaring_sorted_array(arr):
    left, right = 0, len(arr) - 1
    index = right
    result = [0 for _ in range(right + 1)]

    while index >= 0:
        if abs(arr[left]) > abs(arr[right]):
            result[index] = arr[left] * arr[left]
            left += 1
        else:
            result[index] = arr[right] * arr[right]
            right -= 1
        index -= 1
    return result


if __name__ == '__main__':
    print(squaring_sorted_array([]))
    print(squaring_sorted_array([-2, -1, 0, 2, 3]))
    print(squaring_sorted_array([-3, -1, 0, 1, 2]))
    print(squaring_sorted_array([2, 2, 2, 3, 4, 6]))
