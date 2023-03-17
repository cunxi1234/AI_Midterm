import problems
import fringes
import numpy as np

problem = problems.SingleFoodSearchProblem("pacman_single01.txt")
queue = fringes.Queue()
priorityQueue = fringes.PriorityQueue()

def bfs(problem):
    path = queue
    visited = set()
    start_state = problem.initial_state
    path.enqueue((start_state, []))
    while not path.is_empty():
        state, actions = path.dequeue()
        if problem.goal_test(state):
            actions.append("Stop")
            return actions
        visited.add(state)
        for successor, action in problem.successor(state):
            if successor not in visited:
                path.enqueue((successor, actions + [action]))
    return None

def dfs(problem):
    path = queue
    visited = set()
    start_state = problem.initial_state
    path.enqueue((start_state, []))
    while not path.is_empty():
        state, actions = path.dequeue()
        if problem.goal_test(state):
            actions.append("Stop")
            return actions
        visited.add(state)
        for successor, action in problem.successor(state):
            if successor not in visited:
                path.enqueue((successor, actions + [action]))
    return None


def ucs(problem):
    path = priorityQueue
    visited = set()
    start_state = problem.initial_state
    path.enqueue((start_state, []), 0)
    while not path.is_empty():
        state, actions = path.dequeue()
        if problem.goal_test(state):
            actions.append("Stop")
            return actions
        visited.add(state)
        for successor, action in problem.successor(state):
            if successor not in visited:
                cost = problem.path_cost(actions + [action])
                path.enqueue((successor, actions + [action]), cost)
            if any(np.array_equal(successor, item[1]) for item in path.items):
                cost = problem.path_cost(actions + [action])
                path.remove((successor, actions))
                path.enqueue((successor, actions + [action]), cost)
    return None

