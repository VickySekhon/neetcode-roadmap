def restore_array(pairs):
     """ 
     An array was corrupted but luckily it's pairs were still stored.
     
     Given an array of "pairs" with containing n-1 combinations of:
     [pairs[i], [i+1]] or [pairs[i+1], pairs[i]], return the original
     array or reversed original array (any is valid).
     
     e.g.
     For pairs = [[3, 5], [1, 4], [2, 4], [1, 5]], the output can be restoreArray(pairs) = [3, 5, 1, 4, 2].

     The result of splitting the array [3, 5, 1, 4, 2] into pairs is [[3, 5], [5, 1], [1, 4], [4, 2]].

     It can be seen that this array is the same as the pairs up to permutations in some pairs and pairs shuffling.

     The reversed array [2, 4, 1, 5, 3] is also considered a valid answer.
     """
     graph = {}
     for pair in pairs:
          a, b = pair
          if a not in graph:
               graph[a] = [b]
          else:
               graph[a].append(b)
          if b not in graph:
               graph[b] = [a]
          else:
               graph[b].append(a)
     print(graph)
     
     start_node = None
     for node, edges in graph.items():
          degree = len(edges)
          if degree == 1: 
               start_node = node
               break
     
     visited = []
     original_arr = dfs(graph, visited, node=start_node)
     
     print(start_node)
     return original_arr

def dfs(graph, visited, node):
     visited.append(node)
     for neighbor in graph[node]:
          if not neighbor in visited:
               dfs(graph, visited, neighbor)
     return visited
# def dfs(graph, start_node):
#      visited = []
#      while len(visited) < len(graph):
#           dfs_aux(graph, visited, start_node)
#      return visited

# def dfs_aux(graph, visited, node):
#      visited.append(node)
#      for neighbor in graph[node]:
#           if not neighbor in visited:
#                dfs_aux(graph, visited, neighbor)

x = restore_array([[3, 5], [1, 4], [2, 4], [1, 5]])
print(x)