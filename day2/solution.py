f = open("input.txt", "r")

total_score = 0

# x = lose
#
# y = tie
#
# z = win


def winLose(arg, letter):
    win = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }

    lose = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }

    tie = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }

    if arg == 'win':
        return win.get(letter)
    elif arg == 'tie':
        return tie.get(letter)
    elif arg == 'lose':
        return lose.get(letter)


def switcher(arg, letter):
    winPoints = {
        'win': 6,
        'tie': 3,
        'lose': 0
    }

    points = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    return points.get(letter) + winPoints.get(arg)


for x in f:
    outcome = ''
    y = x.split()
    if y[1] == 'X':
        outcome = 'lose'
    elif y[1] == 'Y':
        outcome = 'tie'
    elif y[1] == 'Z':
        outcome = 'win'

    total_score = total_score + switcher(outcome, winLose(outcome, y[0]))

print(total_score)

f.close()
