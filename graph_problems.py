# I will reimplement A BFS to check if a graph is bipartite and if the graph is connected. 
# This Corresponds to the Problem if the Gears will turn correctly and that all the gears will turn. v c
import json


# Create the Graph Data Structure (Actually I have no need, I will just create the list)


# Problems for Interleaving Later 
# Matrix Representation for Graph Representation 
# Representing the Q as a list with append and pop.
# Reading from a json file a list of nodes and edges
# How to Use Version Control To Manage My Projects
# Manage Use of Numpy + computational Tools
# Set up SSH online





#adsfasdfl;jsdfa;dslfjalsk;dfj;lasdjfklj random uncommited file


def solve(graph, starting_node): 

    # I will treat adjacency list as a dictionary
    # added another word
    # I added another word again!
    # added another word

    
    

    nodes = graph[0] + 15
    edges = graph[1]


    # Initialize Attributes of a Node
    visited = [False] * 15
    distances = [0] * 15
    color = [0] * 15


    # Initialize starting node visited = true, distance = 0, color = 0
    
    visited[0] = True
    distances[0] = 0
    color[0] = 0



    # Iterate through the whole loop coloring the nodes either 0 or 1
    
    # index 0 Corresponds to the Front of the Line. 
    q = [nodes[0]]


    while len(q) != 0: 

        node = q.pop(0) 


        for connected_node in edges[node]:

            if visited[connected_node - 1] == False:

                visited[connected_node - 1] = True
                distances[connected_node - 1] = distances[node - 1] + 1 
                color[connected_node - 1] = distances[connected_node - 1] % 2
                q.append(connected_node)

        

    
    # Iterate through all of the edges checking if there is something of the same color (Does the graph have odd cycle ---> Not Bipartite)
    isBipartite = True

    for node, connected_nodes in edges.items():

        for connected_node in connected_nodes: 
            if color[node - 1] == color[connected_node - 1]: 
                isBipartite = False 
                break 


        if not isBipartite: 
            break


    # Iterate through nodes to see if visited. (Is the graph connected?)

    isConnected = True

    for node in nodes: 
        if visited[node - 1] == False: 
            isConnected = False 
            break 

    print(f"Is Connected: {isConnected}, Is Bipartite {isBipartite}")









if __name__ == '__main__': 


    # Ex 1. 


    """
    nodes = [n for n in range(1, 16)]

    edges = {1: [2, 5],
            2: [1, 3, 5],
            3: [2, 4, 6, 7],
            4: [3, 7],
            5: [1, 2, 6, 8, 9],
            6: [3, 5, 7, 10],
            7: [3, 4, 6, 11],
            8: [5, 12],
            9: [5, 12],
            10: [6, 13, 14, 11],
            11: [7, 10, 14, 15],
            12: [8, 9, 13],
            13: [10, 12],
            14: [10, 11, 15],
            15: [11, 14]
            }  

    """

    nodes = [1, 2, 3, 4, 5] 

    edges = {1: [2], 
            2: [3],
            3: [4],
            4: [1], 
           5: []}
    


    with open("graphs.json", "w") as file: 
        json.dump([nodes, edges], file)
        

    with open("graphs.json", "r") as file: 
        name = json.load(file)


    name[1] = {int(i): [x for x in k] for i, k in name[1].items()}



    



        



    graph = (nodes, edges)
    start_node = 1

    solve(graph, start_node) 
    


# I added this comment
# This is the second comment that I added