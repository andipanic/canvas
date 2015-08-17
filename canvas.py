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
        self.width = int(subprocess.check_output(['tput','cols']))
        self.height = int(subprocess.check_output(['tput','lines']))

    def start(self):
        """Set up the curses env and put a boarder
        around it... might remove boarder later. """
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)
        self.screen.clear()
        self.screen.border()

    def __call__(self):
        """Not sure if I should use __call__ here
        but it is a very simple way to get the screen."""
        return self.screen

    def stop(self):
        """Clean up ncurses state settings and reset
        the terminal back to the way it was."""
        self.screen.clear()
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()

def main():
    """ Quick instantiation and test to make sure
    whatever we type into the term shows up."""
    board = Canvas()
    board.start()
    c = 0
    while c is not ord('q'):
        scr = board()
        c = scr.getch()
        scr.addch(5,5,str(chr(c)))
        scr.refresh()

    board.end()

if __name__ == '__main__':
    main()
    
