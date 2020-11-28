"""
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
"""

def average_k(arr: list, k: int) -> list:
    s = sum(arr[:k])
    res = [s/k]
    for i in range(k, len(arr)):
        s += arr[i] - arr[i-k]
        res.append(s / k)
    return res


if __name__ == '__main__':
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    print(average_k(arr, 4))