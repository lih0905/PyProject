"""
생일의 역설 구현

생일 갯수를 입력하면 10만번의 생일 생성 실험을 반복하여 생일이 겹치는 경우가 있는 확률을 반환함
"""
import datetime, random

# 월 이름이 순서대로있는 튜플을 만든다:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
NUM_SIM = 100000

def getBirthdays(numberOfBirthdays):
    """주어진 갯수만큼의 생일을 생성하여 리스트로 반환"""
    birthdays = []
    for i in range(numberOfBirthdays):
        # 연도는 중요하지 않음
        # 1월 1일자로 생성 후 임의의 날짜만큼 더해줌
        startOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """생일 리스트에서 중복되는 생일이 있는지 확인"""
    if len(birthdays) == len(set(birthdays)):
        return False
    return True



def main():
    print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

    while True:
        # 사용자가 유효한 값을 입력하길 기다림
        print("생일을 몇 개 생성할까요? (최대 100개)")
        response = input('> ')
        if response.isdecimal() and (0 < int(response) <= 100):
            numBDays = int(response)
            break
    print()

    # 생일 생성 후 출력
    print(f"{numBDays}개의 생일을 생성하였습니다.")
    birthdays = sorted(getBirthdays(numBDays))
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(', ', end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = f"{monthName} {birthday.day}"
        print(dateText, end='')
    print()

    # 결과 출력
    print("이번 시뮬레이션에서는 ", end='')
    if getMatch(birthdays):
        print("생일이 겹치는 사람이 있습니다.")
    else:
        print("생일이 겹치는 사람이 없습니다.")
    print()

    # 100,000번의 시뮬레이션 실행하기
    print(f"{numBDays}개의 생일 생성을 {NUM_SIM:,}번 반복합니다.")
    input("엔터를 누르세요.")
    
    simMatch = 0 # 생일이 겹치는 경우의 수
    for i in range(NUM_SIM):
        # 10,000번마다 진행 상황 출력
        if i % int(NUM_SIM/10) == 0:
            print(f'{i:,}번째 시뮬레이션 진행 중...')
        birthdays = getBirthdays(numBDays)
        if getMatch(birthdays):
            simMatch += 1
    print(f"{NUM_SIM:,}번의 시뮬레이션을 마쳤습니다.")
    print()

    prob = round(simMatch / NUM_SIM * 100, 2)
    print(f"{NUM_SIM:,}번의 시뮬레이션 중 생일이 겹치는 경우는 {simMatch:,}번이었습니다.")
    print(f"다시 말해, {numBDays}명의 사람이 있으면 그 중 생일이 겹칠 확률은 {prob}% 입니다.")

if __name__ == '__main__':
    main()