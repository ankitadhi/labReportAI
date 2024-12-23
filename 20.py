def makeAGraph():
    G = {
        'A':['B', 'C'],
        'B':['A', 'D', 'E'],
        'C':['A', 'F'],
        'D':['B', 'G'],
        'E':['B', 'H'],
        'F':['C']
    }

    print(G['A'])
makeAGraph()