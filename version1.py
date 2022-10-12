import sys

import numpy as np


def sokoban(stage, input_map):
    print(str(stage) + '\n')
    #print(input_map + '\n')
    for i_map in input_map:
        print(i_map)

    #2차원 배열로 변환 저장
    sign_dict = {'#':0, 'O':1, 'o':2, 'P':3, '=':4, ' ':' '}

    #sokoban_list = list(map(str, input_map.split('\n')))
    sokoban_array = [list(a) for a in input_map]
    for i in range(len(sokoban_array)):
        for j in range(len(sokoban_array[i])):
            sokoban_array[i][j] = sign_dict[sokoban_array[i][j]]

    # 가로, 세로 크기
    print("\n가로크기: " + len(sokoban_array[0]).__str__())
    #max([len(a) for a in alist])), 같은 크기
    print("세로크기: " + len(sokoban_array).__str__())

    #2차원 배열 -> list , [list(a) for a in alist]

    #구멍, 공의 수 O, o
    print("구멍의 수: " + sum([x==1 for b in sokoban_array for x in b]).__str__())
    print("공의 수: " + sum([x==2 for b in sokoban_array for x in b]).__str__())

    #player 위치
    for i in range(len(sokoban_array)):
        for j in range(len(sokoban_array[i])):
            if sokoban_array[i][j] == 3:
                print(f'플레이어 위치 : ({i + 1}, {j + 1})\n')

if __name__ == "__main__":
    #입력하기
    # input = ""
    # for s in sys.stdin:
    #     if (s == "\n"):
    #         break
    #     input += f'{s}'
    input = "Stage 1\n" \
            "#####\n" \
            "#OoP#\n" \
            "#####\n" \
            "=====\n" \
            "Stage 2\n" \
            "  #######  \n" \
            "###  O  ###\n" \
            "#    o    #\n" \
            "# Oo P oO #\n" \
            "###  o  ###\n" \
            " #   O  #  \n" \
            " ########  "
    map = list(map(str, input.split('\n')))

    start = 0
    for i in range(len(map)):
        if ("====" in map[i]):
            sokoban(map[start], map[start+1:i])
            start = i + 1
        if i == len(map)-1:
            sokoban(map[start], map[start + 1:])
            start = i + 1


    # #Stage, 지도데이터
    # stage = 1
    # input = "#####\n" \
    #         "#OoP#\n" \
    #         "#####"
    # sokoban(stage, input)
    #
    # stage = 2
    # input = "  ####### \n" \
    #         "###  O  ###\n" \
    #         "#    o    #\n" \
    #         "# Oo P oO #\n" \
    #         "###  o  ###\n" \
    #         " #   O  #  \n " \
    #         " ########  "
    # sokoban(stage, input)