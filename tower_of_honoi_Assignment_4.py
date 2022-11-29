from pathlib import Path
import gettext
gettext.install('hanoi', Path(__file__).parent)

def single_move(src, dest):
    dest.append(src.pop())

def all_possible_moves(p1, p2):
    if p1 and (not p2 or p1[-1] < p2[-1]):
        return p1, p2
    else:
        return p2, p1

def print_current_status(a, b, c):
    print(a)
    print(b)
    print(c)
    print()

def main(discs):
    a = list(range(discs, 0, -1))
    b = []
    c = []

    min_moves = 2 ** discs - 1

    if discs % 2 == 1:
        p = [a, c, b]
    else:
        p = [a, b, c]

    moves = 0
    while len(c) != discs:
        if moves % 2 == 0:
            single_move(p[0], p[1])  # Smallest disc now on peg[1]
        else:
            src, dest = all_possible_moves(p[0], p[2])
            single_move(src, dest)
            p = p[1:] + p[:1]   # Rotate the peg ordering

        print_current_status(a, b, c)
        moves += 1

    print()
    print(_('Number of Moves:'), moves)
    print(_('Minimal Number of moves:'), min_moves)

if __name__ == '__main__':
    num_of_discs= int(input(_('Please enter the number of disks: ')))
    main(num_of_discs)