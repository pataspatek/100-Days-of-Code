from turtle import Screen

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

BACKGROUND_COLOR = "black"

TITLE = "Pong"


class Window():

    def __init__(self):
        '''Initializes a new Window object'''

        self.screen = Screen()
        self.screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.screen.title(TITLE)
        self.screen.tracer(0)


    def key_listener(self, element):
        self.screen.listen()

        self.screen.onkey(element.up, element.keys[0])
        self.screen.onkey(element.down, element.keys[1])
