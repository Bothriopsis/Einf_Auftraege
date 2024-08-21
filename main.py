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
unsorted_array = [12,24,45,9,8,90,3]

index = 0
next_even = 0
next_odd = 0
print(next_odd)

while unsorted_array:
    if unsorted_array[index] % 2 == 0:
        next_even = unsorted_array[index]
    elif unsorted_array[index] % 2 != 0:
        next_odd = unsorted_array[index]
    print(unsorted_array[index])
    index += 1
    if index == len(unsorted_array):
        break

print(unsorted_array)