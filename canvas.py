#!/usr/bin/python3

import curses
import subprocess

class Canvas:
    def __init__(self):
        self.screen = curses.initscr()
        self.width = int(subprocess.check_output(['tput','cols']))
        self.height = int(subprocess.check_output(['tput','lines']))

    def start(self):
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)
        self.screen.clear()
        self.screen.border()

    def __call__(self):
        return self.screen

    def stop(self):
        self.screen.clear()
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()

def main():
    board = Canvas()
    board.start()
    c = 0
    tick = 0
    while c is not ord('q'):
        tick += 1
        scr = board()
        c = scr.getch()
        scr.addch(5,5,str(chr(c)))
        scr.refresh()

    board.end()

if __name__ == '__main__':
    main()
    
