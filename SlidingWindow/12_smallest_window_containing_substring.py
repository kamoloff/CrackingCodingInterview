from collections import Counter


def validate(cnt: dict, cnt2: dict):
    for key in cnt.keys():
        if key not in cnt2 or cnt2[key] < cnt[key]:
            return False
    return True


def smallest_window_containing_substring(s: str, t: str):
    res = ""
    cnt = Counter(t)
    cnt2 = {}
    st, i = 0, 0
    while i < len(s) and st < len(s):
        cnt2[s[i]] = cnt2.get(s[i], 0) + 1

        if validate(cnt, cnt2):
            if res == "" or len(res) > i + 1 - st:
                res = s[st:i + 1]
            startChar = s[st]
            if startChar not in cnt or cnt2[startChar] > cnt[startChar]:
                cnt2[startChar] -= 1
                cnt2[s[i]] -= 1
                st += 1
                i -= 1
        i += 1
    return res


if __name__ == '__main__':
    print(smallest_window_containing_substring("aabdec", "abc"))
    print(smallest_window_containing_substring("abdabca", "abc"))
    print(smallest_window_containing_substring("adcad", "abc"))

