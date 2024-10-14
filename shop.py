def main():
    t = int(input().strip())

    for _ in range(t):
        n, k = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))

        # Create an index list sorted by b values in descending order
        indices = sorted(range(n), key=lambda i: b[i], reverse=True)

        # Initial values
        total_penalty = sum(max(0, b[i] - a[i]) for i in indices)
        ans = 0
        current_sum = 0
        elements = []

        # If the number of elements in the set equals k, calculate potential answer
        if len(elements) == k:
            ans = max(ans, total_penalty - current_sum)

        for i in indices:
            total_penalty -= max(0, b[i] - a[i])
            elements.append(a[i])
            current_sum += a[i]

            # Maintain a list of up to `k` smallest elements
            if len(elements) > k:
                largest = max(elements)
                current_sum -= largest
                elements.remove(largest)

            if len(elements) == k:
                ans = max(ans, total_penalty - current_sum)

        print(ans)


if __name__ == "__main__":
    main()
