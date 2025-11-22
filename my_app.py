from KiTUI import App, VBox, Label
import curses

class MyApp(App):
    def __init__(self, stdscr):
        super().__init__(stdscr)

    def compose(self):
        return VBox(
			Label(content="Hello World", bindings=[]),
			VBox(
				Label(content="Inner VBOX", binding=[]),
				bindings=[],
				padding="3",
			),
			bindings=[],
			border_style="double",           
			padding="5"
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
