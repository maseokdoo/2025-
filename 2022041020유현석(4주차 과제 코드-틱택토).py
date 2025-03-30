# -*- coding: utf-8 -*-
import random

# 보드 초기화 (3x3)
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# 보드 출력
def print_board(board):
    print("\n틱택토 게임 보드:")
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(f"{cell} |", end=" ")
        print("\n-------------")

# 플레이어 턴
def player_move(board):
    while True:
        try:
            row = int(input("행을 입력하세요 (0-2): "))
            col = int(input("열을 입력하세요 (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("잘못된 위치입니다. 빈 칸에 0-2 사이의 값을 입력하세요.")
        except ValueError:
            print("숫자를 입력해주세요.")

# 컴퓨터 턴 (무작위)
def computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'
        print(f"컴퓨터가 ({row}, {col})에 'O'를 놓았습니다.")

# 승리 조건 체크
def check_winner(board, player):
    # 행 체크
    for row in board:
        if all(cell == player for cell in row):
            return True
    # 열 체크
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # 대각선 체크
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# 보드가 가득 찼는지 확인
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# 메인 게임 루프
def play_game():
    board = initialize_board()
    print("틱택토 게임을 시작합니다! 당신은 'X', 컴퓨터는 'O'입니다.")
    print_board(board)

    while True:
        # 플레이어 턴
        player_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("축하합니다! 당신이 이겼습니다!")
            break
        if is_board_full(board):
            print("무승부입니다!")
            break

        # 컴퓨터 턴
        computer_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("컴퓨터가 이겼습니다! 다시 도전해보세요.")
            break
        if is_board_full(board):
            print("무승부입니다!")
            break

# 게임 실행
while True:
    play_game()
    replay = input("다시 플레이하시겠습니까? (y/n): ").lower()
    if replay != 'y':
        print("게임을 종료합니다. 수고하셨습니다!")
        break