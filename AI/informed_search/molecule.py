from AI.searching_framework.informed_search import *
from AI.searching_framework.utils import Problem
obstacles = [(0, 1), (1, 1), (1, 3), (2, 5), (3, 1), (3, 6), (4, 2),
             (5, 6), (6, 1), (6, 2), (6, 3), (7, 3), (7, 6), (8, 5)]

def move_up(atom1, atom2, atom3, grid_size):
    if atom1[1]+1 <=grid_size[1]-1 and atom1 not in obstacles and atom1 not in [atom2, atom3]:
        atom1[1]+=1
        return atom1
def move_down(atom1, atom2, atom3, grid_size):
    if atom1[1]-1 >=0 and atom1 not in obstacles and atom1 not in [atom2, atom3]:
        atom1[1]-=1
        return atom1
def move_right(atom1, atom2, atom3, grid_size):
    if atom1[0]+1 <=grid_size[0]-1 and atom1 not in obstacles and atom1 not in [atom2, atom3]:
        atom1[0]+=1
        return atom1
def move_left(atom1, atom2, atom3, grid_size):
    if atom1[0]-1 >=0 and atom1 not in obstacles and atom1 not in [atom2, atom3]:
        atom1[0]-=1
        return atom1

class Molecule(Problem):
    def __init__(self, initial):
        super().__init__(initial, None)
        self.grid_size=[7, 9]
    def goal_test(self, state):
        h1_x=state[0]
        h1_y=state[1]
        o_x=state[2]
        o_y=state[3]
        h2_x=state[4]
        h2_y=state[5]
        return h1_y==o_y and h1_x-1==o_x and o_y==h2_y and h2_x+1==o_x
    def successor(self, state):
        successors=dict()
        h1 = [state[0], state[1]]
        o = [state[2], state[3]]
        h2 = [state[4], state[5]]
        new_h1=move_up(h1, o, h2, self.grid_size)
        if new_h1!=h1:
            successors["Up_H1"]= (new_h1[0], new_h1[1], o[0],o[1], h2[0],h2[1])
            # Down H1
        new_h1 = move_down(h1, o, h2, self.grid_size)

        if new_h1!=h1:
            successors["Down_H1"]= (new_h1[0], new_h1[1], o[0],o[1], h2[0],h2[1])
        # Left H1
        new_h1 = move_left(h1, o, h2, self.grid_size)

        if new_h1!=h1:
            successors["Left_H1"]= (new_h1[0], new_h1[1], o[0],o[1], h2[0],h2[1])
        # Right H1
        new_h1 = move_right(h1, o, h2, self.grid_size)

        if new_h1!=h1:
            successors["Right_H1"]= (new_h1[0], new_h1[1], o[0],o[1], h2[0],h2[1])

        # Up O
        new_o = move_up(o, h1, h2, self.grid_size)

        if new_o!=o:
            successors["Up_O"] = (h1[0], h1[1], new_o[0], new_o[1], h2[0], h2[1])
        # Down O
        new_o = move_down(o, h1, h2, self.grid_size)

        if new_o != o:
            successors["Down_O"] = (h1[0], h1[1], new_o[0], new_o[1], h2[0], h2[1])
        # Left O
        new_o = move_left(o, h1, h2, self.grid_size)

        if new_o != o:
            successors["Left_O"] = (h1[0], h1[1], new_o[0], new_o[1], h2[0], h2[1])
        # Right O
        new_o = move_right(o, h1, h2, self.grid_size)

        if new_o != o:
            successors["Right_O"] = (h1[0], h1[1], new_o[0], new_o[1], h2[0], h2[1])

        # Up H2
        new_h2 = move_up(h2, h1, o, self.grid_size)

        if new_h2 != h2:
            successors["Up_H2"] = (h1[0], h1[1], o[0], o[1], new_h2[0], new_h2[1])
        # Down H2
        new_h2 = move_down(h2, h1, o, self.grid_size)

        if new_h2 != h2:
            successors["Down_H2"] = (h1[0], h1[1], o[0], o[1], new_h2[0], new_h2[1])
        # Left H2
        new_h2 = move_left(h2, h1, o, self.grid_size)

        if new_h2 != h2:
            successors["Left_H2"] = (h1[0], h1[1], o[0], o[1], new_h2[0], new_h2[1])
        # Right H2
        new_h2 = move_right(h2, h1, o, self.grid_size)

        if new_h2 != h2:
            successors["Right_H2"] = (h1[0], h1[1], o[0], o[1], new_h2[0], new_h2[1])

        return successors



    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        # Хевристичка функција која за секоја состојба пресметува минимален
        # број на турнувања на паровите од атоми за тие да се спојат
        state = node.state
        h1 = state[0], state[1]
        o = state[2], state[3]
        h2 = state[4], state[5]
        value = 0

        # проверка за позициите на H1 и O и потребниот број на чекори за да се спојат
        if h1[0] != o[0]:
            if h1[1] != (o[1] - 1):
                # ако атомот на водорот не е во иста редица и во колона веднаш до атомот
                # на кислород ни требаат најмалку 2 турнувања (turn down/up + left/right)
                # за да се спојат
                value += 2
            else:
                # ако атомот на водорот не е во иста редица, но е во колона веднаш до атомот
                # на кислород ни треба најмалку 1 турнувањe (turn up or down) за да се спојат
                value += 1
        else:  # h1[0] == o[0]
            if h1[1] > o[1]:
                # ако атомот на водорот е во иста редица, но во колона од десна страна на
                # атомот на кислород ни требаат најмалку 3 турнувања (turn 2 x down/up + left/right)
                # за да се спојат
                value += 3
            elif h1[1] < (o[1] - 1):
                # ако атомот на водорот е во иста редица, но во колона од лева страна на
                # атомот на кислород ни треба најмалку 1 турнување (turn right) за да се спојат
                value += 1

        # проверка за позициите на H2 и O и потребниот број на чекори за да се спојат
        if h2[0] != o[0]:
            if h2[1] != (o[1] + 1):
                # ако атомот на водорот не е во иста редица и во колона веднаш до атомот
                # на кислород ни требаат најмалку 2 турнувања (turn down/up + left/right)
                # за да се спојат
                value += 2
            else:
                # ако атомот на водорот не е во иста редица, но е во колона веднаш до атомот
                # на кислород ни треба најмалку 1 турнувањe (turn up or down) за да се спојат
                value += 1
        else:  # h2[0] == o[0]
            if h2[1] < o[1]:  # ако атомот на водорот е во иста редица, но во колона од лева страна на
                # атомот на кислород ни требаат најмалку 3 турнувања (turn 2 x down/up + left/right)
                # за да се спојат
                value += 3
            elif h2[1] > (o[1] + 1):
                # ако атомот на водорот е во иста редица, но во колона од десна страна на
                # атомот на кислород ни треба најмалку 1 турнување (turn left) за да се спојат
                value += 1

        if h1[0] == h2[0] and h1[0] != o[0]:
            # ако водородните атоми се во ист ред тогаш можеме да имаме само едно турнување на
            # атомот на кислород up/down (а претходно сме пресметале турнување на H1 и турнување на H2)
            value -= 1

        return value

if __name__=="__main__":
    h1_atom_column = int(input())
    h1_atom_row = int(input())
    o_atom_column = int(input())
    o_atom_row = int(input())
    h2_atom_column = int(input())
    h2_atom_row = int(input())

    molecule = Molecule((h1_atom_column, h1_atom_row, o_atom_column,
                         o_atom_row, h2_atom_column, h2_atom_row))

    answer = astar_search(molecule)
    print(answer.solution())