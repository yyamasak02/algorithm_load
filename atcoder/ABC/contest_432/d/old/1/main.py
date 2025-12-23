from dataclasses import dataclass
from copy import copy


@dataclass
class Coord:
    ldx: int
    ldy: int
    rux: int
    ruy: int

    def copy(self):
        return copy(self)

    def change(self, dlx, dly, drx, dry):
        self.ldx += dlx
        self.ldy += dly
        self.rux += drx
        self.ruy += dry

    def to_tuple(self):
        return (self.ldx, self.ldy, self.rux, self.ruy)

    def calc(self):
        return (self.rux - self.ldx + 1) * (self.ruy - self.ldy + 1)


class Groups:
    def __init__(self, size):
        self.size = size
        self.groups: list[set[int]] = [{key} for key in range(size)]
        self.index_to_group = {key: key for key in range(size)}

    def merge(self, a: int, b: int) -> None:
        a_index = self.index_to_group[a]
        b_index = self.index_to_group[b]
        if a_index == b_index:
            return
        self.groups[a_index] |= self.groups[b_index]
        for e in self.groups[b_index]:
            self.index_to_group[e] = a_index
        self.groups[b_index] = set()

    @property
    def show(self):
        print(self.groups)
        print(self.index_to_group)


def main():
    groups: list[Coord] = []
    n, x, y = map(int, input().split())
    groups.append(Coord(0, 0, x - 1, y - 1))
    for _ in range(n):
        query = input().split()
        c, a, b = query[0], int(query[1]), int(query[2])
        new_groups: list[Coord] = []
        for group in groups:
            ldx, ldy, rux, ruy = group.to_tuple()
            if c == "X":
                if ldx >= a:
                    new_groups.append(Coord(ldx, ldy + b, rux, ruy + b))
                elif rux < a:
                    new_groups.append(Coord(ldx, ldy - b, rux, ruy - b))
                else:
                    new_groups.append(Coord(ldx, ldy - b, a - 1, ruy - b))
                    new_groups.append(Coord(a, ldy + b, rux, ruy + b))
            else:
                if ldy >= a:
                    new_groups.append(Coord(ldx + b, ldy, rux + b, ruy))
                elif ruy < a:
                    new_groups.append(Coord(ldx - b, ldy, rux - b, ruy))
                else:
                    new_groups.append(Coord(ldx - b, ldy, rux - b, a - 1))
                    new_groups.append(Coord(ldx + b, a, rux + b, ruy))
        groups = new_groups
    group_size = len(groups)
    d = Groups(group_size)
    for i in range(group_size - 1):
        for j in range(i + 1, group_size):
            s = groups[i]
            t = groups[j]
            x_touch = not (s.rux + 1 <= t.ldx) and not (t.rux + 1 <= s.ldx)
            y_touch = not (s.ruy + 1 <= t.ldy) and not (t.ruy + 1 <= s.ldy)
            is_touch = False
            if (s.rux + 1 == t.ldx) or (t.rux + 1 == s.ldx):
                if y_touch is True:
                    is_touch = True
            if (s.ruy + 1 == t.ldy) or (t.ruy + 1 == s.ldy):
                if x_touch is True:
                    is_touch = True
            if is_touch is True:
                d.merge(i, j)
    answers = []
    for elements in d.groups:
        if not elements:
            continue
        tmp = 0
        for e in elements:
            tmp += groups[e].calc()
        answers.append(tmp)
    answers.sort()
    print(len(answers))
    print(*answers)
    return


if __name__ == "__main__":
    main()
