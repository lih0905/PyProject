"""
움직이는 DVD 로고
"""

import sys, random, time
import bext

# 상수 설정
# best.size() 는 'os.terminal_size(columns=80, lines=25)' 형태를 반환
WIDTH, HEIGHT = bext.size()
# 줄바꿈을 자동으로 추가하지 않으면 윈도우의 마지막 열에 추가할 수 없음
WIDTH -= 1

NUMBER_OF_LOGOS = 20
PAUSE_AMOUNT = 0.01
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# logo 딕셔너리에 대한 키 이름
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    # 로고 생성
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logo = {
            COLOR: random.choice(COLORS),
            X: random.randint(1, WIDTH - 4), 
            Y: random.randint(1, HEIGHT - 4),
            DIR: random.choice(DIRECTIONS)
        }
        logos.append(logo)
        if logos[-1][X] % 2 == 1:
            # X가 짝수여야 코너에 닿을 수 있기 때문에 짝수가 되도록 함
            logos[-1][X] -= 1

    cornerBounces = 0 # 로고가 코너에 닿은 횟수
    while True:
        for logo in logos:
            # logo의 현재 위치 지우기
            bext.goto(logo[X], logo[Y])
            print('   ', end='')

            originalDirection = logo[DIR]

            # logo가 코너에 닿았는지 확인
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # logo가 왼쪽 끝에 닿았는지 확인
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # logo가 오른쪽 끝에 닿았는지 확인 (DVD 문자의 길이 때문에 WIDTH -3)
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # logo가 상단 끝에 닿았는지 확인
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # logo가 하단 끝에 닿았는지 확인
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != originalDirection:
                # 로고가 튕겨 나올 때 색상 변경
                logo[COLOR] = random.choice(COLORS)

            # 로고를 이동시킴
            # 터미널의 문자가 두 배 크기 때문에 X를 2씩 이동
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

            # 코너에 닿은 횟수를 표시
            bext.goto(5, 0)
            bext.fg('white') # 글자 색
            print('Corner bounces:', cornerBounces, end='')

            for logo in logos:
                # 새로운 위치에 로고 그림
                bext.goto(logo[X], logo[Y])
                bext.fg(logo[COLOR])
                print('DVD', end='')

            bext.goto(0, 0)

            sys.stdout.flush() # bext를 사용할 때 필요한 부분
            time.sleep(PAUSE_AMOUNT)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # Ctrl+C 누르면 종료
        print('종료합니다.')
        sys.exit()
