def triplet_closest_sum(arr, target):
    result = float('inf')
    arr.sort()
    arr_len = len(arr)
    for i in range(arr_len - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        left, right = i + 1, arr_len - 1

        while left < right:
            _sum = arr[i] + arr[left] + arr[right]
            if abs(_sum - target) < abs(result - target):
                result = _sum
            if abs(_sum - target) == abs(result - target) and _sum < result:
                result = _sum
            if _sum == target:
                return target
            elif _sum > target:
                right -= 1
            else:
                left += 1

    return result


if __name__ == '__main__':
    print(triplet_closest_sum([-2, 0, 1, 2], 2))
    print(triplet_closest_sum([-3, -1, 1, 2], 1))
    print(triplet_closest_sum([1, 0, 1, 1], 100))
