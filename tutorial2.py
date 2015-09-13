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
mycircle = CircleAsset(5, thinline, blue)
[Sprite(mycircle, (a, sin(radians(a))*100+50)) for a in range(0,360,5)]
#mysprites = [Sprite(mycircle, (x*randint(2,10), x*randint(2,10))) for x in range(100)]
#mysprite = Sprite(myrectangle, (300, 300))

def step():
    pass

myapp = App()
myapp.run(step)
