def solve():
    global numheads,numlegs
    numheads = int(input())
    numlegs = int(input())
    x = (float(numlegs) - float(2 * numheads))/2
    y = float(numheads) - x
    print( "Rabbits:",x,  "Chickens:",y)
    
solve()
