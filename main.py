from problem_temp import SingleFoodSearchProblem
from searchAgents import bfs, dfs, ucs
from problems import SingleFoodSearchProblem

problem = SingleFoodSearchProblem('pacman_single01.txt')
# print('DFS:', dfs(problem))
problem.animate(ucs(problem))

