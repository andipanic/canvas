#!/usr/bin/python3

from canvas import Canvas
import random

class Entity:
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.canvas = canvas

    def move(self):
        possible_moves = set((x,y) for x in range(-1,2) for y in range(-1,2))
        choice = random.sample(possible_moves,1)[0]
        x, y = choice
        self.x += x
        self.y += y

    def char(self):
        return '@'

def main():
    c = Canvas()
    a = Entity(15,15,c)

    c.start()
    screen = c()
    for i in range(10000):
        a.move()
        screen.addch(a.y,a.x,a.char())
        screen.refresh()
        if c is ord('q'):
            c.stop()


if __name__ == "__main__":
    main()
