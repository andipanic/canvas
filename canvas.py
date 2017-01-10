#!/usr/bin/python3

import curses
import subprocess

class Canvas:
    """Bootstrapping some curses stuff into a class
    we can use later to build curses games and or
    simulations and maybe even both at the same
    time"""
    def __init__(self):
        """Create the screen and set the max width
        and max height of the screen in width and height"""
        self.screen = curses.initscr()
        self.height, self.width = self.screen.getmaxyx()

    def start(self):
        """Set up the curses env and put a boarder
        around it... might remove boarder later. """
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.screen.keypad(True)
        self.screen.clear()

    def __call__(self):
        """Not sure if I should use __call__ here
        but it is a very simple way to get the screen."""
        return self.screen

    def window(nlines, ncols, begin_y=0, begin_x=0):
        window = curses.newwin(nlines, ncols, begin_y, begin_x)
        return window

    def stop(self):
        """Clean up ncurses state settings and reset
        the terminal back to the way it was."""
        self.screen.clear()
        self.screen.keypad(False)
        curses.curs_set(1)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

def main():
    """ Quick instantiation and test to make sure
    whatever we type into the term shows up."""
    board = Canvas()
    board.start()
    c = 0
    while 1:
        scr = board()
        try:
            c = scr.getch()
        except KeyboardInterrupt:
            board.stop()
            break
        if c is ord('q'):
            board.stop()
            break
        scr.addch(5,5,str(chr(c)))
        scr.refresh()


if __name__ == '__main__':
    main()
    
