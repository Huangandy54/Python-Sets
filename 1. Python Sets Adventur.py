# Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# 1. Destinations that both airlines fly to.

# 2. Destinations unique to your airline.

# 3. Whether there are any destinations that neither airline shares.

# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def find_shared(our_routes,competitor_routes):
    shared_destination = our_routes.intersection(competitor_routes)
    print(f"Destinations that both airlines fly to: {shared_destination}")
    return shared_destination

def find_unique(our_routes,competitor_routes):
    unique_destination = our_routes.difference(competitor_routes)
    print(f"Destinations that only our airlines fly to: {unique_destination}")
    return unique_destination

def find_neither(our_routes,competitor_routes):
    not_shared_destination = our_routes.symmetric_difference(competitor_routes)
    print(f"Destinations that are not shared: {not_shared_destination}")
    return not_shared_destination

find_shared(our_routes,competitor_routes)
find_unique(our_routes,competitor_routes)
find_neither(our_routes,competitor_routes)