import sys

def print_map(array, p, q):
        array[p][q] = 'P'
        for i in array:
            print("".join(i))

def check_block(array, p, q, c):
    if array[p][q] != ' ':
        for i in array:
            print("".join(i))
        print(c.upper(), ': (경고!) 해당 명령을 수행할 수 없습니다')
    else:
        return True

def play(input_map):
    print("Stage 2\n")
    print(input_map)

    # 2차원 배열로 변환 저장
    sokoban_array = [list(a) for a in input_map.split('\n')]
    # player 위치
    p = 0
    q = 0
    for i in range(len(sokoban_array)):
        for j in range(len(sokoban_array[i])):
            if sokoban_array[i][j] == "P":
                p = i
                q = j


    while True:
        print("\nSOKOBAN> ")
        cmd = str(sys.stdin.readline())
        for c in cmd[:-1]:
            if c == 'q':
                print("Bye~")
                return
            if c not in ('w', 'a', 's', 'd'):
                print_map(sokoban_array, p,q)
                print(c.upper(), ': (경고!) 해당 명령을 수행할 수 없습니다')
            elif c == 'w':
                ch = check_block(sokoban_array, p -1, q, c)
                if ch:
                    sokoban_array[p][q] = ' '
                    p -= 1
                    print_map(sokoban_array, p, q)
                    print("W: 위쪽으로 이동합니다")
            elif c == 'a':
                ch = check_block(sokoban_array, p, q -1 , c)
                if ch:
                    sokoban_array[p][q] = ' '
                    q -= 1
                    print_map(sokoban_array, p, q)
                    print("A: 왼쪽으로 이동합니다")
            elif c == 's':
                ch = check_block(sokoban_array, p+1, q, c)
                if ch:
                    sokoban_array[p][q] = ' '
                    p += 1
                    print_map(sokoban_array, p, q)
                    print("S: 아래쪽으로 이동합니다")
            else: # c == 'd':
                ch = check_block(sokoban_array, p, q + 1, c)
                if ch:
                    sokoban_array[p][q] = ' '
                    q += 1
                    print_map(sokoban_array, p, q)
                    print("D: 오른쪽으로 이동합니다")


if __name__ == "__main__":
    input = "  #######  \n" \
            "###  O  ###\n" \
            "#    o    #\n" \
            "# Oo P oO #\n" \
            "###  o  ###\n" \
            " #   O  #  \n" \
            " ########  "
    play(input)

