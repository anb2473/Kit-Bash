# KiTUI

## Widget Structure

The KiTUI engine will use a dynamic widget system.

### This system begins at the App class

```python
class MyApp(App):
    def __init__(self):
        super().__init__()

    def compose(self):
        return VBox(
            Label("Hello"),
            Label("World"),
            padding=1
        )
```

In this example the MyApp class, containing the app state, is created, inheriting from the App class.

1. On super().__init__() the App class automatically handles initiating the system
    a. The App class begins an asynchronous blocking process which ensures that the terminal dimensions remain in bounds
    b. The App class begins handling io bindings
2. The App provides a .render() method (**we will return to this**)
3. The compose method returns a vertical box with two *children lables, and **modifiers for padding

### How the Render System Works

The render function finishes 3 tasks

1. Clear the terminal
2. Check for io input
    a. If the input targets a key binding (i.e. SHIFT + L) the app changes the actively focused object to the respective object in the binding
    b. If the input does not target a key binding the input is piped to the focusable object
3. Render the widget tree
    a. For each object create a buffer of the dimensions the object should occupy, and render the object in those dimensions
    b. Once the object is rendered, render each child and insert the child buffers into the parent buffer
