"""
달력 생성기
달력을 생성 후 텍스트 파일로 저장하는 프로그램
"""

from calendar import calendar
import datetime

# 상수 설정
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', \
    'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',\
    'July', 'August', 'September', 'October', 'November', 'December')

print("달력 생성기")

while True:
    # 연도 입력 받음
    print("달력 생성할 연도를 입력해주세요.")
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print("연도를 숫자로 입력해주세요(예: 2023).")
    continue

while True:
    # 월도 입력 받음
    print("달력 생성할 월을 입력해주세요(1-12 사이).")
    response = input('> ')

    if not response.isdecimal():
        print("월을 숫자로 입력해주세요.")
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print("1에서 12 사이의 숫자를 입력해주세요.")

def getCalendarFor(year, month):
    calText = '' # 생성할 달력 문자열 

    # 달력 상단에 연/월 표시
    calText += (' '*34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # 달력에 요일 추가
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # 주를 구분하는 수평선 문자열
    weekSeparator = ('+----------' * 7) + '\n'

    # 빈칸 생성
    blankRow = ('|          ' * 7) + '|\n'

    # 해당 월의 첫 날을 구함
    currentDate = datetime.date(year, month, 1)

    # 일요일인 날짜가 될 때까지 currentDate를 하루씩 이전 날짜로 옮김
    # weekday()는 요일을 숫자로 반환하며, 일요일일 때 6 반환
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:
        # 그 달의 각 주를 반복
        calText += weekSeparator

        # dayNumberRow는 날짜 레이블을 담음
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # 다음 날로 이동
        dayNumberRow += '|\n'

        # 날짜 행과 세 줄의 빈 행을 추가
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow
        
        # 그 달에 대한 작업이 끝났는지 확인
        if currentDate.month != month:
            break

    # 달력 맨 하단에 수평선 추가
    calText += weekSeparator
    return calText

calText = getCalendarFor(year, month)
print(calText)

# 달력을 텍스트 파일로 저장
calendarFilename = f'calendar_{year}_{month}.txt'
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print(f"Saved to {calendarFilename}.")