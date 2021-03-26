def pair_with_target_sum(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == target:
            return [left, right]
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            left += 1

    return [-1, -1]


if __name__ == '__main__':
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum([2, 5, 9, 11], 11))
    print(pair_with_target_sum([2, 5, 9, 11], 23))
    print(pair_with_target_sum([3, 5, 6, 11], 2))
