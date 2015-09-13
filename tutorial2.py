from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset
import math

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)
mycircle = CircleAsset(5, thinline, blue)
xcoordinates = range(0, 360, 10)
redcircle = CircleAsset(5, thinline, red)

# Generate a list of sprites that form a line!
blsprites = [Sprite(mycircle, (x, 100+100*math.sin(math.radians(x)))) for x in xcoordinates]
resprites = [Sprite(redcircle, (x, 350+100*math.cos(math.radians(x)))) for x in xcoordinates]

myapp = App()
myapp.run()
