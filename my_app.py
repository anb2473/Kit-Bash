from KiTUI import App, VBox

class MyApp(App):
    def __init__(self):
        super().__init__()

    def compose(self):
        return VBox(
           
        )

if __name__ == "__main__":
    app = MyApp()
    app.start()