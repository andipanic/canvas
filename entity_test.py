#!/usr/bin/python3

from canvas import Canvas
import random

class Entity:
    """Making an entity because it seems like
    the right thing to do on a canvas other than
    draw, which curses does for us fer free"""
    def __init__(self, x, y, canvas):
        """Set the entities position and let
        it know what its currently standing on"""
        self.x = x
        self.y = y
        self.canvas = canvas

    def move(self):
        """Should probably be overriden for
        each type of entity created, but for
        testings sake, we're saying this one
        can move randomly in any direction
        around it including standing still
        
        to-do:
            make a good ol' move validator,
            tis what makes the moves good!
        
        """
        possible_moves = set((x,y) for x in range(-1,2) 
                                for y in range(-1,2))
        choice = random.sample(possible_moves,1)[0]
        x, y = choice
        self.x += x
        self.y += y

    def char(self):
        """This probably comes later in the ol'
        classes we build later, so we'll fake mock
        it out here... this guy is where he's @"""
        return '@'

def main():
    """Set up a screen for a good entity named a
    to walk around randomly on.  Until we tell him
    what moves are valid (because we have electro-
    shock boarders on right now (and always)) 
    he will die always!"""
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
