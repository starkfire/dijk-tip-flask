import sys
import adjacency_matrix as matrix

# initialize variables
nodes = []                      # an array for representing each node
vertices, edges = None, None    # vertices and edges
n_vtx = 0                       # number of vertices

def get_graph(adj_matrix):
    """
    This function will simply return the vertices and edges
    from the input adjacency matrix
    """
    return adj_matrix.vertices, adj_matrix.edges

def create_nodes(source_index, n_vtx):
    """
    Creates an array for representing each vertex as an array or node [x, y], where:
        x : indicates if the vertex has been visited (1) or not (0)
        y : indicates the distance of the node from the input source
    
    The starting point will be represented with `[0, 0]`, 
    while other nodes will have an infinite distance `[0, inf]`
    """
    for x in range(n_vtx):
        nodes.append([0, 0]) if x == source_index else nodes.append([0, sys.maxsize])
    return None

def print_vertices(vertices):
    """
    TEST FUNCTION: Print all vertices
    """
    i = 0
    for x in range(len(vertices)):
        print(chr(ord("A") + i), "=" , vertices[x])
        i += 1

def dijkstra(source, destination):
    """
    Implementation of Dijkstra's Algorithm
    """
    # convert input letters to indexes
    source, destination = ord(source) - 97, ord(destination) - 97
    # import the graph
    vertices, edges = get_graph(matrix)
    # get the number of vertices
    n_vtx = len(vertices)
    # TEST
    print_vertices(vertices)
    # create an array for representing each vertex as a node
    create_nodes(source, n_vtx)
