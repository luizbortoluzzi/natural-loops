
D = [
    set(),
    set([1]),
    set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
]
pred =[{},{},{1,3,4},{2},{2},{4,10},{4},{5,6},{5,9},{8},{9},{7},{10,11}]

natural_loops = []

def find_natural_loops(node, stack, visited, loop_header):
    visited[node] = True
    stack.append(node)

    for neighbor in pred[node]:
        if neighbor == loop_header:
            natural_loops.append(stack.copy())
        elif not visited[neighbor]:
            find_natural_loops(neighbor, stack, visited, loop_header)

    stack.pop()
    visited[node] = False

for node in range(1, len(D)):
    visited = [False] * len(D)
    find_natural_loops(node, [], visited, node)


with open("output.txt", "w") as file:
    for i, loop in enumerate(natural_loops, start=1):
        file.write(f"Loop {i}:\n")
        file.write(f"Header: node {loop[0]}\n")
        file.write("Blocks: " + ", ".join(map(str, loop)) + "\n\n")
