import curses
import time

class App():
    def __init__(self, stdscr):
        self.min_width, self.min_height = 80, 24

        self.focused_obj = None
        self.bindings = {}

        self.stdscr = stdscr
        curses.curs_set(0)        # hide cursor
        self.stdscr.nodelay(True)      # non-blocking input
        self.stdscr.keypad(True)       # capture arrow keys

    def collect_bindings(self, root):
        for child in getattr(root, 'children', []):
            self.bindings.update({binding: child for binding in getattr(child, 'bindings', [])})
            self.collect_bindings(child)

    def run(self):
        # Create a virtual window
        original_height, original_width = self.stdscr.getmaxyx()
        vwin = curses.newwin(original_height, original_width, 0, 0)
        while True:
            # Check for change in window dimensions, and update vwin
            height, width = self.stdscr.getmaxyx()
            if (height != original_height or width != original_width):
                vwin.resize(height, width)

            # Clear virtual window
            vwin.erase()

            # handle focused obj state
            try:
                key = self.stdscr.get_wch()
            except curses.error:
                key = None
            
            if key in self.bindings:
                self.focused_obj = self.bindings.get(key)
            elif self.focused_obj is not None: # pipe IO to focused obj
                self.focused_obj.on_focus(key)

            # render
            buffer = self.root.render(width, height)
            lines = buffer.splitlines()

            for y, line in enumerate(lines):
                try:
                    vwin.addstr(y, 0, line)
                except curses.error:
                    pass  # line too long for terminal

            # Push virtual window to screen without refreshing immediately
            vwin.noutrefresh()

            # Update the screen all at once
            curses.doupdate()

    def start(self):
        self.root = self.compose()
        self.collect_bindings(self.root)
        
