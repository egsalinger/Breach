#generator.py
import sys

class MapGenerator:
 """This class is the main random floor generator. We will
 call this some number of times for each house we're building.
 The way this will work is as follows:

 1) Given a house of size (x, y), the house consists of walls (X's)
 and empty space (.'s).
 A sample house will look like this:
 XXXXXXXXXXXXXXX
 X.............X
 X.............X
 X.............X
 X.............X
 X.............X
 X.............X
 X.............X
 X.............X
 XXXXXXXXXXXXXXX

 2) Given the random house, add additional walls.
 3) Add doors randomly, until all rooms in the house
 are connected.
 4) Add at least one entrance/exit.
 5) To add: Windows, hallways, multiple floors."""


 def __init__ (self, width, length):
  self.width = width
  self.length = length

  # empty map containing nothing
  x = 0
  wall = 'X'
  floor = '.'
  self.map = []
  for y in range (0, length):
   temp = ''
   for x in range (0, width):
    if (x == 0 or y == 0 or x == width-1 or y == length-1):
     temp += wall
    else:
     temp += floor

    self.map.append(temp)
   if DEBUG:
    self.print_map()

 def printMap(self):	 
  for row in self.map:
   print row



DEBUG = False
FAILED = False
x = 5
y = 5
if len (sys.argv) == 3:
 x = int (sys.argv[1])
 y = int (sys.argv[2])
 if x == 0 or y == 0:
  FAILED = True
 if DEBUG:
  print "Running with ", x, ",", y

elif len (sys.argv) != 1:
 FAILED = True
if FAILED:
 print "Improper usage. Correct usage:\n\tGenerator.py length width"
 print "Provided ", len(sys.argv), " args."
 sys.exit (1)

map = MapGenerator(x,y)
map.PrintMap()
