import sys
from os import abort
path = __file__[:-13] + "//Structures"
sys.path.append(path)

from Structures.Graph import Graph

def testAdd():
    graph = Graph()
    graph.addVertex(3)
    assert graph._Graph__list.index(0).index(0).item == 3, f"In first vertex incorrect value, {graph._Graph__list.index(0).index(0).item}"
    
    graph.addVertex(5)
    assert graph._Graph__list.index(1).index(0).item == 5, f"In second vertex incorrect value, {graph._Graph__list.index(1).index(0).item}"

    graph.addEdges(0, 1)
    assert graph._Graph__list.index(0).index(1).item == 1, f"In edges between 0 and 1 error"
    assert graph._Graph__list.index(1).index(1).item == 0, f"In edges between 0 and 1 error"

    graph.addVertex("VALUE")
    assert graph._Graph__list.index(2).index(0).item == "VALUE", f"In third vertex incorrect value, {graph._Graph__list.index(2).index(0).item}"

    graph.addEdges(0, 2)
    assert graph._Graph__list.index(0).index(2).item == 2, f"In edges between 0 and 2 error"
    assert graph._Graph__list.index(2).index(1).item == 0, f"In edges between 0 and 2 error"

    graph.addEdges(2, 1)
    assert graph._Graph__list.index(2).index(2).item == 1, f"In edges between 2 and 1 error"
    assert graph._Graph__list.index(1).index(2).item == 2, f"In edges between 2 and 1 error"

    try:
        graph.addEdges(2, 3)
        print("Error in try-except (indices)")
        abort()

    except:
        pass

    try:
        graph.addEdges(3, 2)
        print("Error in try-except (main index)")
        abort()

    except:
        pass

    try:
        graph.addEdges(2, 2)
        print("Error in try-except (connect to itself)")
        abort()

    except:
        pass

    try:
        graph.addEdges(2, 1)
        print("Error in try-except (already connected)")
        abort()

    except:
        pass

    for i in range(4):
        graph.addVertex(i + 6)
        assert graph._Graph__list.index(i + 3).index(0).item == i + 6, f"In for-loop vertex №{i} incorrect value, {graph._Graph__list.index(i + 3).index(0).item}"

    graph.addEdges(4, 0, 1, 2, 3)
    assert graph._Graph__list.index(4).index(1).item == 0, f"In edges between 4 and 0 error"
    assert graph._Graph__list.index(4).index(2).item == 1, f"In edges between 4 and 1 error"
    assert graph._Graph__list.index(4).index(3).item == 2, f"In edges between 4 and 2 error"
    assert graph._Graph__list.index(4).index(4).item == 3, f"In edges between 4 and 3 error"

    graph.addEdges(5, 6, 2)
    assert graph._Graph__list.index(5).index(1).item == 6, f"In edges between 5 and 6 error"
    assert graph._Graph__list.index(5).index(2).item == 2, f"In edges between 5 and 2 error"
    
    print("Test (add) completed")


testAdd()