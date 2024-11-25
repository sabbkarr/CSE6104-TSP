"""
tsp_utils.py

This file contains utility functions for parsing TSP problem input files
and calculating distances for the Traveling Salesman Problem (TSP).

Functions:
- read_tsp_file(file_path): Parses a TSP file and extracts node coordinates.
- euclidean_distance(point1, point2): Computes the Euclidean distance between two points.
- total_distance(route, points): Computes the total distance of a TSP route.

Usage:
Import this file into your TSP solution files to reuse these utility functions,
avoiding redundancy across different TSP solution approaches. E.g.,
import sys
sys.path.append("PATH_TO_THIS_DIRECTORY")
from tsp_utils import read_tsp_file, total_distance, euclidean_distance

Outputs:
- Coordinates of nodes in Python list (parsed from TSP files)
- Distance calculations for TSP routes
"""

import math

def read_tsp_file(file_path): # Parse the TSP file and extract node coordinates.
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [(float(parts[1]), float(parts[2]))
            for line in lines if "NODE_COORD_SECTION" in line or "EOF" not in line
            for parts in [line.strip().split()] if parts[0].isdigit()]

def euclidean_distance(point1, point2): # Calculate the Euclidean distance between two points.
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def total_distance(route, points): # Calculate the total distance of a route.
    return sum(euclidean_distance(points[route[i]], points[route[i+1]]) for i in range(len(route) - 1)) + euclidean_distance(points[route[-1]], points[route[0]])
