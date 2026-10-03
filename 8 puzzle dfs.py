# 8-Puzzle Problem using DFS

# Goal State
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Display the puzzle
def display(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


# Generate possible moves
def get_neighbors(state):

    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    # Move UP
    if row > 0:
        new_state = list(state)
        new_state[blank], new_state[blank - 3] = \
            new_state[blank - 3], new_state[blank]
        neighbors.append(("UP", tuple(new_state)))

    # Move DOWN
    if row < 2:
        new_state = list(state)
        new_state[blank], new_state[blank + 3] = \
            new_state[blank + 3], new_state[blank]
        neighbors.append(("DOWN", tuple(new_state)))

    # Move LEFT
    if col > 0:
        new_state = list(state)
        new_state[blank], new_state[blank - 1] = \
            new_state[blank - 1], new_state[blank]
        neighbors.append(("LEFT", tuple(new_state)))

    # Move RIGHT
    if col < 2:
        new_state = list(state)
        new_state[blank], new_state[blank + 1] = \
            new_state[blank + 1], new_state[blank]
        neighbors.append(("RIGHT", tuple(new_state)))

    return neighbors


# DFS function
def dfs(state, path, visited):

    # Goal test
    if state == goal:
        return path

    # Mark state as visited
    visited.add(state)

    # Explore neighbors
    for move, new_state in get_neighbors(state):

        if new_state not in visited:

            result = dfs(
                new_state,
                path + [(move, new_state)],
                visited
            )

            if result is not None:
                return result

    return None


# -------------------------------
# Get initial state from user
# -------------------------------

print("Enter the initial state")
print("Use 0 for the blank space")
print("Example: 1 2 3 4 0 6 7 5 8")

initial = tuple(map(int, input().split()))


# Check input
if len(initial) != 9 or set(initial) != set(range(9)):

    print("Invalid input!")
    print("Enter numbers 0 to 8 exactly once.")

else:

    print("\nInitial State:")
    display(initial)

    # Run DFS
    visited = set()
    solution = dfs(initial, [], visited)

    # Display solution
    if solution is not None:

        print("Solution found using DFS!")
        print("Number of moves:", len(solution))

        print("\nMoves:")

        for i, (move, state) in enumerate(solution, 1):

            print("Move", i, ":", move)
            display(state)

        # Display final state
        print("Final State:")
        display(solution[-1][1])

        print("Goal state reached!")

    else:

        print("No solution found.")



