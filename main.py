#!/usr/bin/env python3
import curses, socket, sys, time


def scan(host, start=1, end=1024, timeout=0.08):
    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        ok = s.connect_ex((host, port)) == 0
        s.close()
        yield port, ok


def draw(stdscr):
    curses.curs_set(0)
    host = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 1024
    open_ports = []
    stdscr.nodelay(True)
    for port, ok in scan(host, 1, end):
        if ok: open_ports.append(port)
        stdscr.erase()
        h, w = stdscr.getmaxyx()
        pct = port / end * 100
        fill = int((w-20) * pct / 100)
        stdscr.addstr(0, 2, f'ASCII PORTSCAN - {host} - q to stop')
        stdscr.addstr(2, 2, '[' + '#' * fill + '-' * max(0, w-20-fill) + f'] {pct:5.1f}%')
        stdscr.addstr(4, 2, f'Current port: {port}')
        stdscr.addstr(6, 2, 'Open ports:')
        for i, p in enumerate(open_ports[-(h-8):], 7):
            stdscr.addstr(i, 4, f'{p}/tcp open')
        if stdscr.getch() in (ord('q'), ord('Q')): return
    stdscr.addstr(min(curses.LINES-1, 7 + len(open_ports)), 2, 'Done. Press any key.')
    stdscr.nodelay(False); stdscr.getch()


if __name__ == '__main__':
    curses.wrapper(draw)
