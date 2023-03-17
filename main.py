from problem_temp import *
from searchAgents import bfs, dfs, ucs
from problems import *

problem = SingleFoodSearchProblem('pacman_single01.txt')
multifood_problem = MultiFoodSearchProblem('pacman_multi01.txt')
print('DFS:', dfs(multifood_problem))
#multifood_problem.animate(dfs(multifood_problem))

