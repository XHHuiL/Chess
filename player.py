# coding: utf-8
# created by liu hui
import chess


# 普通玩家的输入接口
def respond_to(fen):
    board = chess.Board(fen)
    is_white = board.turn
    legal_movs = ""
    for legal_mov in board.legal_moves:
        legal_movs += legal_mov.uci() + " "
    print legal_movs
    mov = chess.Move(0, 0)
    if is_white:
        while mov not in board.legal_moves:
            mov = chess.Move.from_uci(raw_input("white please input step that you want take\n"))
    else:
        while mov not in board.legal_moves:
            mov = chess.Move.from_uci(raw_input("white please input step that you want take\n"))
    return mov.uci()