from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Initialize frontier with the root node
        frontier = QueueFrontier()
        frontier.add(root)

        while not frontier.is_empty():
            node = frontier.remove()
 
            # Expandir el nodo y obtener el estado sucesor
            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
 
                # Podar los sucesores cuyo estado ya fue alcanzado
                if successor not in reached:
                    son = Node(
                        "",
                        successor,
                        cost=node.cost + grid.individual_cost(node.state, action),
                        parent=node,
                        action=action,
                    )
 
                    # Aplicar el test objetivo al generar el nodo
                    if grid.objective_test(successor):
                        return Solution(son, reached)
 
                    # Marcar el sucesor como alcanzado y agregarlo a la frontera
                    reached[successor] = True
                    frontier.add(son)

        return NoSolution(reached)