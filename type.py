def type(stdscr,message,i):
    for char in message:
     stdscr.addstr(char,curses.color_pair(i))
     stdscr.refresh()
     time.sleep(0.05)
