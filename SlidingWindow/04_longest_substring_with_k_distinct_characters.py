"""
Given a string, find the length of the longest substring in it with no 
more than K distinct characters.
"""
def longest_substring_with_k_distinct_characters(s: str, k: int) -> int:
    result = 0    
    freq = {}
    start = 0
    for i, c in enumerate(s):
        freq[c] = freq.get(c, 0) + 1
        while len(freq) > k:
            freq[s[start]] -= 1
            if freq[s[start]] == 0:
                del freq[s[start]]
            start += 1
        result = max(result, i-start+1) 

    return result


if __name__ == '__main__':
    print(longest_substring_with_k_distinct_characters("cbbebi", 3))
