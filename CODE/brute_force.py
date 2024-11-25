"""
Brute-force implementation for solving the TSP with a time cut-off.
"""

from tsp_utils import read_tsp_file, total_distance, euclidean_distance
import itertools
import time
import math

def brute_force_tsp(points, time_limit):
    start_time = time.time()
    n = 0
    best_route = None
    best_cost = float('inf')
    
    for perm in itertools.permutations(range(len(points))):
        n += 1
        if time.time() - start_time > time_limit:
            print(f"Time limit of {time_limit} seconds reached. Exiting...")
            break
        current_cost = total_distance(perm, points)
        if current_cost < best_cost:
            best_cost = current_cost
            best_route = perm
    print(f"{round(100*n/math.factorial(len(points)), 3)}% search space explored. ({n} out of {math.factorial(len(points))})")
    return best_route, best_cost
