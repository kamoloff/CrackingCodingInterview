"""
Given an array of positive numbers and a positive number ‘k’, 
find the maximum sum of any contiguous subarray of size ‘k’.
"""

def max_sum_subarray_size_k(arr: list, k: int):
    res = float('-inf')
    _sum = 0
    for i in range(len(arr)):
        _sum += arr[i]
        if i >= k-1:
            res = max(res, _sum)
            _sum -= arr[i+1-k]
    return res


if __name__ == '__main__':
    arr = [1,7,3,5,9,3,-3,11,1,-5,6]
    print(max_sum_subarray_size_k(arr, 4))