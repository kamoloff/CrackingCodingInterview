"""
Given two strings containing backspaces (identified by the character ‘#’),
check if the two strings are equal.
"""


def comparing_strings_containing_backspaces(s1, s2):
    stack1, stack2 = [], []
    for c in s1:
        if c == '#' and stack1:
            stack1.pop()
        else:
            stack1.append(c)

    for c in s2:
        if c == '#' and stack2:
            stack2.pop()
        else:
            stack2.append(c)
    return stack1 == stack2


if __name__ == '__main__':
    print(comparing_strings_containing_backspaces('xzz#', 'xy#z'))
    print(comparing_strings_containing_backspaces('xy#z', 'xyz#'))
    print(comparing_strings_containing_backspaces('xp#', 'xyz##'))
    print(comparing_strings_containing_backspaces('xywrrmp', 'xywrrmu#p'))
