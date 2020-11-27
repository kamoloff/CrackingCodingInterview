"""
Given an array of positive numbers and a positive number ‘S’, find 
the length of the smallest contiguous subarray whose sum is greater 
than or equal to ‘S’. Return 0, if no such subarray exists.
"""

def smallest_subarray_with_given_sum(arr: list, s: int) -> int:
    _s, start, result = 0, 0, float('inf')
    for i, x in enumerate(arr):
        _s += x
        while _s >= s:
            result = min(result, i+1-start)
            _s -= arr[start]
            start+=1

    return result if result != float('inf') else 0




if __name__ == '__main__':
    arr = [1, 3, 2, 6, 3, 4, 1, 8, 2]
    print(smallest_subarray_with_given_sum(arr, 141))