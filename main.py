from sorting import (selection_sort,bubble_sort,merge_sort,quick_sort)
from treasure import binary_search
from bfs import bidirectional_bfs
from dfs import dfs
from battle import battle_score, find_monster

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

def mission_3():

    print("\n===== MISSION 3: FASTEST ROUTE =====")

    n = int(input("Enter number of roads: "))

    graph = {}

    for _ in range(n):

        a, b = input().split()

        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    start, end = input("Enter Start and Destination: ").split()

    path = bidirectional_bfs(graph, start, end)

    print("\nFrom:", start)
    print("To:", end)

    if path:
        print("\nShortest Route:")
        print(" -> ".join(path))
        print("\nSteps:", len(path) - 1)
    else:
        print("\nNo route found!")


def mission_4():
    print("\n===== MISSION 4: EXPLORE THE KINGDOM =====")

    n = int(input("Enter number of roads: "))

    graph = {}

    for _ in range(n):

        a, b = input().split()

        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    start= input("Starting location: ")

    order = dfs(graph, start)

    print("\nStarting Location:", start)

    print("\nDFS Order:")
    print(" -> ".join(order))


def mission_5():

    print("\n===== MISSION 5: MONSTER BATTLE =====")

    n = int(input("Enter number of monsters: "))

    monsters = []

    for _ in range(n):

        name, health, attack, reward = input().split()

        monster = [
            name,
            int(health),
            int(attack),
            int(reward)
        ]

        monsters.append(monster)

    name = input("Choose Monster: ")

    monster = find_monster(monsters, name)

    if monster is None:
        print("Monster not found!")
        return 0

    health = monster[1]
    attack = monster[2]
    reward = monster[3]

    score = battle_score(
        health,
        attack,
        reward
    )

    print("\nMonster:", name)
    print("Battle Score:", score)

    return score

def main():

    print("===== ALGORITHM ARENA =====")

    mission_1()
    mission_2()
    mission_3()
    mission_4()
    mission_5()

if __name__ == "__main__":
    main()