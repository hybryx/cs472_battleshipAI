from battleship import *

session = game()

"""
session.placeShip("2", 0, (0,0), (0,4))
session.placeShip("2", 1, (1,0), (4,0))
session.placeShip("2", 2, (9,7), (9,9))
session.placeShip("2", 3, (8,7), (8,9))
session.placeShip("2", 4, (3,3), (3,4))
session.printShip("2")

session.fire("1", (0,0))
session.fire("1", (0,1))
session.fire("1", (0,2))
session.fire("1", (0,3))
session.fire("1", (0,4))
session.fire("1", (1,0))
session.fire("1", (2,0))
session.fire("1", (3,0))
session.fire("1", (4,0))
session.fire("1", (3,3))
session.fire("1", (3,4))
session.fire("1", (3,5))
session.fire("1", (8,7))
session.fire("1", (8,8))
session.fire("1", (8,9))
session.fire("1", (9,7))
session.fire("1", (9,8))
session.fire("1", (9,9))

session.printShot("1")


print(session.checkWin("1"))
"""
#session.genRandomMap()
#session.printShip("2")
#session.randomShot(10000)
session.heatMapMode(1)

"""
# Custom heatmap testing
#shotMap = [['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X', ' '], [' ', 'X', ' ', 'X', ' ', 'X', ' ', '!', ' ', '!'], ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X', '!'], [' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', '!'], ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', '!', ' '], [' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', '!'], ['X', ' ', 'X', ' ', '!', ' ', '!', ' ', 'X', ' '], ['X', 'X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'], [' ', 'X', 'X', ' ', 'X', ' ', 'X', ' ', 'X', ' '], [' ', ' ', 'X', ' ', ' ', 'X', ' ', 'X', ' ', ' ']]  
shotMap = [['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X', ' '], [' ', 'X', ' ', 'X', ' ', 'X', ' ', '!', ' ', '!'], ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X', '!'], [' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', '!'], ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', '!', ' '], [' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', '!'], ['X', ' ', 'X', ' ', '!', ' ', '!', ' ', 'X', ' '], ['X', 'X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'], [' ', 'X', 'X', ' ', 'X', ' ', 'X', ' ', 'X', ' '], [' ', ' ', 'X', ' ', ' ', ' ', ' ', '!', ' ', ' ']]  
heatMap = session.heatMap(shotMap, "Shot")

for x in range(len(heatMap)):
	for y in range(len(heatMap[x])):
		print("|" + str(heatMap[x][y]).ljust(2), end = ' ')
	print()


| X  |    | X  |    | X  |    | X  |    | X  |    |		 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  
|    | X  |    | X  |    | X  |    | !  |    | !  |		 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  
| X  |    | X  |    | X  |    | X  |    | X  | !  |		 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  
|    | X  |    | X  |    | X  |    | X  |    | !  |		 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  
| X  |    | X  |    | X  |    | X  |    | !  |    |		 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  
|    | X  |    | X  |    | X  |    | X  |    | !  |		 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  
| X  |    | X  |    | !  |    | !  |    | X  |    |		 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  
| X  | X  |    | X  |    | X  |    | X  |    | X  |		 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  
|    | X  | X  |    | X  |    | X  |    | X  |    |		 | 1  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 1  
|    |    | X  |    |    | X  |    | X  |    |    |		 | 2  | 1  | 0  | 2  | 1  | 0  | 0  | 0  | 1  | 2 
"""
