#generator.py
import sys
import random

class MapGenerator:
 """This class is the main random floor generator. We will
 call this some number of times for each house we're building.
 The way this will work is as follows:

 1) Given a house of size (x, y), the house consists of walls (X's)
 and empty space (.'s).
 A sample house will look like this:
 XXXXXXXXXXXXXXX
 X.X......X....X
 X.X......X....X
 X.X......X....X
 X.X......X....X
 XXXXXXXXXXXXXXX
 X.X...........X
 X.X...........X
 X.X...........X
 XXXXXXXXXXXXXXX

 2) Given the random house, add additional walls.
 3) Add doors randomly, until all rooms in the house
 are connected.
 4) Add at least one entrance/exit.
 5) To add: Windows, hallways, multiple floors."""
 
 wall = 'X'
 floor = '.'

 def createFloor (self, width, length):
  self.width = width
  self.length = length

  # empty map containing nothing
  x = 0
  self.map = []
  for x in range (0, width):
   temp = []
   for y in range (0, length):
    if (x == 0 or y == 0 or x == width-1 or y == length-1):
     temp.append(self.wall)
    else:
     temp.append (self.floor)
   self.map.append(temp)

  if DEBUG:
   self.printMap()

  # Assume each space = 25 sqft and account for outside.
  area = (length-2)*(width-2)

  # Assume 100 sqft = average room size
  # Each space = 25 sqft.
  # TODO: Walls should be thinner, and placed in between tiles.
  numWalls = int(area/8)
  self.generateWalls(numWalls)
  if DEBUG:
   self.printMap()

 def generateWalls(self, howMany):
  i = 0
  while i < howMany:
   #TODO: Change room generation to find possible spaces for corners
   # and then pick random valid choices
   x = random.randint (0, self.width-1)
   y = random.randint (0, self.length-1)
   neighbors = self.getNeighbors (x,y)
   if self.wall not in neighbors:
    self.makeWall (x, y)
   i +=1


 def getNeighbors (self, x, y):
  neighbors = []
  if x < self.width-1:
   neighbors.append (self.map [x+1][y])
  if x > 0:
   neighbors.append (self.map [x-1][y])
  if y < self.length -1:
   neighbors.append (self.map [x][y+1])
  if y > 0:
   neighbors.append (self.map [x][y-1])

  return neighbors


 def makeWall (self, x, y):
  curx = x
  cury = y
  self.changeToTile (curx, cury, self.wall)

  while curx > 0:
   curx -=1
   if self.map [curx][cury] is self.wall:
    break
   self.changeToTile (curx, cury, self.wall)

  curx = x

  while curx < self.width -1:
   curx +=1
   if self.map [curx][cury] is self.wall:
    break
   self.changeToTile (curx, cury, self.wall)

  curx = x
  
  while cury > 0:
   cury -=1
   if self.map [curx][cury] is self.wall:
    break
   self.changeToTile(curx, cury, self.wall)
  cury = y

  while cury < self.length-1:
   cury +=1
   if self.map [curx][cury] is self.wall:
    break
   self.changeToTile (curx, cury, self.wall)
  cury = 1

 def changeToTile (self, curx, cury, tile):
   self.map [curx][cury] = tile
   if DEBUG:
    self.printMap()
   

 def printMap(self):	 
  for row in self.map:
   for col in row:
    print col,
   print ''
  print "\n"



DEBUG = False
FAILED = False
x = 5
y = 5
if len (sys.argv) == 3:
 x = int (sys.argv[1])
 y = int (sys.argv[2])
 if x <= 0 or y <= 0:
  FAILED = True
 if DEBUG:
  print "Running with ", x, ",", y

elif len (sys.argv) != 1:
 FAILED = True
if FAILED:
 print "Improper usage. Correct usage:\n\tGenerator.py length width"
 print "Provided ", len(sys.argv), " args."
 sys.exit (1)

map = MapGenerator()
map.createFloor (x, y)
map.printMap()
