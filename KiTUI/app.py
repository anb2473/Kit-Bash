import curses

class App():
    def __init__(self, stdscr):
        self.min_width, self.min_height = 80, 24

        self.focused_obj = None
        self.bindings = {}

        self.stdscr = stdscr
        curses.curs_set(0)        # hide cursor
        self.stdscr.nodelay(True)      # non-blocking input
        self.stdscr.keypad(True)       # capture arrow keys

    def collect_bindings(self):
        for child in self.root.children:
            self.bindings.update({binding: child for binding in child.bindings})
            self.collect_bindings(child)

    def run(self):
        while True:
            # clear terminal
            self.stdscr.clear()

            # handle focused obj state
            key = self.stdscr.get_wch()

            # pipe IO to focused obj
            
            # render
            self.stdscr.refresh()

    def start(self):
        self.root = self.compose()
        