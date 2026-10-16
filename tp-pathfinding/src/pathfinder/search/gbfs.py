from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        reached = {}
        reached[root.state] = root.cost

        frontier = PriorityQueueFrontier()
        frontier.add(root, priority= abs(root.state[0] - grid.end[0]) + abs(root.state[1] - grid.end[1]))
 
        while not frontier.is_empty():
            node = frontier.pop()
 
            if grid.objective_test(node.state):
                return Solution(node, reached)
 
            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
                new_cost = node.cost + grid.individual_cost(node.state, action)
 
                if successor not in reached or new_cost < reached[successor]:
                    son = Node(
                        "",
                        successor,
                        cost=new_cost,
                        parent=node,
                        action=action,
                    )
 
                    reached[successor] = new_cost
                    frontier.add(son, priority=abs(successor[0] - grid.end[0]) + abs(successor[1] - grid.end[1]))
 
        return NoSolution(reached)