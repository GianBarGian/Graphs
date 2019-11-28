"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import functools
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}  
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise KeyError("That vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()
        while queue.size() > 0:
            current_vertex = queue.dequeue()
            if current_vertex not in visited:
                print('bft', current_vertex)
                visited.add(current_vertex)
                for next_vertex in self.vertices[current_vertex]:
                    queue.enqueue(next_vertex) 

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print('dft', current_vertex)
                visited.add(current_vertex)
                for next_vertex in self.vertices[current_vertex]:
                    stack.push(next_vertex) 

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if starting_vertex not in visited:
            print('dft recursive', starting_vertex)
            visited.add(starting_vertex)
            for next_vertex in self.vertices[starting_vertex]:
                self.dft_recursive(next_vertex, visited)
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = set()
        
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            path = queue.dequeue()
            current_vertex = path[-1]
            if current_vertex not in visited:
                if current_vertex == destination_vertex:
                    return path
                visited.add(current_vertex)
                for next_vertex in self.vertices[current_vertex]:
                    new_path = list(path)
                    new_path.append(next_vertex)
                    queue.enqueue(new_path)
            
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        path = []
        while stack.size() > 0:
            current_vertex = stack.pop()
            path.append(current_vertex)
            if current_vertex not in visited:
                if current_vertex == destination_vertex:
                    return path
                visited.add(current_vertex)
                for next_vertex in self.vertices[current_vertex]:
                    stack.push(next_vertex) 
    def last_children(self, starting_vertex):
        queue = Queue()
        visited = set()
        paths = []
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            path = queue.dequeue()
            current_vertex = path[-1]
            if current_vertex not in visited:
                if not len(self.vertices[current_vertex]):
                    paths.append(path) 
                visited.add(current_vertex)
                for next_vertex in self.vertices[current_vertex]:
                    new_path = list(path)
                    new_path.append(next_vertex)
                    queue.enqueue(new_path)
        correct_path = functools.reduce(lambda a,b: a if len(a) > len(b) else b, paths)
        if len(correct_path) > 1:
            return correct_path[-1]
        return -1




if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
