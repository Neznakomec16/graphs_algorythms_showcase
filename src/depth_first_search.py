from src.graph import Node


def dfs_recurcive(start_node: Node, target: str, path: list | None = None, visited: set | None = None) -> list[Node] | None:
    if path is None: path = []
    if visited is None: visited = set()
    path.append(start_node)
    visited.add(start_node)
    if start_node.name == target:
        return path
    for connection in sorted(start_node.connections, key=lambda x: x.weight):
        node = connection.target_node
        if node not in visited:
            result = dfs_recurcive(node, target, path, visited)
            if result is not None:
                return result
    path.pop()
    return None
