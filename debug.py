import heapq

if __name__ == "__main__":
    my_array = [23,243,13,354,23,12,4]

    heapq.heapify(my_array)
    print(f"my Array: {my_array}")
    x = heapq.heappushpop(my_array, 5)
    print(f"after heap is array: {my_array}")
    print(f"for the value of x we have: {x}")