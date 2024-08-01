# Objective: The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.

# Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove duplicates and display the unique customer IDs.

# Example Code:

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
# Expected Outcome: A set of unique customer IDs, ensuring no duplicates. For instance, `{'C001', 'C002', 'C003', 'C004'}`. ---

# NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs.

# The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.

unique_customer_ids= set(customer_ids)
print(customer_ids)
print(unique_customer_ids)