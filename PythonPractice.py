def caught_speeding(speed, is_birthday):
    while not is_birthday:
        if speed <= 60:
            return 0
        elif 61 <= speed <= 80:
            return 1
        else:
            if speed >= 81:
                return 2
    return caught_speeding(speed - 5, False)


print(caught_speeding(82, False))
print(caught_speeding(82, True))


def big_diff(nums):
    # find smallest number
    smallest = nums[0]
    for n in nums:
        smallest = min(smallest, n)

    # find largest number
    largest = nums[0]
    for n in nums:
        largest = max(largest, n)

    return largest - smallest


print(big_diff([1, 2, 10, 50]))


def sum_13(nums):
    result = 0
    previous_is_13 = False

    for i in nums:
        # check for previous num being 13
        if i == 13:
            previous_is_13 = True
            continue

        if previous_is_13:
            previous_is_13 = False
            continue
        result += i
    return result


print(sum_13([1, 2, 3, 4, 14, 13, 15]))