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
        if isinstance(problem.foods, list):
            if problem.goal_test(state):
                problem.foods.remove(state)
                if len(problem.foods) == 0:
                    actions.append("Stop")
                    return actions
                else:
                    start_state = state
                    #TODO:
        elif problem.goal_test(state):
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


# YC2-1
def manhattan_distance(state, goal_pos):
    return abs(state[0] - goal_pos[0]) + abs(state[1] - goal_pos[1])


def euclidean_distance(state, goal_pos):
    return ((state[0] - goal_pos[0]) ** 2 + (state[1] - goal_pos[1]) ** 2) ** 0.5


# 1 hàm được gọi là admissible khi nó không bao giờ đánh giá cao chi phí để từ current state đến goal state. cả 2 hàm manhattan_distance và euclidean_distance đều tính
# path cost là khoảng cách ngắn nhất tức 1 đường thẳng nối liền 2 điểm nên kết quả path cost nó trả về luôn ít hơn hoặc bằng với chi phí thật sự -> cả 2 hàm đều có tính
# admissible

# 1 hàm được gọi là consistent khi thoả mãn: ở bất kì state s, mọi successor s' và cost c để đi từ s tới s', cost ước tính để đến goal state của s luôn nhỏ hơn hoặc bằng
# cost để đến goal state từ s' cộng với cost c từ s tới s'.
# VD: Nếu khoảng cách hàm manhattan trả về từ 1 state s tới goal state là h(s), và khoảng cách Manhattan từ 1 successor s' đến goal cộng với cost c từ s đến s' là h(s') + c
# thì luôn luôn h(s) <= h(s') + c.
# Ta có thể thấy rõ cả 2 hàm manhattan_distance và euclidean_distance => cả 2 đều có tính consistent

# YC2-2
def multi_heuristic(state, goals):
    distances = [manhattan_distance(state, goal) for goal in goals]
    return min(distances) if distances else 0


# YC2-3
def astar(problem, fn_heuristic):
    path = priorityQueue
    visited = set()
    start_state = problem.initial_state
    path_cost = 0
    heuristic_cost = fn_heuristic(start_state, problem.goal_pos)
    path.enqueue((start_state, [], path_cost), heuristic_cost)

    while not path.is_empty():
        state, actions, path_cost = path.dequeue()
        if problem.goal_test(state):
            actions.append("Stop")
            return actions
        visited.add(state)
        for successor, action in problem.successor(state):
            if successor not in visited:
                new_path_cost = path_cost + problem.path_cost(actions + [action])
                heuristic_cost = fn_heuristic(successor, problem.goal_pos)
                total_cost = new_path_cost + heuristic_cost
                path.enqueue((successor, actions + [action], new_path_cost), total_cost)
    return None