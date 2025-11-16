from KiTUI import App, VBox
import curses

class MyApp(App):
    def __init__(self, stdscr):
        super().__init__(stdscr)

    def compose(self):
        return VBox(
           
        )

def main(stdscr):
    app = MyApp(stdscr)
    app.start()
    app.run()

if __name__ == "__main__":
    curses.wrapper(main)