from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # Initialize frontier with the root node
        if grid.objective_test(root.state):
            return Solution(root, expanded)
 
        # Inicializamos la frontera con el nodo raíz (pila LIFO)
        frontier = StackFrontier()
        frontier.add(root)
 
        while not frontier.is_empty():
            # Sacar de la frontera el nodo de mayor profundidad
            node = frontier.remove()
 
            # Saltear el nodo si su estado ya fue expandido
            if node.state in expanded:
                continue

            expanded[node.state] = True
 
            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
 
                # Generar solo los sucesores cuyo estado no fue expandido
                if successor not in expanded:
                    son = Node(
                        "",
                        successor,
                        cost=node.cost + grid.individual_cost(node.state, action),
                        parent=node,
                        action=action,
                    )
 
                    # Aplicar el test objetivo al generar el nodo
                    if grid.objective_test(successor):
                        return Solution(son, expanded)
 
                    frontier.add(son)
 
        return NoSolution(expanded)