# Problem 1 / Solution 1
num_array = [3, 34, 4, 12, 5, 2]
target_sum = 9


def validation(array, target):
    if target == 0 or target < 1:
        return False
    elif len(array) == 0:
        return False
    else:
        if array[0] == target:
            return True
        else:
            return validation(array[1:], (target - array[0])) or validation(array[1:], target)


print(validation(num_array, target_sum))

# Problem 3 / Solution 1
unsorted_array = [12, 24, 45, 9, 8, 90, 3]

index = 0
length_index = len(unsorted_array) - 1

print(f"unsorted_array: {unsorted_array}")
while index < len(unsorted_array):
    if unsorted_array[index] % 2 != 0:
        if unsorted_array[length_index] % 2 == 0:
            unsorted_array[index], unsorted_array[length_index] \
                = unsorted_array[length_index], unsorted_array[index]
        elif unsorted_array[length_index] % 2 != 0 and length_index > index:
            length_index -= 1
            unsorted_array[index], unsorted_array[length_index] \
                = unsorted_array[length_index], unsorted_array[index]
        else:
            break
    index += 1


print(f"Sorted: {unsorted_array}")
