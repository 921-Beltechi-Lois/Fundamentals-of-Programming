def getNextGap(gap):
    # Shrink gap by Shrink factor
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    return gap

def sort(a_list, compare):
    n = len(a_list)

    gap = n
    swapped = True

    while gap != 1 or swapped == 1:
        gap = getNextGap(gap)
        swapped = False

        for i in range(0, n - gap):
            #if a_list[i] > a_list[i + gap]:
            if compare(a_list[i], a_list[i+gap]):   #used
                a_list[i], a_list[i + gap] = a_list[i + gap], a_list[i]
                swapped = True
    return a_list

a_list = sort([10,-1,3,5], lambda x, y: x > y)
print(a_list)



def filter_list(a_list, filter):
    filtered_list = []
    for it in a_list:
        if filter(it):
            filtered_list.append(it)
    return filtered_list


a = [1, 2, 3, 4, 5]

print((lambda x: x > 3)(4))

asd = filter_list(a, lambda x: x > 3)
print(asd)
