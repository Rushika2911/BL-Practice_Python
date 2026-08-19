from sorting import (
    selection_sort,
    bubble_sort,
    merge_sort,
    quick_sort
)

from treasure import binary_search

def mission_1():

    print("\n===== MISSION 1: LEADERBOARD =====")

    n = int(input("Enter number of players: "))

    players = []

    for _ in range(n):
        name, score = input().split()
        players.append([name, int(score)])

    print("\nChoose Sorting Algorithm:")
    print("1. Selection Sort")
    print("2. Bubble Sort")
    print("3. Merge Sort")
    print("4. Quick Sort")

    choice = int(input("Choice: "))

    if choice == 1:

        selection_sort(players)
        algorithm = "Selection Sort"

    elif choice == 2:

        bubble_sort(players)
        algorithm = "Bubble Sort"

    elif choice == 3:

        players = merge_sort(players)
        algorithm = "Merge Sort"

    elif choice == 4:

        quick_sort(players, 0, len(players) - 1)
        algorithm = "Quick Sort"

    else:
        print("Invalid choice!")
        return

    print("\nLeaderboard")
    print("Using", algorithm)
    print()

    for player in players:
        print(player[0], player[1])

def mission_2():

    print("\n===== MISSION 2: TREASURE SCANNER =====")

    n = int(input("Enter number of treasures: "))

    treasure_ids = list(map(int, input("Enter treasure IDs: ").split()))

    target = int(input("Enter Treasure ID: "))

    index = binary_search(treasure_ids, target)

    print("\nSearching for:", target)

    if index != -1:
        print("Treasure Found!")
        print("Index:", index)
    else:
        print("Treasure Not Found!")


def main():

    print("===== ALGORITHM ARENA =====")

    mission_1()
    mission_2()


if __name__ == "__main__":
    main()