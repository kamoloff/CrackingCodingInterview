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


if __name__ == '__main__':
    print(quadruple_sum([4, 1, 2, -1, 1, -3], 1))
    print(quadruple_sum([2, 0, -1, 1, -2, 2], 2))
