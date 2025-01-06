#implementing searching DFS
G = {'Biratnagar': {'Rangeli': 25, 'Itahari': 22, 'Biratchowk': 30},

     'Rangeli': {'Biratnagar': 25, 'Kanepokhari': 25, 'Urlabari': 40},

     'Itahari': {'Biratnagar': 22, 'Biratchowk': 11, 'Dharan': 30},

     'Dharan': {'Itahari': 22, },

     'Biratchowk': {'Biratnagar': 30, 'Itahari': 11, 'Kanepokhari': 10},

     'Kanepokhari': {'Rangeli': 25, 'Biratchowk': 10, 'Urlabari': 12},

     'Urlabari': {'Rangeli': 40, 'Kanepokhari': 12, 'Damak': 6},

     'Damak': {'Urlabari': 6, },
    }
start = 'Biratnagar'
goal = 'Kanepokhari'


    
def dfs(G, initial_state, goal_state):
    stack = []
    prev = {}
    visited = set()
    stack.append(initial_state)
    prev[initial_state] = " "  # Mark the start node

    while stack:
        node = stack.pop()
        visited.add(node)

        if node == goal_state:
            return True, prev

        for neighbor in G[node]:
            if neighbor not in visited:
                stack.append(neighbor)
                prev[neighbor] = node

    return False, prev

def pathBana(G, prev, goal):
    path = goal
    while( prev[goal] != " "):
        path = prev[goal]+ '->'+ path
        goal = prev[goal]
    return path

# def reconstruct_path(prev, start, goal):
#     if goal not in prev:
#         return []  # No path found

#     path = []
#     current = goal
#     while current != start:
#         path.append(current)
#         current = prev[current]
#     path.append(start)
#     path.reverse()
#     return path
goalFound, prev  = dfs(G, start, goal)

if goalFound:
    print("Goal found")
    print(prev)
    path = pathBana(G, prev, goal)
    print(path)
else:
    print("Goal not found")

