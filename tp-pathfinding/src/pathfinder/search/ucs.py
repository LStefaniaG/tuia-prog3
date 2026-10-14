from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root, root.cost)
 
        while not frontier.is_empty():
            # Sacar de la frontera el nodo con menor costo de camino
            node = frontier.pop()
 
            # Aplicar el test objetivo al sacar el nodo de la frontera
            if grid.objective_test(node.state):
                return Solution(node, reached)
 
            # Expandir el nodo
            for action in grid.actions(node.state):
                # Obtener el estado sucesor y su costo de camino
                successor = grid.result(node.state, action)
                new_cost = node.cost + grid.individual_cost(node.state, action)
 
                # Conservar el sucesor si es nuevo o si se alcanzó con menor costo
                if successor not in reached or new_cost < reached[successor]:
                    son = Node(
                        "",
                        successor,
                        cost=new_cost,
                        parent=node,
                        action=action,
                    )
 
                    # Actualizar el mejor costo conocido y agregar el hijo a la frontera
                    reached[successor] = new_cost
                    frontier.add(son, priority=new_cost)
 
        return NoSolution(reached)