import random

MAX_STRIKES = 6
REACTION_FACES = ['😐','😧','😡','🥲','😭']

def get_base_drawing():
    return """
______
|    |
|   😐
| --||--
|   /\\
|  /  \\
|
|_____
"""

def get_body_parts():
    return [
        {'name': 'head', 'indexes': [19]},
        {'name': 'torso', 'indexes':[25,26]},
        {'name': 'left-arm', 'indexes':[23,24]},
        {'name': 'right-arm', 'indexes':[27,28]},
        {'name': 'left-leg', 'indexes':[34,40]},
        {'name': 'right-leg', 'indexes': [35,43]}]

def print_body(strikes):
    drawing = list(get_base_drawing())
    parts = get_body_parts()
    parts.reverse()
    for n in range(MAX_STRIKES-(strikes+1)):
        part = parts[n]
        for index in part['indexes']:
            drawing[index] = ' '
    return ''.join(drawing)


if __name__ == '__main__':
    for n in range(MAX_STRIKES):
        print(n)
        print(print_body(n))
