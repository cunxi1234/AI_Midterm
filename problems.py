import os
import numpy as np
import re

class SingleFoodSearchProblem:
    def __init__(self, input_file):
        self.input_file = input_file
        self.load_input()

    #Đọc mê cung từ tệp
    def load_input(self):
        with open(self.input_file, 'r') as f:
            input_data = f.readlines()

        input_layout = []
        for line in input_data:
            if re.match("^[%. P]+$", line.strip()):
                input_layout.append(list(line.strip()))

        #Chuyển input layout sang mảng numpy
        self.input_array = np.array(input_layout)

        #Vị trí ban đầu của Pac-man
        start_pos = np.argwhere(self.input_array == 'P')[0]
        #Vị trí của mồi
        end_pos = np.argwhere(self.input_array == '.')[0]
        #Initial state
        self.initial_state = tuple(start_pos)

        #Goal position
        self.goal_pos = tuple(end_pos)

    def successor(self, state):
        successors = []
        x, y = state 

        for action in ['N', 'S', 'E', 'W']:
            if action == 'N' and x > 0 and self.input_array[x-1][y] != '%':
                successors.append(((x-1, y), action))
            elif action == 'S' and x < len(self.input_array)-1 and self.input_array[x+1][y] != '%':
                successors.append(((x+1, y), action))
            elif action == 'W' and y > 0 and self.input_array[x][y-1] != '%':
                successors.append(((x, y-1), action))
            elif action == 'E' and y < len(self.input_array[x])-1 and self.input_array[x][y+1] != '%':
                successors.append(((x, y+1), action))
        return successors

    def goal_test(self, state):
        return state == self.goal_pos

    def path_cost(self, actions):
        return len(actions)
    
    #In mê cung ra màn hình
    def print_input(self):
        for line in self.input_array:
            print(''.join(line))

    def animate(self,action) -> None:
        if action != 'Stop':
            os.system('cls')
            self.print_input()
            self.initial_state

            input()
            for i in action:
                os.system('cls')
                if i == 'Stop':
                    self.print_input()
                    print("Congratulations!")
                    break
                #self.state[self.init_state[0]] = update(self.state[self.init_state[0]], self.init_state[1], ' ')
                # self.input_array[self.initial_state]  #update(self.input_array, self.initial_state[0], ' ')
                if i == 'N':
                    self.input_array[self.initial_state] = ' '
                    new_pacman_pos = (self.initial_state[0]-1,self.initial_state[1])
                    self.input_array[new_pacman_pos] = "P"
                    self.initial_state= new_pacman_pos
                if i == 'S':
                    self.input_array[self.initial_state] = ' '
                    new_pacman_pos = (self.initial_state[0]+1,self.initial_state[1])
                    self.input_array[new_pacman_pos] = "P"
                    self.initial_state= new_pacman_pos
                if i == 'E':
                    self.input_array[self.initial_state] = ' '
                    new_pacman_pos = (self.initial_state[0], self.initial_state[1]+1)
                    self.input_array[new_pacman_pos] = "P"
                    self.initial_state = new_pacman_pos
                if i == 'W':
                    self.input_array[self.initial_state] = ' '
                    new_pacman_pos = (self.initial_state[0], self.initial_state[1]-1)
                    self.input_array[new_pacman_pos] = "P"
                    self.initial_state = new_pacman_pos
                self.print_input()
                input()

        else:

            print('Path is not found.')

