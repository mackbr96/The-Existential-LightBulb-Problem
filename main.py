import random
import sys
start = ""


sys.setrecursionlimit(6000)

class Switch:
    def __init__(self):
        self.pointsTo = []
    
    def add(self, num):
        self.pointsTo.append(num)

class NotSwitch:
    def __init__(self):
        self.pointsTo = []
    
    def add(self, num):
        self.pointsTo.append(num)



def graph(bulbs, switches): #Makes the graph
    sw = []
    nsw = []
    for i in range(0,len(switches)):
        s = Switch()
        ns = NotSwitch()
        sw.append(s)
        nsw.append(ns)


    for i in range(0, len(bulbs)):
        first = bulbs[i][0]
        second = bulbs[i][1]

        if( second > 0):
            nsw[abs(second) - 1].add(first)
        else:
            sw[abs(second) - 1].add(first)
        if( first > 0):
            nsw[abs(first) - 1].add(second)
        else:
            sw[abs(first) - 1].add(second)
        '''
            Not second depends on first
            Not first depends on second
        '''

    for i in range(1,len(switches) + 1):
        one, two = walkGraph(sw, nsw, i * -1 ,i, []), walkGraph(sw, nsw, i, i*-1, []) #Check to see if there is a contridiction
        if(one != [] and two != []): #There is a contridiction
            print(one)
            print("blah")
            print(two)    
            return False #There is no solution

    print("***Finished graph check a solution is possible***")
    return True #There is a possible solution


def walkGraph(sw, nsw, og, i, done): #Walk the graph check for a loop back to the negated first switch
    if( i in done):
        return []
    else:
        done.append(i)
    if(i > 0):
        if(og in sw[i-1].pointsTo): #THIS IS BAD
            done.append(og)
            return done
        else:
            for x in range(0,len(sw[abs(i)-1].pointsTo)):
                if(walkGraph(sw, nsw, og, sw[i-1].pointsTo[x], done) != []): return done
                else:
                    return []
    else:
        if(og in nsw[abs(i)-1].pointsTo): #THIS IS BAD
            done.append(og)
            return done
        else:
            for x in range(0,len(nsw[abs(i)-1].pointsTo)):
                if(walkGraph(sw, nsw, og, nsw[abs(i)-1].pointsTo[x], done)) != []: return done
                else:
                    return []
    return []

def checkAll(swithces, bulbs): #Checks if all bulbs are on
    global bulbNum
    for i in range (0,bulbNum):
        first = bulbs[i][0]
        second = bulbs[i][1]
        if(switches[abs(first) -1] != first and switches[abs(second) -1] != second):
            return False

    return True


def checkbulb(bulbs, switches):
    global switchNUm
    global bulbNum
    i = random.randint(0,bulbNum-1)
    first = bulbs[i][0]
    second = bulbs[i][1]
    if(checkAll(switches, bulbs)): #All bulbs are on!
            return -1
    while(switches[abs(first)-1] == first or switches[abs(second)-1] == second ): #Find an off bulb, turn it on
        i = random.randint(0,bulbNum-1)
        first = bulbs[i][0]
        second = bulbs[i][1]
        
    x = i
    i = random.randint(0,1)
    switches[abs(bulbs[x][i])-1] = switches[abs(bulbs[x][i]) -1] * -1 #flip the switch
    if(checkAll(switches, bulbs)): #check if all are on now
            return -1
    return 0



def formatBulb(bulbs):
    array = []
    for i in range(0, len(bulbs)):
        s1 = ""
        s2 = ""
        foundSpace = False
        for x in bulbs[i]:
            if(x == " "):
                foundSpace = True

            if foundSpace == False:
                s1 += x
            else:
                s2 += x
    
        array.append(tuple([int(s1),int(s2)]))
    return array

infile = "text2.txt" #File to test

with open(infile, "r") as f:
    bulbs = []
    for line in f:
        bulbs.append(line)

switchNUm =  int (bulbs[0])
bulbNum = int (bulbs[1])
print("Switch Num is " + str(switchNUm))
print("Bulb Num is "+ str(bulbNum))

bulbs.pop(0) #Remove switch num
bulbs.pop(0) #Remove bulb num
bulbss = formatBulb(bulbs)
switches = []
for i in range(1, switchNUm+1):
    r = random.randint(0,1)
    if( r == 0): switches.append(i)
    else: switches.append(i * -1)
count = 0

while(checkbulb(bulbss, switches) != -1):
    count += 1
    if count > 5: #Quick check
        print("NO RANDOM SOLUTION FOUND")
        print("TESTING USING GRAPH")
        if( graph(bulbss, switches) == True): #A solution is possible Run till we find it
            while(checkbulb(bulbss, switches) != -1):
                continue

            print(switches)
            exit()
        else: #No solution is possible
            print("No solution possible")
            exit()

print(switches) #Print switches if a solution is found in the quick check
