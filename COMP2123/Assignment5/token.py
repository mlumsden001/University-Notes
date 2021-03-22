def token(G,T):
    #Using BFS
    for u in G.vertices():
        seen[u] = False
        parent[u] = None
        
    seen[G.vertices[0]] = True
    layers = []
    current = [G.vertices[0]]
    next_node = []
    
    while not T.is_empty():
        layers.append(current)
        for u in current:
            for b in G.incident(u):
                if b not in seen[v]:
                    next_node.append(v)
                    seen[v] = True
                    parent[v] = u
                    key(parent[v]) = T[0]
                    T.remove[0]
        
        current = next_node
        next_node = []
        
    #Check if each node incident of a node has a different token
    for u in layers: 
        for i in G.incident(u):
            if key(i) == key(u):
                return None
    
    return layers