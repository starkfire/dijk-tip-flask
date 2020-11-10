import sys
import adjacency_matrix as matrix

inf = sys.maxsize

class Pathfinder:
    """
    Dijkstra Pathfinder Implementation
    """

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.n_vtx = len(vertices)
        self.nodes = []
    
    def create_nodes(self, src):
        """
        Creates an array for representing each vertex as a node [x, y]:
            x : indicates if vertex/node has been visited (1) or not (0)
            y : indicates the distance of the node from the input source
        """
        for x in range(self.n_vtx):
            self.nodes.append([0, 0]) if x == src else self.nodes.append([0, inf])
        return None
    
    def get_adjacent_nodes(self, node: int):
        """
        Returns the index of nodes that are adjacent to the input node.
        """
        adjacent_nodes = []
        node_vtx = self.vertices[node]

        for x in range(len(node_vtx)):
            if node_vtx[x] == 1 and self.nodes[x][0] == 0:
                adjacent_nodes.append(x)
        
        return adjacent_nodes