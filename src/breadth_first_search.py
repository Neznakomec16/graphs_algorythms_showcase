from queue import Queue

from src.graph import Node


def bfs(start_node: Node, target_value: str):
    stack = Queue()
    # Set of visited nodes to prevent loops
    visited = set()

    stack.put(start_node)
    visited.add(start_node)

    parent = dict()
    parent[start_node] = None  # no parent for start node

    found_node = None
    while not stack.empty():
        current_node = stack.get()
        if current_node.name == target_value:
            found_node = current_node
            break

        for connection in current_node.connections:
            next_node = connection.target_node
            if next_node not in visited:
                stack.put(next_node)
                parent[next_node] = current_node
                visited.add(next_node)

    path = []
    if found_node is not None:
        path.append(found_node)
        while parent[found_node] is not None:
            path.append(parent[found_node])
            found_node = parent[found_node]
    return reversed(path)
