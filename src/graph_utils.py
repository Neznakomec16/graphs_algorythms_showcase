from src.graph import Node, Connection


def make_edges_list(nodes: list[Node]) -> list[Connection]:
    return list(set(connection for edge in nodes for connection in edge.connections))


def make_adjaency_matrix(nodes: list[Node]) -> dict[Node, dict[Node, int | bool]]:
    empty_matrix = {node: {node_inside: False for node_inside in nodes} for node in nodes}
    for node in nodes:
        for connection in node.connections:
            empty_matrix[node][connection.target_node] = connection.weight
    return empty_matrix


def print_adjaency_matrix(matrix: dict[Node, dict[Node, int | bool]]):
    element_len = len(str(list(matrix.keys())[0]))
    print(" " * (element_len + 1), *matrix)
    for node, row in matrix.items():
        print(f'{node}: {" ".join(map(lambda val: f"{val:^{element_len}}", row.values()))}')


def make_adjaency_list(nodes: list[Node]) -> dict:
    return {node: [connection for connection in node.connections] for node in nodes}


def print_adjaency_list(adj_list: dict[Node, list[Connection]]):
    for node, value in adj_list.items():
        print(f'{node}: {" ".join(map(str, value))}')
