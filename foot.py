def foot(stdscr,footer_win,i):
    footer_win.refresh()
    footer_win.addstr(0,0,"Press any key to continue.", curses.color_pair(i) | curses.A_BOLD)
    stdscr.refresh()
    footer_win.refresh()
    stdscr.getch()
