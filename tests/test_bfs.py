import pytest

from src.breadth_first_search import bfs
from src.graph import Node


@pytest.mark.parametrize(
    "target, expected",
    (
        ("A", ["A"]),
        ("B", ["A", "B"]),
        ("C", ["A", "C"]),
        ("E", ["A", "C", "E"]),
        ("D", []),
        ("F", []),
    ),
)
def test_bfs(connected_nodes: list[Node], target: str, expected: list[str]):
    a, b, c, d, e = connected_nodes
    result = bfs(a, target)
    assert list(map(lambda x: x.name, result)) == expected
