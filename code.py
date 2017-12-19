import sys
import math
#Destroy the mountains before your starship collides with one of them. For that, shoot the highest mountain on your path.
# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

d = {}
# game loop
while True:    
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        print("Mountain Ht.. " + str(i) +  str(mountain_h), file=sys.stderr)
        d[i] = mountain_h        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    pp = max(zip(d.values(), d.keys()))
    print ("dict max" + str(pp), file=sys.stderr)
    # The index of the mountain to fire on.
    print (pp[1])                
    
