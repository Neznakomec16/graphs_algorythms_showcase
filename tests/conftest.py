import pytest

from src.graph import Node


@pytest.fixture()
def nodes() -> list[Node]:
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")

    return [a, b, c, d, e]


@pytest.fixture()
def connected_nodes(nodes) -> list[Node]:
    a, b, c, d, e = nodes
    a.add_connection(c, 1)
    a.add_connection(a, 25)
    a.add_connection(b, 2)
    b.add_connection(c, 3)
    c.add_connection(e, 4)
    return nodes
