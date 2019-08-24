

Need to have:
1. Main function that executes the library
2. Function for performing the optimization
3. Class for an environment simulation



Methods that I will consider:
1. Graph theory approach

- Shortest path for visiting all nodes
- define a graph and connections based on the aircraft's search capability
- define the edge weights based on the distance between each node in real life
- Use breadthfirst search to traverse the graph and find the shortest path through all nodes (https://leetcode.com/articles/shortest-path-visiting-all-nodes/)

2. Genetic Algorithm Approach

-Using a better initial scneario and condition can improve run time
-Segment the search region into spaces (for each vehicle), and create a path that guarentees that the area is searched to begin with
-Starting froma  feasible region can help avoid the entire population dying off
-Filtering population should not filter off all the infeasible cases (in case of them is close to an optimal solution)

3. Machine Learning Approach



















