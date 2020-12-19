"""
Given a string, find the length of the longest substring which has no repeating characters.
"""


def no_repeat_substring(s: str):
    def is_valid():
        for x in cnt.keys():
            if cnt[x] > 1:
                return False
        return True

    res, lef = 0, 0
    cnt = {}

    for i, c in enumerate(s):
        cnt[c] = cnt.get(c, 0) + 1
        while not is_valid():
            cnt[s[lef]] -= 1
            lef += 1
        res = max(i - lef + 1, res)

    return res


if __name__ == '__main__':
    print(no_repeat_substring("aabccbb"))
    print(no_repeat_substring("abbbb"))
    print(no_repeat_substring("abccde"))
