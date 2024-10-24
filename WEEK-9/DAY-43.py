from collections import defaultdict, deque

def find_order(num_courses, prerequisites):
    # Create a graph represented as an adjacency list
    graph = defaultdict(list)
    # Array to keep track of the in-degree (number of prerequisites) for each course
    in_degree = [0] * num_courses

    # Build the graph and calculate in-degrees
    for course, prereq in prerequisites:
        graph[prereq].append(course)  # Add the course to the adjacency list of its prerequisite
        in_degree[course] += 1  # Increment the in-degree for the course

    # Initialize the queue with all courses having no prerequisites (in-degree of 0)
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []  # List to store the order of courses

    # Process the courses in the queue
    while queue:
        course = queue.popleft()  # Get the course from the front of the queue
        order.append(course)  # Add it to the order
        # Decrease the in-degree for all its dependent courses
        for next_course in graph[course]:
            in_degree[next_course] -= 1  # Remove the prerequisite
            if in_degree[next_course] == 0:  # If no more prerequisites, add to queue
                queue.append(next_course)

    # Check if all courses are included in the order; if not, return an empty list (cycle detected)
    return order if len(order) == num_courses else []

# Default Input
num_courses = 4
prerequisites = [[2, 0], [1, 0], [3, 1], [3, 2]]
# Run the function with the default input
result = find_order(num_courses, prerequisites)
print(f"Course order: {result}")
