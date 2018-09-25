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



def graph(bulbs, switches):
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

    #for i in range(0,len(sw)):
        #print("Switch " + str(i + 1) + " points to " + str(sw[i].pointsTo))
        #print("Switch NOT " + str(i + 1) + " points to " + str(nsw[i].pointsTo))
    for i in range(1,len(switches) + 1):
        if(walkGraph(sw, nsw, i * -1 ,i, []) and walkGraph(sw, nsw, i, i*-1, [])):
            print("Switch " + str(i) + " Is a problem")
        '''else:
            print("ALL IS GOOD")'''
    print("***Finished***")


def walkGraph(sw, nsw, og, i, done):
    if( i in done):
        #print("done")
        return False
    else:
        done.append(i)
    #done = sorted(done)
    if(i > 0):
        if(og in sw[i-1].pointsTo):
            #print("THIS IS BAD.")
            return True
            #walkGraph(sw, snw, og * -1, og)
        else:
            for x in range(0,len(sw[abs(i)-1].pointsTo)):
                if(walkGraph(sw, nsw, og, sw[i-1].pointsTo[x], done)): return True
    else:
        if(og in nsw[abs(i)-1].pointsTo):
            #print("THIS IS BAD.")
            return True
            #walkGraph(sw, snw, og * -1, og)
        else:
            for x in range(0,len(nsw[abs(i)-1].pointsTo)):
                if(walkGraph(sw, nsw, og, nsw[abs(i)-1].pointsTo[x], done)): return True


def checkAll(swithces, bulbs):
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
    if(checkAll(switches, bulbs)):
            return -1
    while(switches[abs(first)-1] == first or switches[abs(second)-1] == second ):
        i = random.randint(0,bulbNum-1)
        first = bulbs[i][0]
        second = bulbs[i][1]
        
    x = i
    i = random.randint(0,1)
    switches[abs(bulbs[x][i])-1] = switches[abs(bulbs[x][i]) -1] * -1
    if(checkAll(switches, bulbs)):
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

infile = "text1.txt"

with open(infile, "r") as f:
    bulbs = []
    for line in f:
        bulbs.append(line)

switchNUm =  int (bulbs[0])
bulbNum = int (bulbs[1])
print("Switch Num is " + str(switchNUm))
print("Bulb Num is "+ str(bulbNum))

bulbs.pop(0)
bulbs.pop(0)
bulbss = formatBulb(bulbs)
switches = []
for i in range(1, switchNUm+1):
    r = random.randint(0,1)
    if( r == 0): switches.append(i)
    else: switches.append(i * -1)
count = 0

while(checkbulb(bulbss, switches) != -1):
    count += 1
    if count > len(switches) * 10:
        print("NO RANDOM SOLUTION FOUND")
        print("TESTING USING GRAPH")
        graph(bulbss, switches)
        exit()

print(switches)
print("yes")
