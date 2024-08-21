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

