import curses 
from curses import wrapper 
import queue 
import time 


maze = [
    ["#","#","#","#","#","O","#","#","#"],
    ["#"," "," "," "," "," "," "," ","#"],
    ["#"," ","#","#"," ","#","#"," ","#"],
    ["#"," ","#"," "," "," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#","#","#"],
    ["#"," "," "," "," "," "," "," ","#"],
    ["#","#","#","#","#","#","#","X","#",],
]

def main(stdscr):
    #adding colors
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    #blue_and_black = curses.color_pair(1)  

    stdscr.clear()
    stdscr.addstr(5,0,"Hello World")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)
