
from version3 import check_block, move_o, print_map, check_all_0, divide_0_to_o
import sys
import pickle
from copy import deepcopy

class Sokoban:
    def __init__(self, stage, map):

        self.stage = stage
        self.map = map
        self.sokoban_array = [list(a) for a in self.map]
        self.stack = dict() #LIFO
        self.turn = 0
        self.stack_p = dict()
        self.stack_q = dict()
        self.p = 0
        self.q = 0

    def undo(self):
        self.sokoban_array = self.stack[self.turn - 1]
        self.p = self.stack_p[self.turn - 1]
        self.q = self.stack_q[self.turn - 1]
    def redo(self):
        self.sokoban_array = self.stack[self.turn]
        self.p = self.stack_p[self.turn]
        self.q = self.stack_q[self.turn]

    def play(self):
        print('\n' + self.stage + '\n')
        for i_map in self.map:
            print(i_map)

        # 2차원 배열로 변환 저장
        #sokoban_array = [list(a) for a in self.map]
        # player 위치
        # p = 0
        #         # q = 0
        O_trace = []

        for i in range(len(self.sokoban_array)):
            for j in range(len(self.sokoban_array[i])):
                if self.sokoban_array[i][j] == "P":
                    self.p = i
                    self.q = j
                if self.sokoban_array[i][j] == "O":
                    a = i
                    b = j
                    O_trace.append([a, b])
                if self.sokoban_array[i][j] == "0":
                    a = i
                    b = j
                    O_trace.append([a, b])

        #turn = 0
        self.stack[0] = deepcopy(self.sokoban_array)
        self.stack_p[0] = deepcopy(self.p)
        self.stack_q[0] = deepcopy(self.q)

        while check_all_0(self.sokoban_array):
            print("\nSOKOBAN> ")
            cmd = str(sys.stdin.readline())
            if cmd[:-1] in ['1S', '2S', '3S', '4S', '5S']:
                with open(f"serialized_file{cmd[:-1]}.p", 'wb') as f:
                    self.map = [''.join(y) for y in self.sokoban_array]
                    pickle.dump(s, f)
                print(f"{cmd[:-1]}번 세이브에 진행상황 저장")
                break
                #return ''

            for c in cmd[:-1]:
                if c == 'q':
                    print("Bye~")
                    return
                if c not in ('w', 'a', 's', 'd', 'u', 'U'):
                    print_map(self.sokoban_array, self.p, self.q, O_trace)
                    print(c.upper(), ': (경고!) 해당 명령을 수행할 수 없습니다')
                elif c == 'u':
                    # print(self.turn)
                    # print(self.stack)
                    # print(self.stack[self.turn-1])
                    # print(self.stack_p[self.turn-1])
                    self.undo()
                    #self.sokoban_array = self.stack[self.turn-1]
                    print_map(self.sokoban_array,self.p, self.q, O_trace)
                elif c == 'U':
                    # print(self.turn)
                    # print(self.stack)
                    # print(self.stack[self.turn])
                    # print(self.stack_p[self.turn])
                    self.redo()
                    # self.sokoban_array = self.stack[self.turn-1]
                    print_map(self.sokoban_array, self.p, self.q, O_trace)
                elif c == 'w':
                    self.sokoban_array[self.p][self.q] = ' '
                    if check_block(self.sokoban_array, self.p - 1, self.q):
                        self.p -= 1
                        self.p, self.q = divide_0_to_o(self.sokoban_array, self.p, self.q, c)
                        self.p, self.q = move_o(self.sokoban_array, self.p, self.q, c)
                        print_map(self.sokoban_array, self.p, self.q, O_trace)
                    self.turn += 1
                    self.stack[self.turn] = deepcopy(self.sokoban_array)
                    self.stack_p[self.turn] = deepcopy(self.p)
                    self.stack_q[self.turn] = deepcopy(self.q)

                elif c == 'a':
                    self.sokoban_array[self.p][self.q] = ' '
                    if check_block(self.sokoban_array, self.p, self.q - 1):
                        self.q -= 1
                        self.p, self.q = divide_0_to_o(self.sokoban_array, self.p, self.q, c)
                        self.p, self.q = move_o(self.sokoban_array, self.p, self.q, c)
                        print_map(self.sokoban_array, self.p, self.q, O_trace)
                    self.turn += 1
                    self.stack[self.turn] = deepcopy(self.sokoban_array)
                    self.stack_p[self.turn] = deepcopy(self.p)
                    self.stack_q[self.turn] = deepcopy(self.q)
                elif c == 's':
                    self.sokoban_array[self.p][self.q] = ' '
                    if check_block(self.sokoban_array, self.p + 1, self.q):
                        self.p += 1
                        self.p, self.q = divide_0_to_o(self.sokoban_array, self.p, self.q, c)
                        self.p, self.q = move_o(self.sokoban_array, self.p, self.q, c)
                        print_map(self.sokoban_array,self.p, self.q, O_trace)
                    self.turn += 1
                    self.stack[self.turn] = deepcopy(self.sokoban_array)
                    self.stack_p[self.turn] = deepcopy(self.p)
                    self.stack_q[self.turn] = deepcopy(self.q)

                else:  # c == 'd':
                    self.sokoban_array[self.p][self.q] = ' '
                    if check_block(self.sokoban_array, self.p, self.q + 1):
                        self.q += 1
                        self.p, self.q = divide_0_to_o(self.sokoban_array, self.p, self.q, c)
                        self.p, self.q = move_o(self.sokoban_array, self.p, self.q, c)
                        print_map(self.sokoban_array, self.p, self.q, O_trace)

                    self.turn += 1
                    self.stack[self.turn] = deepcopy(self.sokoban_array)
                    self.stack_p[self.turn] = deepcopy(self.p)
                    self.stack_q[self.turn] = deepcopy(self.q)


        if cmd[:-1] in ['1S', '2S', '3S', '4S', '5S']:

            print("\n진행상황")
            print('\n' + self.stage)
            print(f'턴수: {self.turn}')
            return False

        print('\n' + self.stage + " Clear")
        print(f'턴수: {self.turn}')
        return True

    def __getitem__(self, key):
        return self.stage, self.map




