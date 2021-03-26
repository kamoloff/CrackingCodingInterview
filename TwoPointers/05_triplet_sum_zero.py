def triplet_sum_zero(arr):
    triplets = []
    arr.sort()
    arr_len = len(arr)
    for i in range(arr_len - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        two_sum(arr, -arr[i], i + 1, arr_len - 1, triplets)

    return triplets


def two_sum(arr, target, left, right, triplets):
    while left < right:
        _sum = arr[left] + arr[right]
        if _sum == target:
            triplets.append([-target, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif _sum > target:
            right -= 1
        else:
            left += 1


if __name__ == '__main__':
    print(triplet_sum_zero([]))
    print(triplet_sum_zero([-2, -1, 0, 2, 3]))
    print(triplet_sum_zero([-3, -1, 0, 1, 2]))
    print(triplet_sum_zero([-5, 2, -1, -2, 3]))
    print(triplet_sum_zero([-3, 0, 1, 2, -1, 1, -2]))
    print(triplet_sum_zero([-1, 0, 1, 2, -1, -4]))
