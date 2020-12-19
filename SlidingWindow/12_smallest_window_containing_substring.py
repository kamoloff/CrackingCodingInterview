from collections import Counter


def smallest_window_containing_substring(s: str, t: str):
    freqs, left = Counter(t), len(t)
    start, end = 0, 0
    i = 0
    for j, c in enumerate(s, 1):
        left -= 1 if freqs[c] > 0 else 0
        freqs[c] -= 1

        if not left:
            while i < j and freqs[s[i]] < 0:
                freqs[s[i]] += 1
                i += 1
            if not end or end - start >= j - i:
                start, end = i, j

    return s[start: end]


if __name__ == '__main__':
    print(smallest_window_containing_substring("aabdec", "abc"))
    print(smallest_window_containing_substring("abdabca", "abc"))
    print(smallest_window_containing_substring("adcad", "abc"))