if __name__ == "__main__":
    print("Sokoban Game Start---")

    while True:
        map = []
        with open('map.txt', 'r') as f:
            for line in f.readlines():
                map.append(line.strip())

        start = 0
        for i in range(len(map)):
            if ("====" in map[i]):
                s = Sokoban(map[start], map[start + 1:i])
                ssave = s.play()
                while not ssave:
                    # if ssave:
                    #     print(" ")

                    print("\nS> ")
                    slot = str(sys.stdin.readline())
                    if slot[:-1] in ['1L', '2L', '3L', '4L', '5L']:
                        with open(f"serialized_file{slot[0]}S.p", "rb") as f:
                            sokoban = pickle.load(f)

                            print(f"{slot[:-1]}번 세이브에서 진행상황 불러오기 ")

                            s = Sokoban(sokoban.stage, sokoban.map)

                            ssave = s.play()

                start = i + 1
            if i == len(map) - 1:
                s = Sokoban(map[start], map[start + 1:])
                s.play()
                if ssave:
                    print(" ")
                else:
                    print("\nS> ")
                    slot = str(sys.stdin.readline())
                    if slot[:-1] in ['1L', '2L', '3L', '4L', '5L']:
                        with open(f"serialized_file{slot[0]}S.p", "rb") as f:
                            sokoban = pickle.load(f)
                            print(f"{slot[:-1]}번 세이브에서 진행상황 불러오기 ")
                            print(sokoban.map)
                            print("---------", start)
                            print("---------------", sokoban.stage)
                            s = Sokoban(sokoban.stage, sokoban.map)
                            ssave = s.play()

                start = i + 1

