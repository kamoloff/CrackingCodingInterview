"""
Given a string with lowercase letters only, if you are allowed to replace 
no more than ‘k’ letters with any letter, find the length of the longest 
substring having the same letters after replacement.
"""


def longest_substring_with_same_letters_after_replacement(s: str,
                                                          k: int) -> int:
    max_freq, left, res = 0, 0, 0
    freqs = {}

    for i, c in enumerate(s):
        freqs[c] = freqs.get(c, 0) + 1
        max_freq = max(max_freq, freqs[c])

        # if substring length > max_repeating_char_count + k
        # then we need to remove chars from left to shrink
        # cause we are not allowed to replace more than k chars
        if i - left + 1 - max_freq > k:
            freqs[s[left]] -= 1
            left += 1

        res = max(res, i - left + 1)

    return res


if __name__ == '__main__':
    print(longest_substring_with_same_letters_after_replacement("aabccbb", 2))
    print(longest_substring_with_same_letters_after_replacement("abbcb", 1))
    print(longest_substring_with_same_letters_after_replacement("abccde", 1))
