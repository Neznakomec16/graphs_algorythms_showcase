import pytest

from src.depth_first_search import dfs_recurcive
from src.graph import Node


@pytest.mark.parametrize(
    "target, expected",
    (
        ("A", ["A"]),
        ("B", ["A", "B"]),
        ("C", ["A", "C"]),
        ("E", ["A", "C", "E"]),
        ("D", None),
        ("F", None),
    ),
)
def test_dfs_recurcive(connected_nodes: list[Node], target: str, expected: list[Node]):
    a, b, c, d, e = connected_nodes
    result = dfs_recurcive(a, target=target)
    if result is not None:
        result = list(map(lambda x: x.name, result))
    assert result == expected
