##SNOWFALL.PY##
##It's Christmas##


import curses
from curses import wrapper
import random
from random import choice
class snowflake:
        posX = 0
        posY = 0
        def __init__(self, posY, posX):
                self.posX = posX
                self.posY = posY

def main(stdscr):
	curses.cbreak()
	curses.noecho()
	#stdscr.nodelay(True)
	curses.curs_set(False)
	running = True
	maxYX = stdscr.getmaxyx()
	snowArr = initSnowflakes(1,maxYX[1])
	while running:
		stdscr.clear() 
		stdscr.addstr(0,0, str(maxYX[0]) +" "+ str(maxYX[1]))
		moveSnowFlakes(snowArr,maxYX)
		drawSnowflakes(snowArr, stdscr)
		stdscr.refresh()
		c = stdscr.getch()
		if c == ord( 'q' ):
			running = False	
		else:
			pass
	stdscr.clear()
	stdscr.addstr(0,0, "Program Closed: Press Any Key")
	stdscr.refresh()
	stdscr.getkey()

def moveSnowFlakes(snowArr, maxYX):
##Check if a snowflake is beyond screen limits (maxYX) and 
##Move it if it is.  (Currently only checks the Y value)
	for sf in snowArr:
		if sf.posY > maxYX[0]-1:
			sf.posY = 0
			sf.posX = choice(range(0, maxYX[1]))
		sf.posY +=1;

def initSnowflakes(i, maxX):
	snowArr = list()
	for x in range(0,i):
		snowArr.append(snowflake(0, choice(range(0, maxX))))
	return snowArr

def drawSnowflakes(snowArr,stdscr):
	for sf in snowArr:
		stdscr.addstr(sf.posY,sf.posX,str(sf.posY))

wrapper(main)	
