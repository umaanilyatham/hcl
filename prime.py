def prime(start, end):
    for i in range(start, end + 1):
        if i <= 1:
            continue

        for num in range(2, int(i ** 0.5) + 1):
            if i % num == 0:
                break
        else:
            print(i, end=" ")

prime(2, 100)

