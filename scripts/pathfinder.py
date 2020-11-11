import sys
import adjacency_matrix as matrix

inf = sys.maxsize

class Pathfinder:
    """
    Dijkstra Pathfinder Implementation
    """

    def __init__(self, vertices, edges, debug=False):
        self.vertices = vertices
        self.edges = edges
        self.n_vtx = len(vertices)
        self.nodes = []
        self.source = None
        self.debug = debug
    
    
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

        # print adjacent nodes
        if self.debug: print("Adjacent Nodes: ", adjacent_nodes)
        
        # it's either our script failed to traverse all nodes or it has reached all nodes
        # either way, issue a warning
        if len(adjacent_nodes) == 0:
            if self.debug: print("WARNING: End of the Line\n")
            return None
        
        for x in range(len(adjacent_nodes)):
            # if there is only a single adjacent node left, there's no need to loop further
            if len(adjacent_nodes) == 1: break
            
            # index of the adjacent node, index of the other adjacent node
            adj, other_adj = adjacent_nodes[x], adjacent_nodes[x - 1]

            # compare the distance of the adjacent node to the other adjacent node
            if (self.edges[node][adj] <= self.edges[node][other_adj]):
                adjacent_nodes.pop(x-1)
        
        # print adjacent nodes
        if self.debug: print("Nearest Node: ", adjacent_nodes)
        
        return adjacent_nodes[0]
    
    
    def get_other_unvisited_nodes(self):
        """
        Returns the index of the other unvisited nodes
        """
        for x in range(self.n_vtx):
            if self.nodes[x][0] == 0: return x
        return None

    
    def dijkstra(self, src):
        """
        Returns the shortest distance from the input source node to the other nodes.
        """
        # convert the input parameters to interpretable index
        src= ord(src) - 97

        # set the source property to the index of the source node
        self.source = src
        
        # create an array to represent each vertex as a node
        self.create_nodes(src)

        # a variable for tracking the current node
        current_node = src
        
        for vtx in range(self.n_vtx):
            if self.debug:
                print("\n==================================\n")
                print("Current Node: ", chr(current_node + 97))

            for x in range(self.n_vtx):
                # if unvisited and adjacent
                if self.vertices[current_node][x] == 1 and self.nodes[x][0] == 0:
                    if self.debug: print("Checking Distance to Node", chr(x + 97), ":", self.edges[current_node][x])

                    # prefer the shortest distance between the two nodes
                    distance = self.nodes[current_node][1] + self.edges[current_node][x]
                    if self.nodes[x][1] > distance:
                        self.nodes[x][1] = distance

            # mark current node as visited
            self.nodes[current_node][0] = 1

            # update current node
            current_node = self.get_next_node(current_node)
            if current_node == None:
                current_node = self.get_other_unvisited_nodes()
        
        # print the final distances
        if self.debug:
            print("\n==================================\n")
            self.print_final_distances()
    
    
    def print_final_distances(self):
        """
        Print the distance of the source node to other nodes.
        """
        for dist in range(len(self.nodes)):
            print("Shortest Distance from", chr(self.source + 97), "to", chr(dist + 97), "=", self.nodes[dist][1])
    

    def distance_to_destination(self, dest):
        """
        Return the distance of the source node to the destination node.
        """
        return self.nodes[ord(dest) - 97][1]