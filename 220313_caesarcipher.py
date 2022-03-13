"""
카이사르 사이퍼(KEY만큼 알파벳을 순환시키는 암호) 구현
"""

try:
    import pyperclip # 텍스트를 클립보드로 복사하는 패키지
except ImportError:
    pass

# 암호화/복호화
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("카이사르 사이퍼")
print("카이사르 사이퍼는 알파벳을 정해진 숫자만큼 옮겨서 암호화/복호화하는 방식")

# 암호화 또는 복호화할 문자를 사용자가 입력하게 함
while True:
    # e 또는 d를 입력할 까지 계속 반복한다.
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print("e 혹은 d를 입력해주십시오.")

# 사용할 키를 입력받음
while True:
    # 유효한 키를 입력할 때까지 반복
    maxKey = len(SYMBOLS) - 1
    print(f"Key로 사용할 숫자(0 에서 {maxKey} 사이)를 입력해주세요.")
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# 암호화/복호화하려는 메세지를 사용자가 입력하게 함
print(f"Enter the message to {mode}.")
message = input('> ')

# 카이사르 암호는 대문자에 적용
message = message.upper()

# 암호화/복호화된 형태의 메세지 저장
translated = ''

# 메세지의 각 기호를 암호화/복호화
for symbol in message:
    if symbol in SYMBOLS:
        # 기호에 대한 숫자 찾기
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key

        # num의 범위 조정
        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)

        # 암호화/복호화된 숫자의 기호를 translated에 추가
        translated += SYMBOLS[num]
    else:
        # 암호화/복호화 없이 기호를 그냥 추가
        translated += symbol

# 암호화/복호화된 문자열을 화면에 표시
print(translated)

try:
    pyperclip.copy(translated)
    print("문자열을 클립보드에 복사하였습니다.")
except:
    pass