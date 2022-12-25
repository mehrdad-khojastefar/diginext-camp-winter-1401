def minimum_swaps(arr: list) -> int:
    n = len(arr)

    # holds the position of element
    pos_array = [*enumerate(arr)]

    pos_array.sort(key=lambda it: it[1])

    # create a node for each element and holds the status (visited/not visited) in this dictionary
    node_state = {k: False for k in range(n)}

    count = 0
    for i in range(n):

        if node_state[i] or pos_array[i][0] == i:
            continue

        cycle_size = 0
        j = i

        while not node_state[j]:

            node_state[j] = True

            j = pos_array[j][0]
            cycle_size += 1

        if cycle_size > 0:
            count += cycle_size - 1

    return count


if __name__ == "__main__":
    # gets the array from user in format like -> 1 2 3 4 5 (seperated by space)
    arr = [int(c) for c in list(input().split())]
    print(minimum_swaps(arr))
