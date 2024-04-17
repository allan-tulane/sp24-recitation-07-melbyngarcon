# CMPS 2200 Recitation 10## Answers

**Name:**_________________________
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
The reachable function, which uses a breadth-first search (BFS), has a time and space complexity of O(n + m), where n is the number of nodes and m is the number of edges in the graph. This complexity comes from processing each node once and considering each edge twice (due to the undirected nature of the graph). The function scales linearly with the size of the graph, making it efficient for sparse and moderately dense graphs. The space complexity is also O(n + m), which includes the storage for all nodes, edges, and the auxiliary data structures used during the traversal.

- **4)**
To determine if a graph is connected, you only need to call the reachable function once. By starting from any node and checking if all nodes are reachable from this node, you can conclusively determine the connectivity of the entire graph with just one call to reachable

- **5)**
The work of the connected function, when analyzing an undirected graph with n nodes and m edges, involves calling the reachable function once to determine connectivity. Since reachable has a time complexity of O(n + m), the same complexity applies to connected. This function efficiently checks if you can reach all other nodes from any starting node, thereby confirming whether the graph is connected. This single check, encompassing all nodes and edges linearly, makes it practical for various sizes of graphs.

- **7)**
Switching the graph representation to an adjacency matrix would change the work of the * reachable' function. In an adjacency matrix, each node's connections are represented as rows in a matrix, with the presence of an edge indicated by a value (often 1) and the absence by another (often 0). The primary difference in the work of reachable' is in how neighbors are accessed: instead of direct set operations, each node check involves scanning through an entire row of the matrix to determine connected nodes. This results in a time complexity of O(n^2) for 'reachable', regardless of the number of edges m, because every potential connection (n*n, where n is the number of nodes) must be checked in the worst case. This is less efficient than the adjacency list approach, particularly for sparse graphs where m is much smaller than n^2.
