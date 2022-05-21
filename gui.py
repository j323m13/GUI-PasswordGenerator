from guizero import App, Text

app = App(title="Hello world")
app.bg = "white"

message = Text(app, text="Welcome to the Hello world app!")

button = PushButton(app, text="Press me", command=change_message)

app.display()