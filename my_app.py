from KiTUI import App, VBox
import curses

class MyApp(App):
    def __init__(self, stdscr):
        super().__init__(stdscr)

    def compose(self):
        return VBox(
		border_style="solid"           
        )

def main(stdscr):
    app = MyApp(stdscr)
    app.start()
    app.run()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        # Silently exit on keyboard interrupt
        pass
