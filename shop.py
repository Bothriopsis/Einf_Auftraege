import heapq
import sys

putin = sys.stdin.readline


def inp():
    return int(putin())


def invert():
    return map(int, putin().split())


def starting_price(main_ar, sec_arr):
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
    return sub_summ


if __name__ == "__main__":
    t = inp()
    for x in range(t):
        arr = []
        k_arr = []
        temp_pop = []
        n, k = invert()
        a = list(invert())
        a = [-x for x in a]
        b = list(invert())
        max_value = 0
        sub_sum = 0
        my_bool = False

        for i in range(n):
            arr.append([a[i], b[i]])
        arr.sort(key=lambda y: y[1], reverse=False)

        for k_range in range(1, k + 1):
            if arr:
                heapq.heappush(k_arr, arr[-1])
                arr.pop()

        if arr:
            sub_sum = starting_price(arr, k_arr)
        if sub_sum > max_value:
            max_value = sub_sum
        while arr:
            if arr:
                sub_sum -= arr[-1][1]
                if arr[-1][1] + arr[-1][0] <= 0:
                    sub_sum += arr[-1][0]
                temp_pop = heapq.heappushpop(k_arr, arr[-1])
                arr.pop()
                if temp_pop:
                    sub_sum -= temp_pop[0]
            if sub_sum > max_value:
                max_value = sub_sum
        print(max_value)
