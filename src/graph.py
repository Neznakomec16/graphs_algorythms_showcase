class Node:
    def __init__(self, name: str):
        self.name = name
        self._connections: set[Connection] = set()

    def add_connection(self, node: "Node", weight: int):
        connection = Connection(self, node, weight)
        self._connections.add(connection)
        return connection

    @property
    def connections(self):
        return self._connections

    def __str__(self):
        return f"Node {self.name}"


class Connection:
    def __init__(self, start: Node, target: Node, weight: int):
        self.start_node = start
        self.target_node = target
        self.weight = weight

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"<{self.start_node}->{self.target_node}: {self.weight}>"
