"""
카이사르 사이퍼를 브루트포스로 해킹하는 프로그램
"""

print("카이사르 사이퍼 해커")

# 해킹할 메세지 입력
print("카이사르 사이퍼로 암호화된 메세지를 입력하세요.")
message = input('> ')

# 복호화할 수 있는 기호
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    # 모든 키에 대해 루프
    translated = ''

    # 메세지의 각 기호를 복호화
    for symbol in message:
        if symbol in SYMBOLS:
            # 기호의 숫잣값을 찾은 후 복호화
            num = SYMBOLS.find(symbol)
            num -= key

            if num < 0:
                num += len(SYMBOLS)

            # 복호화된 기호를 더함
            translated += SYMBOLS[num]
        else:
            # 복호화 없이 기호를 더함
            translated += symbol

    # 테스트된 키와 함께 복호화된 텍스트 표시
    print(f"Key #{key}: {translated}")
