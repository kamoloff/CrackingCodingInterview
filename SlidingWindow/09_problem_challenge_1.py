"""
Given a string and a pattern, find out if the string 
contains any permutation of the pattern.
"""
import collections

def problem_challenge_1(s: str, t: str):
    if len(s) < len(t): 
        return False
    cnt1 = collections.Counter(s[:len(t)-1])
    cnt2 = collections.Counter(t)

    left = 0
    for i in range(len(t)-1, len(s)):
        valid = True
        cnt1[s[i]] = cnt1.get(s[i], 0) + 1
        for x in cnt2.keys():
            if x not in cnt1 or cnt1[x] < cnt2[x]:
                valid = False
                break
        cnt1[s[left]] -= 1
        left += 1
        if valid:
            return True
    return False    

# Note: s and t are swapped here
def problem_challenge_1_optimized(t: str, s: str) -> bool:
        t, s = s, t
        if len(s) < len(t): 
            return False
        
        c1, c2 = [0]*26, [0]*26
        for i in range(len(t)):
            c1[ord(t[i])-ord('a')]+=1
            c2[ord(s[i])-ord('a')]+=1
        
        same = 0
        
        for i in range(26):
            if c1[i] == c2[i]:
                same += 1
        
        for i in range(len(s) - len(t)):
            
            l, r = ord(s[i]) - ord('a'), ord(s[i+len(t)])-ord('a')
            if same == 26: return True
            c2[r] += 1
            if c2[r] == c1[r]: same += 1
            elif c2[r] == c1[r] + 1: same -= 1
            c2[l] -= 1
            if c2[l] == c1[l]: same += 1
            if c2[l] == c1[l] - 1: same -= 1
        
        return same == 26


if __name__ == '__main__':
    print(problem_challenge_1("oidbcaf", "abc"))
    print(problem_challenge_1("odicf", "dc"))
    print(problem_challenge_1("bcdxabcdy", "bcdyabcdx"))
    print(problem_challenge_1("aaacb", "abc"))

    print(problem_challenge_1_optimized("oidbcaf", "abc"))
    print(problem_challenge_1_optimized("odicf", "dc"))
    print(problem_challenge_1_optimized("bcdxabcdy", "bcdyabcdx"))
    print(problem_challenge_1_optimized("aaacb", "abc"))