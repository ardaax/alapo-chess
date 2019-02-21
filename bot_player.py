import time
player_id = ""
import random
"""
Initialization of the game.
p_id = player_id
"""


def game_started(env, p_id):
    global player_id
    player_id = p_id
    return True


"""
Write your move returning code to this method.
"""


# def generate_output(move):
#     action = str(chr((move['pos'][1]) + 97))
#     action += str(int((move['pos'][0])) + 1)
#     action += str(chr((move['new_pos'][1]) + 97))
#     action += str(int((move['new_pos'][0])) + 1)
#     return action

def move(env):
    print(env.board_output)
    letter_format = input("Type your move:")
    # moves = env.get_possible_moves(env.state, "-1")
    # m = random.choice(moves)
    # letter_format = generate_output(m)
    # print(letter_format)
    return letter_format

"""
    moves = env.get_possible_moves(env.state, you)
    m = random.choice(moves)
    return m
"""


"""
Get the response of your move here.
"""


def move_response(env, resultCode):
    print(env.board_output)

"""
Opponent Moved - get updated env
"""


def opponent_moved(env):
    print(env.board_output)

"""
Game end
"""


def game_ended(env, result, resultCode):
    print(env.board_output)
    print("Result Code:" +str(resultCode))
    if result == "won":
        print("You won the game")
    elif result == "lost":
        print("You lost the game")
    elif result == "draw":
        print("The game is drew")

"""
Disconnected From Server
"""


def disconnected_from_server():
    pass

"""
Connected to Server
"""


def connected_to_server():
    pass