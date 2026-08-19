def selection_sort(players):
    n = len(players)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if players[j][1] < players[min_index][1]:
                min_index = j

        players[i], players[min_index] = players[min_index], players[i]

    return players


def bubble_sort(players):
    n = len(players)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if players[j][1] > players[j + 1][1]:
                players[j], players[j + 1] = players[j + 1], players[j]
                swapped = True

        if not swapped:
            break

    return players


def merge_sort(players):
    if len(players) <= 1:
        return players

    mid = len(players) // 2

    left = players[:mid]
    right = players[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def quick_sort(players, low, high):
    if low < high:

        pivot_index = partition(players, low, high)

        quick_sort(players, low, pivot_index - 1)
        quick_sort(players, pivot_index + 1, high)


def partition(players, low, high):

    pivot = players[high][1]

    i = low - 1

    for j in range(low, high):

        if players[j][1] <= pivot:
            i += 1
            players[i], players[j] = players[j], players[i]

    players[i + 1], players[high] = players[high], players[i + 1]

    return i + 1