import heapq
import sys

read_input = sys.stdin.readline

def get_single_integer():
    return int(read_input())

def get_integer_list():
    return map(int, read_input().split())


def calc_total(primary_items, secondary_heap):
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
    return total


def main():
    test_cases = get_single_integer()

    for _ in range(test_cases):
        heap = []
        remaining_items = []
        n, k = get_integer_list()

        prices = list(get_integer_list())
        neg_prices = [-price for price in prices]

        bonuses = list(get_integer_list())

        max_profit = 0
        current_profit = 0

        combined = list(zip(neg_prices, bonuses))

        combined.sort(key=lambda item: item[1])

        for _ in range(k):
            if combined:
                heapq.heappush(heap, combined.pop())

        if combined:
            current_profit = calc_total(combined, heap)

        if current_profit > max_profit:
            max_profit = current_profit

        while combined:
            item = combined.pop()
            if item[0] + item[1] >= 0:
                current_profit -= item[1]
            else:
                current_profit += item[0]

            removed_item = heapq.heappushpop(heap, item)
            if removed_item:
                current_profit -= removed_item[0]

            if current_profit > max_profit:
                max_profit = current_profit
        print(max_profit)


main()
