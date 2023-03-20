import os
import numpy as np
import re


class SingleFoodSearchProblem:
    def __init__(self, input_file):
        self.input_file = input_file
        self.load_input()

    # Đọc mê cung từ tệp
    def load_input(self):
        with open(self.input_file, 'r') as f:
            input_data = f.readlines()

        input_layout = []
        for line in input_data:
            if re.match("^[%. P]+$", line.strip()):
                input_layout.append(list(line.strip()))

        # Chuyển input layout sang mảng numpy
        self.input_array = np.array(input_layout)

        # Vị trí ban đầu của Pac-man
        start_pos = np.argwhere(self.input_array == 'P')[0]
        # Vị trí của mồi
        end_pos = np.argwhere(self.input_array == '.')[0]
        # Initial state
        self.initial_state = tuple(start_pos)

        # Goal position
        self.goal_pos = tuple(end_pos)

    def successor(self, state):
        successors = []
        x, y = state

        for action in ['N', 'S', 'E', 'W']:
            if action == 'N' and x > 0 and self.input_array[x - 1][y] != '%':
                successors.append(((x - 1, y), action))
            elif action == 'S' and x < len(self.input_array) - 1 and self.input_array[x + 1][y] != '%':
                successors.append(((x + 1, y), action))
            elif action == 'W' and y > 0 and self.input_array[x][y - 1] != '%':
                successors.append(((x, y - 1), action))
            elif action == 'E' and y < len(self.input_array[x]) - 1 and self.input_array[x][y + 1] != '%':
                successors.append(((x, y + 1), action))
        return successors

    def goal_test(self, state):
        return state == self.goal_pos

    def path_cost(self, actions):
        return len(actions)

    # In mê cung ra màn hình
    def print_input(self):
        for line in self.input_array:
            print(''.join(line))

    def animate(self, action) -> None:
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
                # self.state[self.init_state[0]] = update(self.state[self.init_state[0]], self.init_state[1], ' ')
                # self.input_array[self.initial_state]  #update(self.input_array, self.initial_state[0], ' ')
                if i == 'N':
                    self.input_array[self.initial_state] = ' '
                    new_pacman_pos = (self.initial_state[0] - 1, self.initial_state[1])
                    self.input_array[new_pacman_pos] = "P"
                    self.initial_state = new_pacman_pos
                if i == 'S':
                    self.input_array[self.initial_state] = ' '
                    new_pacman_pos = (self.initial_state[0] + 1, self.initial_state[1])
                    self.input_array[new_pacman_pos] = "P"
                    self.initial_state = new_pacman_pos
                if i == 'E':
                    self.input_array[self.initial_state] = ' '
                    new_pacman_pos = (self.initial_state[0], self.initial_state[1] + 1)
                    self.input_array[new_pacman_pos] = "P"
                    self.initial_state = new_pacman_pos
                if i == 'W':
                    self.input_array[self.initial_state] = ' '
                    new_pacman_pos = (self.initial_state[0], self.initial_state[1] - 1)
                    self.input_array[new_pacman_pos] = "P"
                    self.initial_state = new_pacman_pos
                self.print_input()
                input()  # Enter sau mỗi lần lặp để render ra scene mới

        else:

            print('Path is not found.')


class MultiFoodSearchProblem:
    def __init__(self, input_file):
        self.input_file = input_file
        self.load_input()

    def load_input(self):
        with open(self.input_file, 'r') as f:
            input_data = f.readlines()
        food = []
        input_layout = []
        for line in input_data:
            if re.match("^[%. P]+$", line.strip()):
                input_layout.append(list(line.strip()))

        # Chuyển input layout sang mảng numpy
        self.input_array = np.array(input_layout)

        # Vị trí ban đầu của Pac-man
        start_pos = np.argwhere(self.input_array == 'P')[0]
        # Initial state
        self.initial_state = tuple(start_pos)

        # Tất cả vị trí của mồi, list contain element type of tuple
        foods = np.argwhere(self.input_array == '.')
        self.foods = [tuple(food) for food in foods]

    def successor(self, state):
        successors = []
        x, y = state

        for action in ['N', 'S', 'E', 'W']:
            if action == 'N' and x > 0 and self.input_array[x - 1][y] != '%':
                successors.append(((x - 1, y), action))
            elif action == 'S' and x < len(self.input_array) - 1 and self.input_array[x + 1][y] != '%':
                successors.append(((x + 1, y), action))
            elif action == 'W' and y > 0 and self.input_array[x][y - 1] != '%':
                successors.append(((x, y - 1), action))
            elif action == 'E' and y < len(self.input_array[x]) - 1 and self.input_array[x][y + 1] != '%':
                successors.append(((x, y + 1), action))
        return successors

    def print_input(self):
        for line in self.input_array:
            print(''.join(line))

    def goal_test(self, state):
        if state in self.foods:
            return True
        else:
            return False

    def initial_state(self):
        return self.start_state

    def path_cost(self, actions):
        return len(actions)

    def animate(self, actions):
        if actions != 'Stop':
            os.system('cls')
            self.print_input()
            self.initial_state
            input()
            for i in actions:
                os.system('cls')
                if i == 'Stop':
                    self.print_input()
                    print("Congratulations!")
                    break
                # self.state[self.init_state[0]] = update(self.state[self.init_state[0]], self.init_state[1], ' ')
                # self.input_array[self.initial_state]  #update(self.input_array, self.initial_state[0], ' ')
                if i == 'N':
                    self.input_array[self.initial_state] = ' '
                    new_pacman_pos = (self.initial_state[0] - 1, self.initial_state[1])
                    self.input_array[new_pacman_pos] = "P"
                    self.initial_state = new_pacman_pos
                if i == 'S':
                    self.input_array[self.initial_state] = ' '
                    new_pacman_pos = (self.initial_state[0] + 1, self.initial_state[1])
                    self.input_array[new_pacman_pos] = "P"
                    self.initial_state = new_pacman_pos
                if i == 'E':
                    self.input_array[self.initial_state] = ' '
                    new_pacman_pos = (self.initial_state[0], self.initial_state[1] + 1)
                    self.input_array[new_pacman_pos] = "P"
                    self.initial_state = new_pacman_pos
                if i == 'W':
                    self.input_array[self.initial_state] = ' '
                    new_pacman_pos = (self.initial_state[0], self.initial_state[1] - 1)
                    self.input_array[new_pacman_pos] = "P"
                    self.initial_state = new_pacman_pos
                self.print_input()
                input()  # Enter sau mỗi lần lặp để render ra scene mới

        else:

            print('Path is not found.')


