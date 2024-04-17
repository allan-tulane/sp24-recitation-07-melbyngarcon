from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
  """
  Returns:
    the set of nodes reachable from start_node
  """
  result = set([start_node])
  frontier = set([start_node])
  while frontier:
      current = frontier.pop()  # Remove one node from frontier
      for neighbor in graph[current]:
          if neighbor not in result:
              result.add(neighbor)
              frontier.add(neighbor)
  return result



def connected(graph):
    """
    Determines if the graph is connected.

    Returns:
        True if the graph is connected, False otherwise.
    """
    if not graph:  # Handle the case where the graph is empty
        return True

    # Start from any node in the graph (grab an arbitrary key from the graph dictionary)
    start_node = next(iter(graph))

    # Use the reachable function to get all nodes that can be reached from the start node
    reachable_nodes = reachable(graph, start_node)

    # Check if the number of reachable nodes is equal to the number of nodes in the graph
    return len(reachable_nodes) == len(graph)



def n_components(graph):
  """
  Returns the number of connected components in an undirected graph.
  """
  visited = set()
  component_count = 0

  for node in graph:
      if node not in visited:
          # Get all nodes reachable from the current node
          reachable_nodes = reachable(graph, node)
          # Add these nodes to the visited set
          visited.update(reachable_nodes)
          # Increment the component count for each set of connected nodes
          component_count += 1

  return component_count

