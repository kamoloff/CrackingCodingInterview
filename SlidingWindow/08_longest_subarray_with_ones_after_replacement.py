"""
Given an array containing 0s and 1s, if you are allowed to replace no more 
than ‘k’ 0s with 1s, find the length of the longest contiguous 
subarray having all 1s
"""


def longest_subarray_with_ones_after_replacement(arr: list, k: int) -> int:
    max_freq, left, res = 0,0,0
    cnt = 0

    for i,x in enumerate(arr):
        if x == 1:
            cnt += 1

        if i - left + 1 - cnt > k:
            if arr[left] == 1:
                cnt -= 1
            left += 1
        
        res = max(res, i - left + 1)
    
    return res


if __name__ == '__main__':
    print(longest_subarray_with_ones_after_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(longest_subarray_with_ones_after_replacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))