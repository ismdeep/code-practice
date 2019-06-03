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


def full_test(game_board):
    for item in game_board:
        if item is 0:
            return False
    return True


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
    # 判断程序是否已经结束
    if end_game_test(game_board):
        return game_equal, None
    # 根据当前节点，产生接下来的所有可能操作
    next_nodes = generate_next_nodes(game_board)
    # 判断产生的节点中是否有已经赢的，如果有则直接返回
    for _id_, node in next_nodes:
        if win_test(node):
            return game_win, _id_
    rival_nodes = []
    for _id_, node in next_nodes:
        # 判断是否已经满了，如果满了则随便返回第一个
        if full_test(node):
            return game_equal, _id_
        flag, new_id = search(inverse(node))
        rival_nodes.append((flag, _id_, new_id))
    for flag, _id_, _new_id_ in rival_nodes:
        if flag == game_lose:
            return game_win, _id_
    for flag, _id_, _new_id_ in rival_nodes:
        if flag == game_equal:
            return game_equal, _id_
    flag, _id_, _new_id_ = rival_nodes[0]
    return game_lose, _id_


def symbol_chess(_val_):
    if _val_ is 1:
        return 'o'
    if _val_ is -1:
        return 'x'
    return '□'


def game_board_to_string(_game_board_):
    ans = ''
    ans += '%s %s %s\n%s %s %s\n%s %s %s\n' % (
        symbol_chess(_game_board_[0]),
        symbol_chess(_game_board_[1]),
        symbol_chess(_game_board_[2]),
        symbol_chess(_game_board_[3]),
        symbol_chess(_game_board_[4]),
        symbol_chess(_game_board_[5]),
        symbol_chess(_game_board_[6]),
        symbol_chess(_game_board_[7]),
        symbol_chess(_game_board_[8]))
    return ans


def main_demo():
    result, _id_ = search([1, 1, 0, 0, -1, 0, 0, 0, 0])
    print(result, _id_)


def main_human_first():
    _game_board_ = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(game_board_to_string(_game_board_))
    while True:
        _human_id_ = int(input())
        _game_board_[_human_id_] = 1
        print(game_board_to_string(_game_board_))
        result, _robot_id_ = search(inverse(_game_board_))
        print('robot >', result, _robot_id_)
        _game_board_[_robot_id_] = -1
        print(game_board_to_string(_game_board_))


def main_robot_first():
    _game_board_ = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(game_board_to_string(_game_board_))
    while True:
        result, _robot_id_ = search(inverse(_game_board_))
        print('robot >', result, _robot_id_)
        _game_board_[_robot_id_] = -1
        print(game_board_to_string(_game_board_))
        _human_id_ = int(input())
        _game_board_[_human_id_] = 1
        print(game_board_to_string(_game_board_))


main_human_first()
# main_robot_first()
