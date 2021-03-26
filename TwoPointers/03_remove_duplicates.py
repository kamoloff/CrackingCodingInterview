def remove_duplicates(arr):
    dis, dup, sz = 0, 1, len(arr)
    if sz < 2:
        return sz
    while dup < sz:
        if arr[dis] != arr[dup]:
            dis += 1
            arr[dis] = arr[dup]
        dup += 1

    return dis + 1


if __name__ == '__main__':
    print(remove_duplicates([]))
    print(remove_duplicates([1]))
    print(remove_duplicates([1, 1]))
    print(remove_duplicates([2, 2, 2, 3, 4, 6]))
    print(remove_duplicates([1, 2, 3, 4, 5, 6, 7]))
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
