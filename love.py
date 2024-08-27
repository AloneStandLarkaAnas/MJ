import curses
import time
import random

def draw_hearts(stdscr):
    curses.curs_set(0)  # Hide the cursor
    sh, sw = stdscr.getmaxyx()  # Get screen height and width
    hearts = ['❤️', '💛', '💚', '💙', '💜']
    
    while True:
        stdscr.clear()
        for _ in range(1000):  # Number of hearts to display
            y = random.randint(0, sh - 1)
            x = random.randint(0, sw - 1)
            stdscr.addstr(y, x, random.choice(hearts))
        
        stdscr.refresh()
        time.sleep(0.1)  # Adjust the speed of the rain effect

def zoom_out_text(stdscr):
    curses.curs_set(0)  # Hide the cursor
    sh, sw = stdscr.getmaxyx()  # Get screen height and width
    text = "Alone Stand Larka love with you"
    zoom = 1
    max_zoom = min(sh, sw) // 2  # Maximum zoom level
    
    while zoom < max_zoom:
        stdscr.clear()
        y = sh // 2 - zoom
        x = sw // 2 - len(text) * zoom // 2
        for i in range(zoom):
            stdscr.addstr(y + i, x, text, curses.A_BOLD)
        stdscr.refresh()
        zoom += 1
        time.sleep(0.5)  # Adjust the speed of zooming out

def main(stdscr):
    # Draw hearts rain
    draw_hearts(stdscr)
    # After hearts rain, start zooming out text
    zoom_out_text(stdscr)

curses.wrapper(main)
