#!/usr/bin/python3

import time
from canvas import Canvas
import random
import string
import curses


# To do- push all the curses crap over to canvas

class Pollock:
    def __init__(self, board):
        self.board = board
        self.screen = board()
        self._spots = set((y,x) for y in range(0,self.board.height - 3)
                          for x in range(0,self.board.width - 3))
        self.chars = string.printable[:-5]

        curses.start_color()
        curses.use_default_colors()
        for i in range(0,curses.COLORS):
            curses.init_pair(i+1, i, -1)

    def add_footer(self,msg):
        message_length = len(msg)
        width = self.board.width
        position = int((width - message_length) / 2)
        self.screen.addstr(self.board.height-2, position,"[{}]".format(msg))
        self.screen.refresh()

    def get_random_spots(self,num):
        return random.sample(self._spots, num)

    def stroke(self):
        num_spots = random.randint(0,int(len(self._spots)/18))
        spots = self.get_random_spots(num_spots)
        char = random.choice(self.chars)
        color = random.choice(range(0,curses.COLORS))
        for spot in spots:
            y,x = spot
            self.screen.addstr(y,x,char,curses.color_pair(color))
        

    def start(self):
        self.board.start()
        count = 0
        while count <= 10020:
            self.stroke()
            count += 1
            time.sleep(.1)
            self.add_footer("-Shhh... Pollock is painting-")
            self.screen.refresh()
        time.sleep(10)
        self.board.stop()


if __name__ == "__main__":
    board = Canvas()
    pol = Pollock(board)
    pol.start()
