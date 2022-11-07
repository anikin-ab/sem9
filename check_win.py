def get_win_check(board, symbol):
    if_win = False
    for line in board:
        if line.count(symbol) == 3:
            if_win = True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            if_win = True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        if_win = True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        if_win = True
    return if_win