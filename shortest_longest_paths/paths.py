"""
Name: Alyssa Kelley

Disclaimer:

This is my own work and absolutly no code was copied. 
I did discuss this project with Anne Glickenhaus (classmate).
I also used the following links to better my understanding for
concepts such as ***********:

https://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/
"""

import sys
from collections import defaultdict 

def main():

	input_file = sys.stdin

	graph = defaultdict(list) # this is a dictionary which holds the adjacency Lists.
	# example: {1: [2, 3, 4, 5]} 

	# first line = N which is the number of nodes
	num_of_nodes = int(input_file.readline()) # should read the first line then skip it to the next

	# second line = M which is the number of edges
	num_of_edges = int(input_file.readline()) # should read the second line then skip it to the next

	for line in input_file: # should start with the num pairs indicating the edges
		# the next lines will be for M indicates edges between num1 and num2 on that line
		line = line.rstrip('\n')
		line = line.split()

		node_1 = int(line[0]) # these will be the nodes that have a joining edge
		node_2 = int(line[1])

		add_to_edges(graph, node_1, node_2)

	current_path = []

	total_paths = create_possible_paths(graph, 1, num_of_nodes, current_path)

	shortest_len = find_len_shortest_path(total_paths)
	longest_len = find_len_longest_path(total_paths)
	
	total_amount_of_short_paths = how_many_short_paths(total_paths, shortest_len)
	total_amount_of_long_paths = how_many_long_paths(total_paths, longest_len)

	print("Shortest path: ", shortest_len)
	print("Number of short paths: ", total_amount_of_short_paths)

	print("Longest path: ", longest_len)
	print("Number of long paths: ", total_amount_of_long_paths)

	# ---- printing all the paths ----
	# print_all_paths(total_paths)

def add_to_edges(graph, node_1, node_2):
	# this function adds the edge to the graph
	graph[node_1].append(node_2)


def create_possible_paths(graph, current_node, num_of_nodes, current_path):
	"""
	This function creates a nested list which is all of the paths. Each path is 
	stored as a separate list. This function was inspired by the tologicalsort from
	geeksforgeeks which is linked at the top of this program.

	We keep track of the current path and add the next node 
	"""
	current_path = current_path + [current_node]

	if current_node == num_of_nodes:
		return [current_path]

	total_paths = []

	#print(graph[current_node])

	for node in graph[current_node]:
		if node not in current_path:
			new_path = create_possible_paths(graph, node, num_of_nodes, current_path)

		for new_node in new_path:
			total_paths.append(new_node)

	return total_paths


def find_len_shortest_path(total_paths):
	"""
	This function goes through the total paths list that was created in another function
	and it loops through the entire nested list and compares the lengths to each other
	and keeps track of the length of the shortest path, and that is the int returned.
	"""
	len_shortest_path = len(total_paths[0])

	for path in range(len(total_paths)):
		current_len = len(total_paths[path])
		if current_len < len_shortest_path:
			len_shortest_path = current_len

	return (len_shortest_path - 1) # -1 to alot for starting at 0


def find_len_longest_path(total_paths):
	"""
	This function goes through the total paths list that was created in another function
	and it loops through the entire nested list and compares the lengths to each other
	and keeps track of the length of the longest path, and that is the int returned.
	"""
	len_longest_path = len(total_paths[0])

	for path in range(len(total_paths)):
		current_len = len(total_paths[path])
		if current_len > len_longest_path:
			len_longest_path = current_len

	return (len_longest_path - 1) # -1 to alot for starting at 0


def how_many_short_paths(total_paths, shortest_len):
	"""
	This function will go through the total paths nested list and if the len of a 
	path is equal to the smallest length, then it increments the number of shortest
	paths which it will then return that counter. 
	"""
	num_of_shortest_paths = 0

	for i in range(len(total_paths)):
		if (len(total_paths[i]) == shortest_len+1):
			num_of_shortest_paths += 1

	return num_of_shortest_paths

def how_many_long_paths(total_paths, longest_len):
	"""
	This function will go through the total paths nested list and if the len of a 
	path is equal to the longest length, then it increments the number of longest
	paths which it will then return that counter. 
	"""
	num_of_longest_paths = 0
	
	for i in range(len(total_paths)):
		if (len(total_paths[i]) == longest_len+1):
			num_of_longest_paths += 1

	return num_of_longest_paths

def print_all_paths(total_paths):
	""" 
	This function is not part of the project spec, but will go through the
	nested list and print each path (list) on separate lines for clarity. 
	"""
	for i in range(len(total_paths)):
		print(total_paths[i])


if __name__ == "__main__":
	main()