"""
Utility Classes for Local Search Optimization in TSP

Includes classes for Random Walk initialization and Hill Climbing optimization.
"""
import random


class RandomWalkGenerator:
    """Generates a random walk through all nodes in the graph."""
    
    def __init__(self, graph, seed=None):
        self.graph = graph
        self.random_seed = seed

    def initialize_walk(self):
        """
        Initializes a random walk across the nodes, calculating the total distance.

        Returns:
        - total_cost: Total distance of the walk.
        - node_sequence: Ordered list of node indices representing the walk.
        """
        if self.random_seed is not None:
            random.seed(self.random_seed)

        num_nodes = len(self.graph)
        visited_nodes = set()
        node_sequence = []

        # Choose a random starting point
        current_node = random.randrange(num_nodes)
        node_sequence.append(current_node)
        visited_nodes.add(current_node)

        total_cost = 0

        while len(node_sequence) < num_nodes:
            next_node, min_distance = self._find_next_node(current_node, visited_nodes)
            node_sequence.append(next_node)
            total_cost += min_distance
            visited_nodes.add(next_node)
            current_node = next_node

        total_cost += self.graph[current_node][node_sequence[0]]  # Return to starting point
        return total_cost, node_sequence

    def _find_next_node(self, current_node, visited):
        """Finds the next node with the minimum distance."""
        candidates = [(i, self.graph[current_node][i]) for i in range(len(self.graph)) if i not in visited]
        next_node, min_distance = min(candidates, key=lambda x: x[1])
        return next_node, min_distance


class HillClimbingOptimizer:
    """Explores neighboring solutions to improve the current solution."""

    def __init__(self, graph, seed=None):
        self.graph = graph
        self.random_seed = seed

    def optimize(self, current_cost, current_sequence):
        """
        Searches for a better neighboring solution.

        Parameters:
        - current_cost: Cost of the current solution.
        - current_sequence: Current sequence of nodes.

        Returns:
        - new_cost: Updated cost of the solution (if improved).
        - new_sequence: Updated sequence of nodes.
        """
        if self.random_seed is not None:
            random.seed(self.random_seed)

        idx1, idx2 = self._select_random_indices(len(current_sequence))
        new_sequence = current_sequence[:]
        new_sequence[idx1], new_sequence[idx2] = new_sequence[idx2], new_sequence[idx1]  # Swap nodes

        new_cost = self._calculate_total_cost(new_sequence)

        return (new_cost, new_sequence) if new_cost < current_cost else (current_cost, current_sequence)

    def _select_random_indices(self, size):
        """Selects two unique random indices."""
        idx1 = random.randrange(size)
        idx2 = random.randrange(size)
        while idx2 == idx1:
            idx2 = random.randrange(size)
        return idx1, idx2

    def _calculate_total_cost(self, sequence):
        """Calculates the total cost of the given sequence."""
        return sum(self.graph[sequence[i]][sequence[i + 1]] for i in range(len(sequence) - 1)) + \
               self.graph[sequence[-1]][sequence[0]]
