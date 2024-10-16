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
        n, k = invert()
        a = list(invert())
        a = [-x for x in a]
        b = list(invert())
        k_arr = []
        max_value = 0
        sub_sum = 0

        for i in range(n):
            arr.append([a[i], b[i]])
        arr.sort(key=lambda y: y[1], reverse=True)

        for k_range in range(1, k + 1):
            if arr:
                if k_range <= len(arr):
                    heapq.heappush(k_arr, arr[0])
                arr.pop(0)

        if arr:
            sub_sum = starting_price(arr, k_arr)
        if sub_sum > max_value:
            max_value = sub_sum
        while arr:
            if k_arr and len(k_arr) == k:
                if arr[0][0] + arr[0][1] > 0:
                    sub_sum -= k_arr[0][0]
                    sub_sum -= arr[0][1]
            if arr:
                heapq.heappushpop(k_arr, arr[0])
                arr.pop(0)
            if sub_sum > max_value:
                max_value = sub_sum
        print(max_value)
