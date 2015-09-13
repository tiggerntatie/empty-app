from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset
from math import sin, cos, radians, degrees


# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
bluecircle = CircleAsset(5, thinline, blue)
redcircle = CircleAsset(5, thinline, red)
[Sprite(bluecircle, (a, sin(radians(a))*100+100)) for a in range(0,360,5)]
[Sprite(redcircle, (a, cos(radians(a))*100+100)) for a in range(0,360,5)]

def step():
    pass

myapp = App()
myapp.run(step)
