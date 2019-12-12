#! /usr/bin/env python3
import sys

DEBUG = False

def main(args):
    paths = []

    f = open(args[1], 'r')
    for p_desc in f.readlines():
        if p_desc.strip() == "":
            continue
        paths.append(Path(p_desc))

    print(nearest_intersection(paths))


class Path:
    def __init__(self, description):
        self.desc = [x for x in description.strip().split(',')]
        self.spaces = [Node(0,0)]

    def spaceSet(self):
        log("Existing Spaces: %s" % self.spaces)
        for step in self.desc:
            new_spaces = self.spaces[-1].takeStep(step)
            log("New Spaces: %s" % new_spaces)
            self.spaces += new_spaces
        return set(self.spaces)

    def __str__(self):
        return "%s" % self.desc

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return self.__key().__repr__()

    def __key(self):
        return (self.x, self.y)

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())

    def takeStep(self, step):
        direction = step[0]
        num = int(step[1:])
        log("stepping: %s -> %s, %s" % (step, direction, num))
        if direction == 'U':
            return self.stepUp(num)
        elif direction == 'D':
            return self.stepDown(num)
        elif direction == 'L':
            return self.stepLeft(num)
        elif direction == 'R':
            return self.stepRight(num)
        else:
            raise ValueError("direction not recognized: '%s'" % direction)


    def stepUp(self, num):
        return [Node(self.x, self.y + i) for i in range(1, num + 1)]

    def stepDown(self, num):
        return [Node(self.x, self.y - i) for i in range(1, num + 1)]

    def stepRight(self, num):
        return [Node(self.x + i, self.y) for i in range(1, num + 1)]

    def stepLeft(self, num):
        return [Node(self.x - i, self.y) for i in range(1, num + 1)]

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y, other.y)

def nearest_intersection(paths):
    print("Path 0: %s" % paths[0])
    print("Path 1: %s" % paths[1])
    print("Set 0: %s" % paths[0].spaceSet())
    print("Set 1: %s" % paths[1].spaceSet())
    intersections = paths[0].spaceSet() & paths[1].spaceSet()
    # for p in paths:
        # print("Intersections: %s" %intersections)
        # intersections = intersections & p.spaceSet()
    print("Intersections: %s" % intersections)

def log(msg):
    if DEBUG:
        print(msg)

if __name__ == "__main__":
    main(sys.argv)
