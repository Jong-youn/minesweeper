import random

def make_game_board():
    bombs = []

    # random module로 지뢰 위치 선정
    while len(bombs) < 10:
        place = (random.randrange(0,10), random.randrange(0,10))
        if place not in bombs:
            bombs.append(place)

    return bombs

def game():
    bombs = make_game_board()
    result = [[0]*10 for _ in range(10)]

    print('#1 지뢰 위치: ')
    print_out(result, bombs)

    row_direc = [-1, -1, -1, 0, 0, 1, 1, 1]
    col_direc = [-1, 0, 1, -1, 1, -1, 0, 1]

    for row in range(10):
        for col in range(10):
            # [row, col]주변에 위치한 8개의 사각형 탐색
            for d in range(8):
                new_row = row + row_direc[d]
                new_col = col + col_direc[d]
                if 0 <= new_row < 10 and 0 <= new_col < 10 and (new_row, new_col) in bombs:
                    result[row][col] += 1

    print('#2 결과: ')
    print_out(result, bombs)

    return result

def print_out(result, bombs):
    PINK = 207
    BLUE = 43

    for row in range(10):
        for col in range(10):
            #폭탄이 있는 사각형은 분홍색으로 출력, 주변에 폭탄이 하나 이상 위치한 사각형은 파란색으로 출력
            if (row, col) in bombs:
                print(f'\033[38;5;{PINK}m' + str(result[row][col]) + '\033[0m', end= ' ')
            elif result[row][col] > 0:
                print(f'\033[38;5;{BLUE}m' + str(result[row][col]) + '\033[0m', end= ' ')
            else:
                print(result[row][col], end= ' ')
        print(end='\n')
    print(end='\n')

game()