class EightQueenProblem:
    # constructor
    def __init__(self, board):
        self.board = board
        self.size = len(board)

    # read file from sample input
    @classmethod
    def read_file(cls, file_path):
        with open(file_path) as f:
            board = [line.strip().split() for line in f.readlines()]
        return cls(board)

    def print_board(self, board=None):
        if board is None:
            board = self.board
        print('\n'.join([' '.join(row) for row in board]))

    def h(self, board=None):
        if board is None:
            board = self.board
        attacks = 0
        # tạo 2 vòng lặp để tìm kiếm Q
        for row in range(self.size):
            for col in range(self.size):
                # nếu tìm được thì tiếp tục
                if board[row][col] == 'Q':
                    # lặp qua từng hàng và cột của bàn cờ
                    for i in range(self.size):
                        # kiểm tra Q có đang ở cùng cột hay không
                        if board[row][i] == 'Q' and i != col:
                            # có thì kiểm tra xem có giống với Q hiện tại hay không, không thì +1 attack giữa 2 Q
                            attacks += 1
                        # kiểm tra Q có đang ở cùng hàng hay không
                        if board[i][col] == 'Q' and i != row:
                            # có thì kiểm tra xem có giống với Q hiện tại hay không, không thì +1 attack giữa 2 Q
                            attacks += 1
                    # kiểm tra từ các đường chéo đi lên và sang trái từ Q hiện tại
                    # dùng function zip để kiểm tra cùng lúc 2 phạm vi tìm kiếm trong một lần (lên đầu bảng và cạnh trái của bảng)
                    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                        # nếu một Q được tìm thấy trong đường chéo thì +1 attack
                        if board[i][j] == 'Q':
                            attacks += 1
                    # kiểm tra từ các đường chéo đi lên và sang phải từ Q hiện tại
                    for i, j in zip(range(row - 1, -1, -1), range(col + 1, self.size)):
                        # nếu một Q được tìm thấy trong đường chéo thì +1 attack
                        if board[i][j] == 'Q':
                            attacks += 1
                    # kiểm tra các đường chéo đi xuống và sang trái từ Q hiện tại.
                    for i, j in zip(range(row + 1, self.size), range(col - 1, -1, -1)):
                        # nếu một Q được tìm thấy trong đường chéo thì +1 attack
                        if board[i][j] == 'Q':
                            attacks += 1
                    # kiểm tra các đường chéo đi xuống và sang phải từ Q hiện tại.
                    for i, j in zip(range(row + 1, self.size), range(col + 1, self.size)):
                        # nếu một Q được tìm thấy trong đường chéo thì +1 attack
                        if board[i][j] == 'Q':
                            attacks += 1
        return attacks // 2

    def hill_climbing_search(self):
        # khởi tạo bàn cờ từ file đọc
        current_board = self.board
        # gọi hàm h để tính số lượng xung đột giữa các Q trong bàn cờ và gán vào biến current_conflict
        current_conflict = self.h(current_board)
        while True:
            # khởi tạo bảng trống để lưu trữ
            neighbors = []
            # 2 vòng lặp for tìm kiếm Q
            for row in range(self.size):
                for col in range(self.size):
                    # nếu ô này tìm được Q thì đi tiếp
                    if current_board[row][col] == 'Q':
                        # tìm nước đi có thể của Q
                        for i in range(self.size):
                            # nếu hàng hiện tại không trùng với hàng của Q thì tiếp tục
                            if i != row:
                                # tạo bảng sao của bàn cờ hiện tại
                                neighbor = [list(r) for r in current_board]
                                # thay ô hiện tại bằng ô trống
                                neighbor[row][col] = '0'
                                # di chuyển Q vào ô mới
                                neighbor[i][col] = 'Q'
                                neighbors.append(neighbor)
            # không có neighbor
            if not neighbors:
                print('Local maximum found')
                break

            # tính số xung đột của neighbors gán vào biến neighbor_h
            neighbor_h = [(self.h(neighbor), neighbor) for neighbor in neighbors]
            # tìm số lượng xung đột tối thiểu và gán vào best_neighbor_conflict và best_neighbor
            best_neighbor_conflict, best_neighbor = min(neighbor_h)

            # nếu số xung đột tối thiểu của best_neighbor lớn hơn hoặc bằng số xung đột trong bảng hiện tại
            if best_neighbor_conflict >= current_conflict:
                print('Optimal solution found')
                break

            # gán bảng có giải pháp tối ưu nhất thành bảng hiện tại
            current_board = best_neighbor
            # gán số xung đột tối thiểu thành số xung đột của bảng hiện tại
            current_conflict = best_neighbor_conflict

        # trả về giải pháp tối ưu nhất
        return current_board
