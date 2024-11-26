import random
city_list = ["Atlanta.tsp", "Champaign.tsp", "NYC.tsp", "SanFrancisco.tsp", "UMissouri.tsp",
        "Berlin.tsp", "Cincinnati.tsp", "Philadelphia.tsp", "Toronto.tsp",
        "Boston.tsp", "Denver.tsp", "Roanoke.tsp", "UKansasState.tsp"]


selected_city = random.choice(city_list)
print(f"Selected city: {selected_city.split('.')[0]}")
points = read_tsp_file(f"/content/CSE6104-TSP/DATA/{selected_city}")

# Brute Force
time_limit = 60  
best_route, best_cost = brute_force_tsp(points, time_limit)
print("Best route found (bruteforce):", best_route)
print("Best cost (bruteforce):", round(best_cost, 2))


# Approximate
best_route, best_cost = mst_tsp_approximation(points)
print("Best route found (approximate):", best_route)
print("Best cost (approximate):", round(best_cost, 2))   


"""
# Local Search
best_route, best_cost = local_search_tsp(points)
print("Best route found (local search):", best_route)
print("Best cost (local search):", round(best_cost, 2))   
"""
