# coding: utf-8
# author: ismdeep
# dateime: 2019-05-29 08:09:30
# filename: main.py
# blog: https://ismdeep.com


game_win = 1
game_lose = -1
game_equal = 0


def inverse(game_board):
    ans = []
    for item in game_board:
        ans.append(0 - item)
    return ans


def win_test(game_board):
    win_indexes = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for win_index in win_indexes:
        if game_board[win_index[0]] == 1 and game_board[win_index[1]] == 1 and game_board[win_index[2]] == 1:
            return True
    return False


def end_game_test(game_board):
    for item in game_board:
        if 0 == item:
            return False
    return True


def generate_next_nodes(game_board):
    results = []
    for i in range(9):
        if 0 == game_board[i]:
            tmp = [item for item in game_board]
            tmp[i] = 1
            results.append((i, tmp))
    return results


def search(game_board):
    if end_game_test(game_board):
        return game_equal, None
    next_nodes = generate_next_nodes(game_board)
    for id, node in next_nodes:
        if win_test(node):
            return game_win, id
    rival_nodes = []
    for id, node in next_nodes:
        flag, new_id = search(inverse(node))
        rival_nodes.append((flag, new_id))
    for flag, id in rival_nodes:
        if flag == game_lose:
            return game_win, id
    for flag, id in rival_nodes:
        if flag == game_equal:
            return game_equal, id
    flag, id = rival_nodes[0]
    return game_lose, id


def main():
    result, id = search([0, 0, 0, 0, 0, 0, 0, 0, 0])
    print(result, id)


main()
