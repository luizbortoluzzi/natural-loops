pred = [{}, {}, {1, 3, 4}, {2}, {2}, {4, 10}, {4}, {5, 6}, {5, 9}, {8}, {9}, {7}, {10, 11}]

def convert_pred_to_graph(pred):
    graph = {}
    for i in range(1, len(pred)):
        if i not in graph:
            graph[i] = set()
        for p in pred[i]:
            if p not in graph:
                graph[p] = set()
            graph[p].add(i)
    return graph

def dfs(graph, node, visited, stack, loops, ancestor):
    visited.add(node)
    stack.append(node)
    ancestor[node] = True

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack, loops, ancestor)
        elif ancestor[neighbor]:
            loop_start_index = stack.index(neighbor)
            loop = stack[loop_start_index:]
            loops.append((neighbor, loop))

    stack.pop()
    ancestor[node] = False

def find_loops(graph):
    visited = set()
    ancestor = {}
    loops = []

    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, [], loops, ancestor)

    return loops

graph = convert_pred_to_graph(pred)
loops = find_loops(graph)

with open('loops.txt', 'w') as file:
    for i, (header, loop) in enumerate(loops):
        file.write(f"Laço {i + 1}:\n")
        file.write(f"Cabeçalho: nodo {header}\n")
        file.write("Blocos " + ', '.join(map(str, loop)) + "\n\n")
