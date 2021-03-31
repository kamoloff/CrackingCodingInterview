def dutch_national_flag(nums):
    i, low, high = 0, 0, len(nums) - 1

    while i <= high:
        if nums[i] == 0:
            nums[i], nums[low] = nums[low], nums[i]
            i += 1
            low += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[i], nums[high] = nums[high], nums[i]
            high -= 1

    return nums


if __name__ == '__main__':
    print(dutch_national_flag([0, 2, 0, 1, 1, 1, 2, 0, 0, 2]))
    print(dutch_national_flag([1, 0, 2, 1, 1, 1, 2, 0]))
    print(dutch_national_flag([1, 0, 2, 1, 0]))
    print(dutch_national_flag([2, 2, 0, 1, 2, 0]))
