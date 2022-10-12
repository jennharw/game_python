import sys

#두개 붙어 있는 경우
def check_block(array, p, q):
    if array[p][q] == '#':
        return False
    return True

def move_o(array, p, q, c):
    if array[p][q] == 'o':

        #밀기
        if (c == 'a') :
            if (array[p][q-1] == 'O'):
                array[p][q-1] = '0'
            else:
                if check_block(array, p, q-1) & (array[p][q-1] != 'o') & (array[p][q-1] != '0')  :
                    array[p][q-1] = 'o'
                else:
                    q += 1
                    return p, q
        elif (c == 'd') :
            if (array[p][q+1] == 'O'):
                array[p][q+1] = '0'
            else:
                if check_block(array, p, q + 1) & (array[p][q+1] != 'o') & (array[p][q+1] != '0')  :
                    array[p][q + 1] = 'o'
                else:
                    q -= 1
                    return p, q
        elif (c == 's'):
            if (array[p+1][q] == 'O'):
                array[p+1][q] = '0'
            else:
                if check_block(array, p+1, q) & (array[p+1][q] != 'o') & (array[p+1][q] != '0')  :
                    array[p+1][q] = 'o'
                else:
                    p -= 1
                    return p, q
        elif (c == 'w'):
            if (array[p-1][q] == 'O'):
                array[p-1][q] = '0'
            else:
                if check_block(array, p-1, q) & (array[p-1][q] != 'o') & (array[p-1][q] != '0')  :
                    array[p - 1][q] = 'o'
                else:
                    p += 1
                    return p, q
        array[p][q] = 'P'
        return p, q
    else:
        return p, q

def print_map(array, p, q, O_trace):
    array[p][q] = 'P'
    for a in O_trace:     ## P 없으면 ,
        if array[a[0]][a[1]] == ' ':
            array[a[0]][a[1]] = 'O'
    for i in array:
        print("".join(i))


def check_all_0(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'o':
                return True
    return False

def divide_0_to_o(array, p, q, c):

    if (c =='a') & (array[p][q] == '0'):
        if check_block(array, p, q-1):
            array[p][q-1] = 'o'
            array[p][q] = 'O'
        else:
            q += 1
            return p, q
    elif (c == 'd') & (array[p][q] == '0'):
        if check_block(array, p, q + 1):
            array[p][q+1] = 'o'
            array[p][q] = 'O'
        else:
            q -= 1
            return p, q
    elif (c == 'w') & (array[p][q] == '0'):
        if check_block(array, p-1, q):
            array[p-1][q] = 'o'
            array[p][q] = 'O'
        else:
            p += 1
            return p, q
    elif (c == 's') & (array[p][q] == '0'):
        if check_block(array, p + 1, q):
            array[p+1][q] = 'o'
            array[p][q] = 'O'
        else:
            p -= 1
            return p, q
    return p, q





def main(stage, map):

    print('\n' +stage + '\n')
    for i_map in map:
        print(i_map)

    # 2차원 배열로 변환 저장
    sokoban_array = [list(a) for a in map]
    # player 위치
    p = 0
    q = 0
    O_trace = []

    for i in range(len(sokoban_array)):
        for j in range(len(sokoban_array[i])):
            if sokoban_array[i][j] == "P":
                p = i
                q = j
            if sokoban_array[i][j] == "O":
                a = i
                b = j
                O_trace.append([a, b])
            if sokoban_array[i][j] == "0":
                a = i
                b = j
                O_trace.append([a, b])

    turn = 0
    while check_all_0(sokoban_array):
        print("\nSOKOBAN> ")
        cmd = str(sys.stdin.readline())
        for c in cmd[:-1]:
            if c == 'q':
                print("Bye~")
                return
            if c not in ('w', 'a', 's', 'd'):
                print_map(sokoban_array, p, q, O_trace)
                print(c.upper(), ': (경고!) 해당 명령을 수행할 수 없습니다')
            elif c == 'w':
                sokoban_array[p][q] = ' '
                if check_block(sokoban_array, p-1, q):
                    p -= 1
                    p, q = divide_0_to_o(sokoban_array, p, q, c)
                    p, q = move_o(sokoban_array, p, q, c)
                    print_map(sokoban_array, p, q, O_trace)
                turn += 1
            elif c == 'a':
                sokoban_array[p][q] = ' '
                if check_block(sokoban_array, p, q-1):
                    q -= 1
                    p, q = divide_0_to_o(sokoban_array, p, q, c)
                    p, q = move_o(sokoban_array, p, q, c)
                    print_map(sokoban_array, p, q, O_trace)

                    turn += 1
            elif c == 's':
                sokoban_array[p][q] = ' '
                if check_block(sokoban_array, p+1, q):
                    p += 1
                    p, q = divide_0_to_o(sokoban_array, p, q, c)
                    p, q = move_o(sokoban_array, p, q, c)
                    print_map(sokoban_array, p, q, O_trace)
                turn += 1
            else:  # c == 'd':
                sokoban_array[p][q] = ' '
                if check_block(sokoban_array, p, q+1):
                    q += 1
                    p, q = divide_0_to_o(sokoban_array, p, q, c)
                    p, q = move_o(sokoban_array, p, q, c)
                    print_map(sokoban_array, p, q, O_trace)
                turn += 1
    print('\n' + stage + " Clear")
    print(f'턴수: {turn}')

if __name__ == "__main__":
    print("Sokoban Game Start---")
    map = []
    with open('map.txt', 'r') as f:
        for line in f.readlines():
            map.append(line.strip())

    start = 0
    for i in range(len(map)):
        if ("====" in map[i]):
            main(map[start], map[start + 1:i])
            start = i + 1
        if i == len(map) - 1:
            main(map[start], map[start + 1:])
            start = i + 1

