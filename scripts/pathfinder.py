import sys
import adjacency_matrix as matrix

# initialize variables
nodes = []                      # an array for representing each node
vertices, edges = None, None    # vertices and edges of a graph
n_vtx = 0                       # number of vertices
inf = sys.maxsize               # signifies an infinite value

def get_graph(adj_matrix):
    """
    Returns the vertices and edges from an input adjacency matrix.
    """
    return adj_matrix.vertices, adj_matrix.edges

def create_nodes(src_index, n_vtx):
    """
    Creates an array for representing each vertex as a node [x, y]:
        x : indicates if vertex/node has been visited (1) or not (0)
        y : indicates the distance of the node from the input source
    """
    for x in range(n_vtx):
        nodes.append([0, 0]) if x == src_index else nodes.append([0, inf])
    return None