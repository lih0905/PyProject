"""
블랙잭 게임 구현
"""

import random, sys

# 상수 설정:
HEARTS   = chr(9829) # 문자 9829는 '♥'.
DIAMONDS = chr(9830) # 문자 9830은 '♦'.
SPADES   = chr(9824) # 문자 9824는 '♠'.
CLUBS    = chr(9827) # 문자 9827은 '♣'.
# (chr 코드에 대한 목록은 https://inventwithpython.com/charactermap을 참조하자)
BACKSIDE = 'backside'

# 사용할 함수들 정의

def getBet(maxBet):
    """플레이어에게 얼마를 걸지 묻는 함수"""
    while True: # 유효한 값을 입력할 때까지 계속 질문
        print(f"얼마를 베팅하시겠습니까? (1-{maxBet}, or QUIT)")
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print("플레이 해주셔서 감사합니다.")
            sys.exit()

        if not bet.isdecimal():
            # 숫자를 입력하지 않았다면 다시 물어봄
            continue 

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDeck():
    """52개의 모든 카드에 대한 (rank, suit) 튜플 리스트를 반환"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in list('JQKA'):
            deck.append((rank,suit))
    random.shuffle(deck)
    return deck

def getHandValue(cards):
    """카드의 값을 반환한다. 얼굴이 있는 카드들은 모두 10이며,
    에이스는 11 또는 1이다(이 함수는 최적의 에이스 값을 선택한다)."""
    value = 0
    numberOfAces = 0

    # 에이스가 아닌 나머지 카드들에 값을 추가
    for card in cards:
        # card = (rank, suit)
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in list('KQJ'):
            # 문자 카드는 10을 더함
            value += 10
        else:
            value += int(rank)

    # 에이스에 대한 값을 추가
    value += numberOfAces # 일단 에이스 하나당 1을 더함
    for i in range(numberOfAces):
        # 만약 추가로 10을 더해도 bust가 되지 않는다면 그렇게 함
        if value + 10 <= 21:
            value += 10

    return value

def displayCards(cards):
    """카드 리스트에 있는 모든 카드를 표시"""
    rows = ['', '', '', '', ''] # 각 행에 표시될 텍스트 변수

    for i, card in enumerate(cards):
        rows[0] += ' ___  ' # 카드의 상단 라인
        if card == BACKSIDE:
            # 카드의 뒷면 출력:
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '| ##|'
        else:
            # 카드의 앞면 출력:
            rank, suit = card
            rows[1] += f'|{rank.ljust(2)} | '
            rows[2] += f'| {suit} | '
            rows[3] += f'|_{rank.rjust(2, "_")}| '
    
    # 화면에 각 행을 출력
    for row in rows:
        print(row)

def displayHands(playerHand, dealerHand, showDealderHand):
    """플레이어와 딜러의 카드를 보여준다.
    만약에 showDealerHand가 False면 딜러의 첫 카드를 가린다."""
    print()
    if showDealderHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # 딜러의 첫 번째 카드를 가림
        displayCards([BACKSIDE] + dealerHand[1:])

    # 플레이어의 카드 표시
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

def getMove(playerHand, money):
    """플레이어 차례에서 플레이터 선택을 묻는다.
    히트인 'H', 스탠드인 'S', 더블다운인 'D'를 반환"""
    # 플레이어가 올바른 입력을 할 때까지 계속 반복
    while True:
        # 플레이어의 선택지 리스트
        moves = ['(H)it', '(S)tand']

        # 플레이어가 최초에 받은 카드 두 장이 서로 같다면
        # 더블 다운할 수 있음을 알려줌
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # 플레이어의 선택을 받음
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move 


def main():
    print('''Blackjack, by Al Sweigart al@inventwithpython.com

    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.''')

    money = 5000
    while True: # 메인 게임 루프
        # 플레이어가 돈을 다 썼는지 검사
        if money <= 0:
            print("파산했습니다!")
            print("플레이 해주셔서 감사합니다.")
            sys.exit()

        # 이번 판에 배팅할 금액 임력
        print("소지금:", money)
        bet = getBet(money)

        # 딜러와 플레이어에게 두 장의 카드 배분
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # 플레이어의 동작을 처리
        print('베팅:', bet)
        # 플레이어가 stand 또는 bust 될 때까지 계속 루프를 돎
        while True:
            # 현재 들고 있는 카드를 출력
            displayHands(playerHand, dealerHand, False)
            print()

            # 플레이어가 bust되었는지 검사
            if getHandValue(playerHand) > 21:
                break

            # 플레이어의 동작을 받음
            move = getMove(playerHand, money - bet)

            # 플레이어의 동작 처리
            if move == 'D':
                # 더블 다운
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f"베팅액을 {bet}원으로 올립니다.")
                print('베팅:', bet)

            if move in ('H', 'D'):
                # Hit 또는 double down이면 다른 카드를 받음
                newCard = deck.pop()
                rank, suit = newCard
                print(f"{suit} {rank} 카드를 뽑았습니다.")
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # 플레이어가 bust됨
                    continue

            if move in ('S', 'D'):
                # Stand 또는 double down이면 플레이어 턴이 끝남
                break

        # 딜러의 동작 처리
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # 딜러가 hit
                print('딜러가 카드를 뽑습니다.')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                input('엔터를 누르세요...')
                print('\n\n')

        # 들고 있던 패를 공개함
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # 플레이어가 익뎠는지, 졌는지, 아니면 비겼는지 처리
        if dealerValue > 21:
            print(f"딜러가 버스트했습니다. ${bet}원을 획득하였습니다.")
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("패배하였습니다.")
            money -= bet
        elif playerValue > dealerValue:
            print(f"${bet}원을 획득하였습니다.")
            money += bet
        elif playerValue == dealerValue:
            print("비겼으므로 베팅액을 반환합니다.")

        input("엔터를 누르세요...")
        print('\n\n')



if __name__ == '__main__':
    main()
