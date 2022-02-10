"""
220210 Bagels 게임 구현

"""

import random

NUM_DIGITS = 3 # 숨겨진 숫자의 자릿수 세팅
MAX_GUESSES = 10 # 최대 답변 횟수

# 유틸 함수 정의

def getSecretNum():
    """길이가 NUM_DIGITS인 숫자열 반환 / 중복 허용하지 않음"""
    numbers = list('0123456789')
    random.shuffle(numbers)

    return ''.join(numbers[:NUM_DIGITS])

def getClues(guess, secretNum):
    """비밀번호에 대한 단서인 pico, fermi, bagels로 구성된
    문자열을 반환함"""

    # 정답을 맞춘 경우 
    if guess == secretNum:
        return 'You got it!'

    # 정답이 아닌 경우, 사용자가 입력한 숫자별로 체킹
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # 숫자와 자리 모두 맞는 경우
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        # 일치하는 숫자가 없는 경우는 Bagels 리턴
        return 'Bagels'
    else:
        # 힌트를 정렬해서 리턴
        return ' '.join(sorted(clues))


# 메인 함수 정의
def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.
---------------------------------------------------
'''.format(NUM_DIGITS))

    while True: # 메인 게임 루프
        # 비밀번호 산출
        secretNum = getSecretNum()
        print("숫자를 맞춰보세요.")
        print(f"총 {MAX_GUESSES}번의 기회가 있습니다.")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # 유효한 예측값을 입력할 때까지 대기
            # 자릿수가 다르거나 숫자 외의 문자를 입력하면 다시 입력받음
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}: ')
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                # getClues() 에서 축하 메세지를 출력했고
                # 여기서 루프 종료
                break
            if numGuesses > MAX_GUESSES:
                print("기회를 모두 소비했습니다.")
                print(f"정답은 {secretNum}이었습니다.")

        # 다시 게임하고 싶은지 묻는다.
        print("다시 한번 플레이하겠습니까? (y/n)")
        if not input('> ').lower() == 'y':
            break

    print("Thanks for playing!")


if __name__ == '__main__':
    main()