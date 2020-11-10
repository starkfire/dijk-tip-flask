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
    
    def get_next_node(self, node: int):
        """
        Returns the nearest, unvisited node that is adjacent to the input node.
        """
        # get adjacent nodes
        adjacent_nodes = self.get_adjacent_nodes(node)
        
        # it's either our script failed to traverse all nodes or it has reached all nodes
        # either way, issue a warning
        if len(adjacent_nodes) == 0:
            print("WARNING: End of the Line")
            return None
        
        for x in range(len(adjacent_nodes)):
            # if there is only a single adjacent node left, there's no need to loop further
            if len(adjacent_nodes) == 1: break
            
            # index of the adjacent node, index of the other adjacent node
            adj, other_adj = adjacent_nodes[x], adjacent_nodes[x - 1]

            # compare the distance of the adjacent node to the other adjacent node
            if (self.edges[node][adj] <= self.edges[node][other_adj]):
                adjacent_nodes.pop(x-1)
        
        return adjacent_nodes[0]
    
    def dijkstra(self, src, dest):
        """
        Returns the shortest path from the input source node to destination node
        """
        # convert the input parameters to interpretable index
        src, dest = ord(src) - 97, ord(dest) - 97
        # create an array to represent each vertex as a node
        self.create_nodes(src)