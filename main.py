from searchAgents import bfs, dfs, ucs
import problems

single_food =  problems.SingleFoodSearchProblem('pacman_single01.txt')
multifood_problem = problems.MultiFoodSearchProblem('pacman_multi01.txt')
print('DFS:', dfs(multifood_problem))
#multifood_problem.animate(dfs(multifood_problem))

eight_queen = problems.EightQueenProblem.read_file('eight_queens01.txt')

print('Initial state')
initial_state = eight_queen.print_board()
print(initial_state)

conflict = eight_queen.h()
print('Total conflicts: ', conflict)
print()

solution = eight_queen.hill_climbing_search()
eight_queen.print_board(solution)