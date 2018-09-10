import random

def checkAll(swithces, bulbs):
    right = 0
    #print("Bulbs = ")
    #print(bulbs)
    for i in bulbs:
        first = i[0]
        second = i[1]
        #print(first)
        #print(second)
        if first < 0:
            firstNeg = True
            first *= -1
        else:
            firstNeg = False
            
        if second < 0:
            second *= -1
            secondNeg = True
        else:
            secondNeg = False

        #print("First is " + str(first) + " and switch is " + str(switches[first - 1]) + " and neg is " + str(firstNeg))
        #print("Second is " + str(second) + " and switch is " + str(switches[second - 1]) + " and neg is " + str(secondNeg) )
        first -= 1
        second -= 1

        right += 1

            
        if(check(firstNeg, switches[first]) == False and check(secondNeg, switches[second]) == False):
            #print(right)
            return False
    print("TRUE")

    return True



def check(neg, number):
    if(neg == True and number == 0):
        return True
    elif(neg == True and number == 1):
        return False
    elif neg == False and number == 1:
        return True
    elif neg == False and number == 0:
        return False
    else:
        return False

def checkbulb(bulbs, switches):
    global switchNUm
    global bulbNum
    i = random.randint(0,bulbNum-1)
    first = bulbs[i][0]
    second = bulbs[i][1]
    if first < 0:
        firstNeg = True
        first *= -1
    else:
        firstNeg = False
    if second < 0:
        second *= -1
        secondNeg = True
    else:
        secondNeg = False
    first -= 1
    second -= 1
    #print(first)
    #print(second)
    #print(len(switches))
    #while(check(firstNeg, switches[first]) or check(secondNeg, switches[second])):
    while(check(firstNeg, switches[first]) or check(secondNeg, switches[second])):
        i = random.randint(0,bulbNum - 1)
        first = bulbs[i][0]
        second = bulbs[i][1]
        if first < 0:
            firstNeg = True
            first *= -1
        else:
            firstNeg = False
        if second < 0:
            second *= -1
            secondNeg = True
        else:
            secondNeg = False
        first -= 1
        second -= 1
        if(checkAll(switches, bulbs)):
            return -1
        
    x = i
    i = random.randint(0,1)
    #print((bulbs[x][i])-1)
    switches[abs(bulbs[x][i])-1] = (switches[abs(bulbs[x][i])-1] * -1) + 1
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
for i in range(0, switchNUm):
    i = random.randint(0,1)
    switches.append(i)
count = 0
while(checkbulb(bulbss, switches) != -1):
    count += 1
    if count > 99999:
        print("BIG NO")
        exit()
    print("no")
#print(bulbss)
print(switches)
print("yes")
