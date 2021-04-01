"""
Given an array of unsorted numbers and a target number,
find all unique quadruplets in it, whose sum is equal to the target number.
"""


def quadruple_sum(nums, target):
    def k_sum(arr, tar, k):
        res = []
        if len(arr) == 0 or arr[0] * k > tar or arr[-1] * k < tar:
            return res
        if k == 2:
            return two_sum(arr, tar)

        for i in range(len(arr)):
            if i == 0 or arr[i - 1] != arr[i]:
                for sub_res in k_sum(arr[i + 1:], tar - arr[i], k - 1):
                    res.append([arr[i]] + sub_res)

        return res

    def two_sum(arr, tar):
        res = []
        s = set()
        for i in range(len(arr)):
            if len(res) == 0 or res[-1][1] != arr[i]:
                if tar - arr[i] in s:
                    res.append([tar - arr[i], arr[i]])
            s.add(arr[i])
        return res

    nums.sort()
    return k_sum(nums, target, 4)


def four_sum(nums, target):
    def two_sum(arr, first, second, target, quadruplets):
        left = second + 1
        right = len(arr) - 1
        while left < right:
            _sum = arr[first] + arr[second] + arr[left] + arr[right]
            if _sum == target:
                quadruplets.append(
                    [arr[first], arr[second], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[left + 1]:
                    right -= 1
            elif _sum < target:
                left += 1
            else:
                right -= 1

    nums.sort()
    quadruplets = []
    sz = len(nums)

    for i in range(sz - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, sz - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            two_sum(nums, i, j, target, quadruplets)
    return quadruplets


if __name__ == '__main__':
    print(quadruple_sum([4, 1, 2, -1, 1, -3], 1))
    print(four_sum([4, 1, 2, -1, 1, -3], 1))
    print(quadruple_sum([2, 0, -1, 1, -2, 2], 2))
    print(four_sum([2, 0, -1, 1, -2, 2], 2))
