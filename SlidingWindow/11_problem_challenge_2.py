"""
Given a string and a pattern, find all anagrams of the pattern in the given string.
Anagram is actually a Permutation of a string. For example, “abc” has 
the following six anagrams:

1. abc
2. acb
3. bac
4. bca
5. cab
6. cba

Write a function to return a list of starting indices of the anagrams of the 
pattern in the given string.
"""


def problem_challenge_2(s: str, t: str) -> list:
    res  = []
    if len(s) < len(t): 
        return []
    
    c1, c2 = [0]*26, [0]*26
    for i in range(len(t)):
        c1[ord(t[i])-ord('a')]+=1
        c2[ord(s[i])-ord('a')]+=1
    
    same = 0
    
    for i in range(26):
        if c1[i] == c2[i]:
            same += 1
    i = 0

    for i in range(len(s) - len(t)):
        if same == 26:
            res.append(i)
        l, r = ord(s[i]) - ord('a'), ord(s[i+len(t)])-ord('a')
        c2[r] += 1
        if c2[r] == c1[r]: same += 1
        elif c2[r] == c1[r] + 1: same -= 1
        c2[l] -= 1
        if c2[l] == c1[l]: same += 1
        if c2[l] == c1[l] - 1: same -= 1

    if same == 26:
            res.append(i+1)
    return res


if __name__ == '__main__':
    
    print(problem_challenge_2("ppqp", "pq"))
    print(problem_challenge_2("abbcabc", "abc"))