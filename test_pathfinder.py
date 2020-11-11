from scripts.pathfinder import Pathfinder
import scripts.adjacency_matrix as matrix

pf = Pathfinder(matrix.vertices, matrix.edges)

# pf.dijkstra(source_node) ; a to u
pf.dijkstra('a')

# print distance of source_node (A) to all other nodes
pf.print_final_distances()

# print the distance of A to U
distance = pf.distance_to_destination('u')
print(distance)