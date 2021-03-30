def triplets_with_smaller_sum(nums, target):
    nums.sort()
    count, sz = 0, len(nums)
    for index in range(sz - 2):
        left, right = index + 1, sz - 1
        while left < right:
            _sum = nums[index] + nums[left] + nums[right]
            if _sum < target:
                count += (right - left)
                left += 1
            else:
                right -= 1

    return count


if __name__ == '__main__':
    print(triplets_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5))
    print(triplets_with_smaller_sum([1, 0, 1, 1], 100))
