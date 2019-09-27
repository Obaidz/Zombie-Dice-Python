from sys import exit
cup = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
values = [3, 4, 6, 0, 0, 0, 0, 0, 0]
names = []
SBF = [0, 0, 0]     # SHOTGUNS ,  BRAINS, FOOTPRINTS.
players = int(raw_input("How many players will play? ")) 
scores = [z * 0 for z in range(0, players)]

def intro(n):
    if n > 0:
        for items in range(0, (n)):
            name = str(raw_input("Write player %s names: " % (str(items))))
            names.append(name)
        



def dice(n, val, x):
    redGunshots = 0
    redFeet = 0
    redBrain = 0
    yelGunshots = 0
    yelFeet = 0
    yelBrain = 0
    greenGunshots = 0
    greenFeet = 0
    greenBrain = 0
    from random import randint    # Importing random from library.
    t = 1
    while t < 4:     #range = 0, 1, 2

        x[12] = val[0] + val[1] + val[2]       # x12 is total dice
        
        if (x[12] < 3):
            if x[12] < 0:
                print "Not enough dice to through"
                
            print "Not enough dice to throw. Adding Brain to the cup."
            x[12] = x[12] + x[0] + x[3] + x[6]
            x[0] = 0
            x[3] = 0
            x[6] = 0

            print x[12]
        
            

        random = randint(1, (x[12] + 1))

        if random <= val[2]:
            val[2] -= 1
            val[5] += 1
        elif random > val[2] + val[1]:
            val[0] -= 1
            val[3] += 1
        elif random > val[2] and random <= (x[12] - val[0]):
            val[4] += 1
            val[1] -= 1
        else:
            print "No dice selected"
            print random
        t += 1


    totalleft = val[0] + val[1] + val[2]
    while val[3] > 0:
        dice_red = randint(1, 7)
        if dice_red == 1:
            redBrain += 1
        elif dice_red >= 2 and dice_red <= 3:
            redFeet += 1
        else:
            redGunshots += 1
        
        val[3] -= 1

    
    while val[5] > 0:
        dice_green = randint(1, 7)
        if dice_green == 1:
            greenGunshots += 1
        elif dice_green > 1 and dice_green < 4:
            greenFeet += 1
        else:
            greenGunshots += 1

        val[5] -= 1
        
    
    while val[4] > 0:
        dice_yellow = randint(1, 7)
        if dice_yellow >= 1 and dice_yellow < 3:
            yelGunshots += 1
        elif dice_yellow > 2 and dice_yellow < 5:
            yelFeet += 1
        else:
            yelBrain += 1  

        val[4] -= 1
        

    val[6] = redBrain + greenBrain + yelBrain    # Total brain
    val[7] = redFeet + yelFeet + greenFeet      #Total feet
    val[8] = redGunshots + greenGunshots + yelGunshots   #total gunshots

    x[0] += redBrain
    x[1] += redFeet
    x[2] += redGunshots 
    x[3] += greenBrain
    x[4] += greenFeet
    x[5] += greenGunshots
    x[6] += yelBrain
    x[7] += yelFeet
    x[8] += yelGunshots


    print "Gunshots: %d" % val[8],
    print ", Brains: %d" % val[6],
    print ", Feet: %d" % val[7]
    print "Total red dice left = %d, Total green dice left = %d, total yellow dice left = %d." % (val[0], val[2], val[1])
    print "Total dice left: %d" % totalleft

    return x
    return val
    return n



def ask2(g, va, cu, na): 
    currentplayer = 0
    y = ""
    while y is not "Q":
        print
        print "%s's turn" % names[currentplayer]
        y = str(raw_input("Enter P to play, ENTER C to change turns, Q to quit: "))
        print
        
        if y == "P":
            dice(SBF, values, cup)
            
             
            
            TotalBrains = cu[0] + cu[6] + cu[3]
            TotalGunshots = cu[2] + cu[5] +cu[8]        # Getting total amount of B , G, F.
            TotalFeet = cu[1] + cu[4] +cu[7]

            cu[9] = cu[9] + va[3]         # storing red dices from values list to cup list so that dices will get subtracted every time we roll dice.
            cu[10] = cu[10] + va[4]       # storing yellow dices
            cu[11] = cu[11] + va[5]       # storing green dices
            
            if TotalGunshots >= 4:
                print "You have been hit 3 times, Next player turn."
                TotalGunshots = 0
                cu[9] = 0
                cu[10] = 0
                cu[11] = 0
                cu[2] = 0
                cu[5] = 0
                cu[8] = 0
                TotalBrains = 0
                cu[0] = 0
                cu[3] = 0
                cu[6] = 0
                TotalFeet = 0
                cu[1] = 0
                cu[4] = 0
                cu[7] = 0
                print "Refilling cup"
                va[0] = 3 
                va[1] = 4
                va[2] = 6
                cu[12] = va[0] + va[1] + va[2]
                currentplayer += 1

                if currentplayer == g:
                    currentplayer = 0
                    
        
            if scores[currentplayer] > 13:
                print "WOOOOOOOOOOOOOOOON "
                exit(0)

            print "Total Gunshots = %d, Total Brains = %d, total Feet = %d." % (TotalGunshots, TotalBrains, TotalFeet)
            

        elif y == "Q":
            print "Quitting..."
            exit(0)

        elif y == "C":
            scores[currentplayer] = scores[currentplayer] + TotalBrains
            TotalGunshots = 0
            cu[2] = 0
            cu[5] = 0
            cu[8] = 0
            cu[9] = 0
            cu[10] = 0
            cu[11] = 0
            print "Refilling cup"
            va[0] = 3 
            va[1] = 4
            va[2] = 6
            cu[12] = va[0] + va[1] + va[2]
            TotalBrains = 0
            cu[0] = 0
            cu[3] = 0
            cu[6] = 0
            TotalFeet = 0
            cu[1] = 0
            cu[4] = 0
            cu[7] = 0
            currentplayer += 1
            print "Total player %s score is %d" % (names[currentplayer - 1], scores[currentplayer - 1])
            if currentplayer == g:
                currentplayer = 0
                TotalBrains = scores[currentplayer]

        else:
            print "Wrong Input, Try again",
            ask2(players, values, cup, names)  
    
    

def main(g, va, cu, p):
    total_dice = 13
    intro(players)
    ask2(players, values, cup, names)
    print p
    
        
    
main(players, values, cup, scores)
  




    



