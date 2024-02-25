def merge(l1, l2):
    nums = []
    l1_i = 0
    l2_i = 0

    while l1_i < len(l1) and l2_i < len(l2):
        if l1[l1_i] < l2[l2_i]:
            nums.append(l1[l1_i])
            l1_i += 1
        else:
            nums.append(l2[l2_i])
            l2_i += 1

    nums.extend(l1[l1_i:])
    nums.extend(l2[l2_i:])

    return nums

x = [2, 5, 8]
y = [4, 6, 7]
print(merge(x, y))

