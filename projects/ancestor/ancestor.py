from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for edge in ancestors:
        if edge[0] not in graph.vertices:
            graph.add_vertex(edge[0])
        if edge[1] not in graph.vertices:
            graph.add_vertex(edge[1])
    for edge in ancestors:
        graph.add_edge(edge[1], edge[0])
    return graph.last_children(starting_node)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 6)