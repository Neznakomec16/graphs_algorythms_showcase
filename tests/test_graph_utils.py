from src.graph import Node
from src.graph_utils import make_adjaency_matrix, make_edges_list, make_adjaency_list


def test_make_adjaency_matrix(connected_nodes: list[Node]):
    a, b, c, d, e = connected_nodes
    result = make_adjaency_matrix(connected_nodes)
    assert result[a][a] == 25
    matrix = [
        [25, 2, 1, False, False],
        [False, False, 3, False, False],
        [False, False, False, False, 4],
        [False, False, False, False, False],
        [False, False, False, False, False],
    ]
    for result_line, matrix_line in zip(result.values(), matrix):
        assert list(result_line.values()) == matrix_line


def test_make_edges_list(connected_nodes: list[Node]):
    a, b, c, d, e = connected_nodes
    result = make_edges_list(connected_nodes)
    first_result = sorted(result, key=lambda obj: obj.weight)[0]
    assert first_result.weight == 1
    assert first_result.target_node == c
    assert first_result.start_node == a


def test_make_adjaency_list(connected_nodes: list[Node]):
    a, b, c, d, e = connected_nodes
    result = make_adjaency_list(connected_nodes)
    assert sorted(result[a], key=lambda obj: obj.weight) == sorted(list(a.connections), key=lambda obj: obj.weight)
