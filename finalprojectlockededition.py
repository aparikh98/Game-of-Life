#final project game of life
#Tomer and Aakash
#Cape 2012


import lotterypro
import random
import time
college=1
money = 0
happy = 0
salary = 0
living = 0
communication = 0
car=0
dropout=1
job=1
jackpot=1
jobtimes=0
shoppingtimes=0
mansion=0
apartment=0
SH=0
jet=0
ferrari=0
prius=0
bike=0
android=0
basicp=0
TCT=0
life=0
spouse=0
marrytimes=0
martialarts=0
money2=0
notmoneylottery1=0
education=0
smarts=0

def blackjack():
    global money
    global ComputerHand
    global PlayerHand
    random.seed()
    x=random.randint(1,10)
    y=random.randint(1,10)
    comp1=random.randint(1,10)
    comp2=random.randint(1,10)
    print "Here are your numbers"
    print x
    print y
    print "One of the dealer's cards is"
    print comp1
    total1=x+y
    comptotal1=comp1+comp2
    flag=0
    bet(flag)
    yes=raw_input("Here is your third card (press enter)")
    PlayerHand=total1
    ComputerHand=comp1+comp2
    card1(total1,ComputerHand)
    compplus(comptotal1)
    
def bet(flag):
    global bet1
    bet1=input("How much would you like to bet? (Type a number)")
    global money
    if bet1>money:
        print"You cannot bet that much"
        flag=1
        while flag!=0:
            bet(flag)
            return
    if bet1<=-1:
        print"You cannot bet that much"
        flag=1
        while flag!=0:
            bet(flag)
            return
    if bet1<=money:
        flag==0
        print "Your current money is " +str(money-bet1) + "."
        money=money-bet1
        print 

def win():
    print
    global money
    global bet1
    money=money+bet1+bet1
    print "Your current money is " +str(money) + "."
    print
    print
    shopping()

def compplus(comptotal1):
    z=random.randint(1,10)
    global ComputerHand
    global PlayerHand
    if ComputerHand<17:
        ComputerHand=comptotal1+z
    PlayerHand=PlayerHand
    compare(PlayerHand)
            
def card1(total1,ComputerHand):
    random.seed()
    z=random.randint(1,10)
    total2=total1+z
    print
    print "Your new card is " + str(z) + "."
    if total2>21:
        print
        print "You lose."
        print "Your number is " + str(total2) + "."
        print
        print "You ended up with " +str(money) + "."
        shopping()
    else:
        print
        yes=raw_input("Would you like another card?")
        if yes=="yes" or yes=="Yes" or yes=="y" or yes=="Y":
            card2(total2)
        else:
            PlayerHand=total2
            compare(PlayerHand)

def card2(total2):
    random.seed()
    a=random.randint(1,10)
    total3=total2+a
    print
    print "Your new card is " + str(a) + "."
    if total3>21:
        print
        print "You lose."
        print "Your number is " + str(total3) + "."
        print
        print "You ended up with " +str(money) + "."
        shopping()
    else:
        print
        yes=raw_input("Would you like another card?")
        if yes=="yes" or yes=="Yes" or yes=="y" or yes=="Y":
            card3(total3)
        else:
            PlayerHand=total3
            compare(PlayerHand)
            

def card3(total3):
    random.seed()
    b=random.randint(1,10)
    total4=total3+b
    print
    print "Your new card is " + str(b) + "."
    if total4>21:
        print "You lose."
        print "Your number is " + str(total4) + "."
        print
        print "You ended up with " +str(money) + "."
        shopping()
    else:
        print
        yes=raw_input("Would you like another card?")
        if yes=="yes" or yes=="Yes" or yes=="y" or yes=="Y":
            card4(total4)
        else:
            PlayerHand=total4
            compare(PlayerHand)
            
def card4(total4):
    random.seed()
    c=random.randint(1,10)
    total5=total4+c
    print
    print "Your new card is " + str(c) + "."
    if total5>21:
        print
        print "You lose."
        print "Your number is " + str(total5) + "."
        print
        print "You ended up with " +str(money) + "."
        shopping()
    else:
        PlayerHand=total5
        compare(PlayerHand)
        
def compare(PlayerHand):
    global ComputerHand
    if ComputerHand>PlayerHand:
        print
        print "You lost. Computer had " + str(ComputerHand) + "."
        shopping()
    if ComputerHand==PlayerHand:
        print "The result is a tie."
        print
        blackjack()
    if ComputerHand<PlayerHand:
        print
        print "You win! Computer had " + str(ComputerHand) + "."
        win()

def shopping():
    global money
    global balance
    global living
    global car
    global communication
    global happy
    global shoppingtimes
    global mansion
    global SH
    global apartment
    global jet
    global ferrari
    global prius
    global bike
    global android
    global basicp
    global TCT
    print
    print "You can buy several types of houses:"
    print
    print "(M)ansion ($1500)"
    print "(S)ingle family house ($600)"
    print "(A)partment ($250)"
    print "(N)othing"
    print
    house=raw_input ("Print your choice with a letter (shown in parentheses) ")
    house=house.upper()
    print
    if house == "M" and money<1500:
        print "You can not afford this item."
        print "You were caught trying to steal this item, and were fined 500 dollars."
        money = money-500
    if house == "S" and money<600:
        print "You can not afford this item."
        print "You were caught trying to steal this item, and were fined 500 dollars."
        money = money-500
    if house == "A" and money<250:
        print "You can not afford this item."
        print "You were caught trying to steal this item, and were fined 500 dollars."
        money = money-500
    if house == "M" and money>=1500:
        print "You bought a Mansion"
        print " _Π_____"
        print "/______/~＼"
        print "｜ 田田 ｜門｜"
        money= money-1000
        living=living+10
        mansion=mansion+1
    if house == "S" and money>=600:
        print "You bought a Single Family Home"
        print " _Π_ "
        print "/___\ "
        print "｜田 | "
        money= money-500
        living=living+5
        SH=SH+1
    if house == "A" and money>=250:
        print "You bought an Apartment"
        print "|^|"
        money=  money-200
        living=living+2
        apartment=apartment+1
    print ("You now have $" +str(money) + ".")
    print
    print "You can buy several types of transportation:"
    print
    print "(J)et ($1000)"
    print "(F)errari ($500)"
    print "(T)oyota Prius ($200)"
    print "(B)ike ($50)"
    print "(N)othing"
    print
    vehicle=raw_input ("Print your choice with a letter (shown in parentheses) ")
    vehicle=vehicle.upper()
    print
    if vehicle == "J" and money<1000:
        print "You can not afford this item."
        print "You were caught trying to steal this item, and were fined 500 dollars."
        money = money-500
    if vehicle == "F" and money<500:
        print "You can not afford this item."
        print "You were caught trying to steal this item, and were fined 500 dollars."
        money = money-500
    if vehicle == "T" and money<200:
        print "You can not afford this item."
        print "You were caught trying to steal this item, and were fined 500 dollars."
        money = money-500
    if vehicle == "B" and money<50:
        print "You can not afford this item."
        print "You were caught trying to steal this item, and were fined 500 dollars."
        money = money-500
    if vehicle == "J" and money>=1000:
        print "You bought a Boeing 787."
        money = money-1000
        car=car+10
        jet=jet+1
    if vehicle == "F" and money>=500:
        print "You bought a Ferrari."
        money= money-500
        car=car+4
        ferrari=ferrari+1
    if vehicle == "T" and money>=200:
        print "You bought a Prius."
        money= money-200
        car=car+2
        prius=prius+1
    if vehicle == "B" and money>=50:
        print "You bought an Bike."
        money= money-50
        car=car+1
        bike=bike+1
    print ("You now have $" + str(money) + ".")
    print
    print "You can buy several types of phones:"
    print
    print "(A)ndroid ($150)"
    print "(B)asic Phone ($80)"
    print "(T)in Can Telephone ($30)"
    print "(N)othing"
    print
    phone=raw_input ("Print your choice with a letter (shown in parentheses) ")
    phone=phone.upper()
    print
    if phone == "A" and money<150:
        print "You can not afford this item."
        print "You were caught trying to steal this item, and were fined 500 dollars."
        money = money-500
    if phone == "B" and money<80:
        print "You can not afford this item."
        print "You were caught trying to steal this item, and were fined 500 dollars."
        money = money-500
    if phone == "T" and money<30:
        print "You can not afford this item."
        print "You were caught trying to steal this item, and were fined 500 dollars."
        money = money-500
    if phone == "A" and money>=150:
        print "You bought an Android"
        money= money-150
        communication=communication+3
        android=android+1
    if phone == "B" and money>=80:
        print "You bought a Basic Phone"
        money= money-80
        communication=communication+2
        basicp=basicp+1
    if phone == "T" and money>=30:
        print "You bought an Tin Can Telephone"
        money= money-30
        communication=communication+1
        TCT=TCT+1
    print ("You now have $" + str(money) +".")
    print
    print "You can now donate your money to charities"
    print
    charity=raw_input ("You can choose to donate your money to (G)oogle.org, or (R)ed Cross, or you can choose to be a (M)iser and keep your money. ")
    if charity != "M" and charity != "m" and charity != "G" and charity != "g" and charity != "R" and charity != "r":
        print "Because you did not choose one, you are a miser, this lowers your happiness by making you feel guilty."
        happy = happy-10
    if charity == "G" or charity == "g":
        print "Thank you for donating $10 to google.org."
        money = money-10
        print "You have"
        print "$" + str(money)
        happy=happy+5
    if charity == "R" or charity == "r":
        print "Thank you for donating $10 to Red Cross"
        money = money-10
        print "You have "
        print "$" + str(money)
        happy = happy+5
    if charity == "M" or charity == "m":
        print "You are a miser, and this lowers your happiness by making you feel guilty"
        happy = happy-10
    shoppingtimes=shoppingtimes+1
    if shoppingtimes<7:
        print
        workorlottery=raw_input("Would you like to go to (W)ork or try to win the (L)ottery?")
        workorlottery=workorlottery.upper()
        if workorlottery == "W" or workorlottery == "WORK":
            print
            print
            Job()
        else:
            print
            print
            lotterypro()
    if shoppingtimes>=7:
        print 
        endgame()

def endgame():
    global life
    global money
    global happy
    if money<0 or happy<0:
        print ("You lose because you are in debt or you are depressed. Your money is $" + str(money)+ ".")
        print ("Your happiness level is at " + str(happy) + ".")
    else:
        print "You have reached the end of your life, and you look back at your life."
        print ("The amount of money you have left is $" + str(money) + ".")
        print ("The amount of happiness you have left is " + str(happy) + ".")
        print ("You have " + str(mansion) + " mansion(s)")
        print ("You have " + str(SH) + " single family house(s)")
        print ("You have " + str(apartment) + " apartment(s)")
        print ("You have " + str(jet) + " jet(s)")
        print ("You have " + str(ferrari) + " ferrari(s)")
        print ("You have " + str(prius) + " prius(s)")
        print ("You have " + str(bike) + " bike(s)")
        print ("You have " + str(android) + " android(s)")
        print ("You have " + str(basicp) + " basic phone(s)")
        print ("You have " + str(TCT) + " tin can telephone(s)")
        print
        if spouse==3:
            print "You are married, which is good."
            life=life+3
            print
        if living>=10:
            print "Your living conditions are great!"
            life=life+3
        if living>=5 and living<10:
            print "Your living conditions are moderate."
            life=life+2
        if living<5:
            print "Your living conditions are low."
            life=life+1
        if car>=10:
            print "Your transportation conditions are great!"
            life=life+3
        if car>=5 and car<10:
            print "Your transportation conditions are moderate."
            life=life+2
        if car<5:
            print "Your transportation conditions are low."
            life=life+1
        if communication>=6:
            print "Your communication ability is great!"
            life=life+3
        if communication>=3 and communication<6:
            print "Your communication ability is moderate."
            life=life+2
        if communication<3:
            print "Your communication ability is low"
            life=life+1
        print
        print "Your level of smarts is " + str(smarts) + "."
        if smarts>9:
            print "You are a professor with a PhD in LIFE."
            life=life+3
        if smarts>6 and smarts <=9:
            print "You have a Masters degree in Computer Science."
            life=life+2
        if smarts<=6 and smarts>3:
            print "You weren't the brightest, but you survived."
            life=life+1
        if smarts<=3:
            print "You barely know the alphabet."
        print
        print "Your life score is " + str(life) + "."
        print
        if life==15:
            print "Nobody has had a better life than you!!!!!!!!!"
        if life>=12 and life<=14:
            print "You've had a superb life!!!"
        if life>=10 and life<12:
            print "You've had a fantastic life!!"
        if life==9: 
            print "Your life has been amazing!"
        if life>=4 and life<9:
            print "Your life has been ok."
        if life<4:
            print "You have had a difficult life."
    print
    print "Thank you for playing THE GAME OF LIFE!"
    print
    print  "          /\        /\    "
    print  "         //\\      //\\   "
    print  "        (/\ \\,,,,// /\)  "
    print  "           \ `````` /     "
    print  "          (___)(___)      "
    print  "           (0)  (0)`      "
    print  "            |~   ~ ,      "
    print  "            |      |      "
    print  "            |     /\      "
    print  "            |     |       "
    print  "                  |       "
    print  "           /      |       "
    print  "          /_....__        "
    print  "         /        \       "   
    print  "        |          |      "
    print  "        |          |      "
    print  "        | () ()    |      "   
    print  "        `.        .       "
    print  "          `-------        "
    print
    print
    print "    _        _           _                   _   _____                   "
    print "   /_\  __ _| |____ _ __| |_    __ _ _ _  __| | |_   _|__ _ __  ___ _ _  "
    print "  / _ \/ _` | / / _` (_-< ' \  / _` | ' \/ _` |   | |/ _ \ '  \/ -_) '_| "
    print " /_/ \_\__,_|_\_\__,_/__/_||_| \__,_|_||_\__,_|   |_|\___/_|_|_\___|_|   "
    print "              / __|_ _ ___ __ _| |_(_)___ _ _  ___                       "
    print "              |(__| '_/ -_) _` |  _| / _ \ ' \(_-<                       "
    print "              \___|_| \___\__,_|\__|_\___/_||_/__/                       "
    print
    print "Special thanks to Brandon Wui and Jove Yuan for contributions to Blackjack and Lottery."
    time.sleep(20)
    quit()
    
def collegevacation ():
    global money
    print
    print "Congratulations on graduating from college."
    print "You had some fun, but mainly did a lot of studying. Your education also gave you a better job. What will you do next?"
    print "In order to celebrate your graduation, you are going on a vacation with friends."
    vaca = raw_input("You can go to (L)as Vegas and play in the casino [which you are finally old enough to play in] or go (C)amping with your friends?")
    if vaca == "L" or vaca == "l" or vaca == "LasVegas" or vaca == "Las Vegas" or vaca == "LAS VEGAS" or vaca == "las vegas":
        print "Have fun in Vegas!"
        money = money - 50
        print "It cost you $50 to stay in a casino on the trip."
        print
        print "Balance=$" + str(money)
        print
        print "You have entered the black jack table."
        print
        blackjack()
        return
    if vaca == "C" or vaca == "c" or vaca == "camping" or vaca == "Camping" or vaca == "CAMPING":
        print "You have headed to the beautiful Yosemite National Park."
        money = money-15
        print "It only cost you $15 to stay in a tent at Yosemite."
        print "Balance=$" + str(money)
        hugeparty()
    else:
        print "Try again."
        collegevacation()

def hugeparty():
    global spouse
    global happy
    global money
    global marrytimes
    print
    print "Your friend is hosting a huge party, and his goal is to help people get to know each other."
    friends=raw_input("What type of people are you looking for? (B) for boy, (G) for girl")
    if friends!="B" and friends!="b" and friends!="G" and friends!="g":
        print "Invalid answer."
        hugeparty()
    if friends=="B" or friends=="b":
        spouse=1
        relationship=raw_input ("Are you looking for a love relationship? (Y) or (N)")
        if relationship!="Y" and relationship!="y" and relationship!="N" and relationship!="n":
            print "Invalid answer. Follow the instructions."
            spouse=0
            hugeparty()
        if relationship=="Y" or relationship=="y":
            print "You have found a very attracrive man, and you spend the night with him. In the end, he asks you to marry."
            marry=raw_input ("Do you accept? (Y) or (N)")
            if marry!="Y" and marry!="y" and marry!="N" and marry!="n":
                print "Invalid answer. Follow the instructions!"
                spouse=0
                hugeparty()
            if marry=="Y" or marry=="y":
                print
                print
                marriage()
            if marry=="N" or marry=="n":
                print "Offended, the man walks away. He happens to leave his wallet on the table next to you."
                takeit=raw_input("Do you take it? (Y) or (N)")
                if takeit!="Y" and takeit!="y" and takeit!="N" and takeit!="n":
                    print "Invalid answer. Follow the instructions!!!"
                    spouse=0
                    hugeparty()
                if takeit=="Y" or takeit=="y":
                    print "You found $400 in it, but you feel guilty for taking it and your happiness decreases."
                    happy=happy-10
                    money=money+400
                    print ("You now have $" + str(money) +".")
                    print ("Your happiness is at " + str(happy)+".")
                    Job()
                if takeit=="N" or takeit=="n":
                    print "You leave the wallet, never to know what was inside."
                    Job()
        if relationship=="N" or relationship=="n":
            print "You had a great time, and your happiness has increased."
            happy=happy+5
            print ("Your happiness is at " + str(happy) + ".")
            Job()
    if friends=="G" or friends=="g":
            spouse=2
            relationship=raw_input ("Are you looking for a love relationship? (Y) or (N)")
            if relationship!="Y" and relationship!="y" and relationship!="N" and relationship!="n":
                print "Invalid answer. Follow the instructions."
                spouse=0
                hugeparty()
            if relationship=="Y" or relationship=="y":
                print "You have found a very attracrive woman, and you spend the night with her. In the end, she asks you to marry."
                marry=raw_input ("Do you accept? (Y) or (N)")
                if marry!="Y" and marry!="y" and marry!="N" and marry!="n":
                    print "Invalid answer. Follow the instructions!"
                    spouse=0
                    hugeparty()
                if marry=="Y" or marry=="y":
                    print
                    print
                    marriage()
                if marry=="N" or marry=="n":
                    print "Offended, the woman walks away. She happens to leave her wallet on the table next to you."
                    takeit=raw_input("Do you take it? (Y) or (N)")
                    if takeit!="Y" and takeit!="y" and takeit!="N" and takeit!="n":
                        print "Invalid answer. Follow the instructions!!!"
                        spouse=0
                        hugeparty()
                    if takeit=="Y" or takeit=="y":
                        print "You found $400 in it, but you feel guilty for taking it and your happiness decreases."
                        happy=happy-10
                        money=money+400
                        print ("You now have $" + str(money) +".")
                        print ("Your happiness is at " + str(happy)+ ".")
                    if takeit=="N" or takeit=="n":
                        print "You leave the wallet, never to know what was inside."
                        Job()
            if relationship=="N" or relationship=="n":
                print "You had a great time, and your happiness has increased."
                happy=happy+5
                print ("Your happiness is at " + str(happy) + ".")
                Job()

def marriage():
    global happy
    global money
    global spouse
    global marrytimes
    print
    if spouse==1:
        print "Congratulations on your new husband! Your happiness shoots up, and you received some money from your friends to help you."
        happy=happy+8
        money=money+100
        print ("You now have $" + str(money) + ".")
        print ("Your happiness is at " + str(happy) +".")
        spouse=3
        marrytimes=1
        martialartsfunc()
    if spouse==2:
        print "Congratulations on your new wife! Your happiness shoots up, but you lose some money so you can support the two of you."
        happy=happy+10
        money=money-100
        print ("You now have $" + str(money) +".")
        print ("Your happiness is at " + str(happy)+".")
        spouse=3
        marrytimes=1
        martialartsfunc()

def martialartsfunc():
    global martialarts
    global money
    global happy
    print
    print "Your spouse has encouraged you to take lessons in martial arts to protect yourself against potential attackers. Unfortunately, it is very expensive."
    learnit=raw_input("Do you want to? (Y) or (N)")
    if learnit!="Y" and learnit!="y" and learnit!="yes" and learnit!="Yes" and learnit!="N" and learnit!="n" and learnit!="No" and learnit!="no":
        print "That was not a choice."
        martialartsfunc()
    if learnit=="Y" or learnit=="y" or learnit=="yes" or learnit=="Yes":
        print "You have become a black belt in martial arts."
        print
        print "It cost you $250, and was hard work, so it made you unhappy."
        money=money-250
        happy=happy-8
        print
        print ("You now have $" + str(money) +".")
        print ("Your happiness is at " + str(happy)+".")
        martialarts=1
        print
        Job()
    if learnit=="N" or learnit=="n" or learnit=="No" or learnit=="no":
        print "Your spouse accepts your decision."
        print
        Job()
    
def dropoutvacation ():
    print
    fun = raw_input ("Dropping out of college means no more studying, but it also means, you have a lower paying job. Because of this, you can either choose to (P)arty with your friends or go to the (M)all." )
    if fun == "P" or fun == "p" or fun == "Party" or fun == "party" or fun == "PARTY":
        print "To get clothes for the party, it costs you $30"
        global money
        money = money - 30
        print money
        print "You are having a lot of fun partying! At the party, one of the main hits is a black jack table."
        blackjack()
        return
    if fun == "M" or fun == "m" or fun == "Mall" or fun == "mall" or fun == "MALL":
        print "you can buy several things from the mall"
        shopping()
        return
    else:
        print "Try again."
        dropoutvacation()


def starting():
    global education
    global salary
    global college
    global dropout
    global money
    global happy
    global life
    global smarts
    print " You have just graduated from high school. You have been admitted to your local college, but many of your friends are dropping out."
    print "You have a very important choice to make, which will affect the rest of your life. The rules of life are simple: stay happy, and keep out of bankruptcy. Don't go under 0 in either."
    education1 = raw_input("Do you want to go to (C)ollege or (D)ropout?" )
    if education1 != "C" and education1 != "c" and education1 != "COLLEGE" and education1 != "college" and education1 != "College" and education1 != "D" and education1 != "d" and education1 != "DROPOUT" and education1 != "dropout" and education1 != "Dropout" and education1 != "tomerristhebest" and education1 != "aakashissawesome":
        print "Sorry, you can't do that... Maybe if you get a time machine...."
        print
        print
        starting()
        return
    if education1 == "aakashissawesome":
        happy=happy+100000000000000000000
        salary=110
        money=money+500
        print "You now have $" + str(money) + "."
        print "Your salary is $" + str(salary) + "."
        print "You now have " + str(happy) + " happiness points."
        print "You have bought all of the luxury in the world."
        print
        education=college
        dropoutvacation()
    if education1 == "tomerristhebest":
        money=money+100000000000000000000
        happy=happy+10
        salary=10000
        print "You now have " + str(happy) + " happiness points."
        print "You now have $" + str(money) + "."
        print "Your salary is $" + str(salary) + "."
        print "You have graduated from every college in the world with every degree that there is."
        print
        education=college
        collegevacation()
    if education1 == "C" or education1 == "c" or education1 == "COLLEGE" or education1 == "college" or education1 == "College":
        print "You have enrolled and completed college."
        print "Your salary is "
        salary = 110
        print "$" +str(salary)
        print "your employer paid you $500 to get started"
        money = money + 500
        print ("You have")
        print ("$" + str(money))
        happy = happy - 10
        print "Your happiness level is at"
        print happy
        print "Make sure to make yourself happier!"
        smarts=smarts+3
        print "Your level of smarts is 3."
        education=college
        print
        print
        print "Before your employer assigns you to a position, he wants to test you with some math."
        print
        jobapp()
        collegevacation()
        Job()
    if education1 == "D" or education1 == "d" or education1 == "DROPOUT" or education1 == "dropout" or education1 == "Dropout":
        print "You have dropped out of college to hang out with your friends."
        print "Your salary is "
        salary = 60
        print "$" + str(salary)
        smarts=smarts+1
        print "Your level of smarts is 1."
        print
        print "Your parents gave you $100 to get started"
        money = money + 100
        happy = happy + 10
        print ("You have $")
        print money
        print "This number ranks your happiness level"
        print happy
        education=dropout
        dropoutvacation()
        Job()

def jobapp():
    global money
    global happy
    global salary
    global i
    score=0
    for i in range(5):
        rtest1=random.randint(1,50)
        rtest2=random.randint(1,50)
        test3total=rtest1*rtest2
        print (str(rtest1) + "*" + str(rtest2))
        answertest=raw_input("What is the answer? (Type only one number)")
        if answertest.isdigit():
            if int(answertest)==test3total:
                print "Correct."
                score=score+1
            if int(answertest)!=test3total:
                print "Incorrect."
        else:
            print "Invalid Answer. Therefore it is incorrect."
    if score>=4:
        print
        print "Congratulations! You passed!"
        print "Your boss is very happy with you."
        print
    if score==3:
        print
        print "The boss had overestimated your abilites, and now decides to lower your salary."
        print "Your salary is now $100."
        salary=salary-10
    if score==2:
        print
        print "The boss had overestimated your abilites, and now decides to lower your salary."
        print "Your salary is now $90."
        salary=salary-20
    if score==1:
        print
        print "The boss had overestimated your abilites, and now decides to lower your salary."
        print "Your salary is now $70."
        salary=salary-40
    if score==0:
        print
        print "The boss had overestimated your abilites, and now decides to lower your salary."
        print "Your salary is now $40."
        salary=salary-70
    print
    return
    
def Job():
    global money
    global salary
    global education
    global jobtimes
    global happy
    print
    print "It's the night before you have to go to your job. All of your friends want you to stay up all night to party."
    jobbeginning = raw_input ("Do you want to get ready for your (j)ob, or stay out to (p)arty?" )
    print
    if jobbeginning != "J" and jobbeginning != "j" and jobbeginning != "Job" and jobbeginning != "JOB" and jobbeginning != "job" and jobbeginning != "P" and jobbeginning != "p" and jobbeginning != "Party" and jobbeginning != "PARTY" and jobbeginning !="party":
        print "Try again"
        Job()
    if jobbeginning == "J" or jobbeginning == "j" or jobbeginning == "Job" or jobbeginning == "JOB" or jobbeginning == "job":
        print "Your boss rewards your punctuallity and how prepared you were by giving your paycheck in advance."
        money = money + salary
        print ("You now have $" +str(money) + ".")
        jobtimes=jobtimes+1
        if jobtimes==3:
            promotion()
    if jobbeginning == "P" or jobbeginning == "p" or jobbeginning == "Party" or jobbeginning == "PARTY" or jobbeginning =="party":
        jobyell=random.randint(1,2)
        if jobyell==1:
            print
            print "You woke up late, and came to work tired, your boss took back your bonus, and yelled at you for coming late. Try to come earlier and better prepared next time."
            if education == college:
                money = money - 200
            if education == dropout:
                money = money -80
            print ("You now have $" + str(money) + ".")
            print
            charitytestfunc()
        if jobyell==2:
            print
            print "You were lucky, and the boss was in a good mood."
            print "The party boosted your spirits."
            money=money+salary
            happy=happy+2
            print ("You now have $" + str(money) + ".")
            print ("Your happiness is at " + str(happy) + ".")
            print
            charitytestfunc()
    if jobtimes<3 or jobtimes>5:
        print
        print
        charitytestfunc()
    if jobtimes==4:
        if money>0:
            print
            print "You decided to go gambling."
            blackjack()
        else:
            print
            shopping()
    if jobtimes==5:
        jobtragedyfunc()

def jobtragedyfunc():
    global money
    global happy
    global martialarts
    jobtragedy=random.randint(1,5)
    if jobtragedy==1 or jobtragedy==2 or jobtragedy==3 or jobtragedy==4:
        print
        print "On your way back home, a wild looking man with a pocket knife comes up to you and threatens to attack you if you do not give him a lot of money."
        mugged=raw_input("Do you pay him? (Y) or (N)")
        if mugged!="Y" and mugged!="y" and mugged!="yes" and mugged!="Yes" and mugged!="N" and mugged!="n" and mugged!="No" and mugged!="no":
            print "That was not a choice."
            jobtagedyfunc()
        if mugged=="Y" or mugged=="y" or mugged=="yes" or mugged=="Yes":
            atk=random.randint(1,3)
            if atk==2:
                print "The man attacked you anyway, and took $80 more than the $240 that you paid him."
                print
                print "You are unhappy, but relieved that you weren't injured, and therefore your happiness stays the same."
                money=money-320
                print "You now have $" + str(money) + "."
                print
                print "You decide to try to regain your money and go to the lottery."
                print
                lotterypro()
            else:
                print "You paid the man $240 and he left."
                print
                money=money-240
                print "You are unhappy, but relieved that you weren't injured, and therefore your happiness stays the same."
                print
                print "You now have $" + str(money) + "."
                if money>0:
                    print
                    print "You decide to try to regain your money and go play blackjack."
                    print
                    blackjack()
                else:
                    print
                    print "You decide to go shopping."
                    print
                    shopping()
        if mugged=="N" or mugged=="n" or mugged=="No" or mugged=="no":
            if martialarts==1:
                print "The man came at you and stabbed at you with his knife. Before there was any contact, you remembered that you trained in martial arts."
                print "You grabbed the knife and twisted it out of his hand. Awed, the man ran away, leaving behind $100 that he stole from another person."
                money=money+100
                print
                print "You now have $" + str(money) + "."
                print
                charitytestfunc()
            else:
                print "The man became furious and broke your leg. He then stole $300 from you. You now have to pay another $100 to heal your leg."
                print
                money=money-400
                print "You now have $" + str(money) + "."
                print
                print "You decide to try to regain your money by trying to win the lottery."
                print
                lotterypro()
    else:
        charitytestfunc()
            

def promotion():
    global salary
    global money
    global happy
    print
    print
    print "For coming so many times to your job, you boss offers to promote you."
    print "This will mean no more gambling, because your boss disapproves, but you will receive more money."
    promotionanswer=raw_input("Do you accept? (Y) or (N)")
    if promotionanswer!="Y" and promotionanswer!="y" and promotionanswer!="N" and promotionanswer!="n":
        print "Your boss repeats himself, because he did not understand you."
        promotion()
    if promotionanswer=="Y" or promotionanswer== "y":
        salary=salary+80
        happy=happy-6
        print "Congratulations!, your salary has been raised by $80!"
        print "Unfortunately, you are more stressed now and your happiness has been reduced."
        tragedy()
    if promotionanswer=="N" or promotionanswer=="n":
        happy=happy+3
        print "Your boss accepts your answer and thanks you for your time."
        print "You were nervous about his reaction, and now that it is over you are relieved and happier."
        print ("Your happiness level is " + str(happy) + ".")
        print
        print "You head over to your friend's house to tell him, and find yourself gambling again."
        print
        blackjack()

def tragedy():
    print
    print
    global money
    global happy
    yikes=random.randint(1,2)
    if yikes==1:
        print "On your way home you were thinking about your new promotion, and you did not notice the truck coming at you while you were crossing the street."
        print "Expecting you to stop, the driver was taken by surprise and had to swerve to avoid you."
        print "Unfortunately, he crashed into a Ferrari, and the owner sued you."
        print "You now have to pay $500."
        argue=raw_input("Do you want to argue with his lawyer? (Y) or (N)")
        if argue!="Y" and argue!="y" and argue!="N" and argue!="n":
            print "That was not a choice. As a consequence, you will have to reread the scenario."
            tragedy()
        if argue=="Y" or argue=="y":
            arguerand=random.randint(1,2)
            if arguerand==2:
                money=money-500
                happy=happy-8
                print "The lawyer publicly humiliated you by besting you in an argument."
                print "You have also decreased in happiness."
                print ("Your money is now at $" + str(money) + ".")
                print ("Your happiness is now at " + str(happy) + ".")
            if arguerand==1:
                money=money-150
                happy=happy+2
                print "You managed to convince the lawyer that it was not your fault."
                print "The lawyer managed to convince the Ferrari owner to only sue you for $150 instead of $500."
                print "You also feel satisfied that you convinced a man who argues professionally, and become happier."
                print ("Your money is now at $" + str(money) + ".")
                print ("Your happiness is now at " + str(happy) + ".")
        if argue=="N" or argue=="n":
            money=money-500
            print "You paid him 500 dollars and he forgave you."
            print ("Your money is now at $" + str(money) + ".")
        print
        print "Relieved that you weren't arrested, you go shopping"
        print
        shopping()
    if yikes==2 and marrytimes==0:
        print
        print "Your friend wants to celebrate your promotion."
        hugeparty()
    else:
        print
        print "You wanted to spend your new money trying to win the lottery."
        lotterypro()

def charitytestfunc():
    global smarts
    global happy
    global money
    global martialarts
    global salary
    print "A seemingly poor man comes up to you while you are walking back home."
    print "He asks for some money."
    charitytest=raw_input("Do you give him money? (Y) or (N)")
    if charitytest!="Yes" and charitytest!="yes" and charitytest!="y" and charitytest!="Y" and charitytest!="No" and charitytest!="no" and charitytest!="n" and charitytest!="N":
        print "That is not a valid answer."
        print
        charitytestfunc()
    if charitytest=="Yes" or charitytest=="yes" or charitytest=="y" or charitytest=="Y":
        money=money-30
        happy=happy+3
        print "You gave him $30. He thanks you and leaves."
        print "You feel happy that you helped, and your happiness increases."
        steal=random.randint(1,3)
        if steal==2:
            print "You did not notice that his buddy 'bumped' into you and stole $40 more from you."
            money=money-40
        print ("You now have $" + str(money) + ".")
        print ("Your happiness level is at " + str(happy) + ".")
    if charitytest=="No" or charitytest=="no" or charitytest=="n" or charitytest=="N":
        hurt=random.randint(1,2)
        if hurt==2:
            if martialarts==1:
                print "The man became furious and attacked you. Fortunately, you know martial arts."
                print "You defended yourself and he ran away."
            if martialarts==0:
                print "The man became furious and attacked you. He broke your arm. Now you need to pay $100 to have it healed."
                money=money-100
                print ("You now have $" + str(money) + ".")
        else:
            happy=happy-10
            print "You feel guilty about letting the man starve and lose happiness." 
            print ("Your happiness level is " + str(happy) + ".")
    print
    smartslevelup=raw_input("Would you like to hire a tutor and level up your smarts? (Y) or (N)")
    if smartslevelup=="Y" or smartslevelup=="y" or smartslevelup=="yes" or smartslevelup=="Yes":
        amountsm=input("How many levels do you want to increase in? (Each level costs $400)")        
        checker=money-(amountsm*400)
        if checker<0:
            print
            print "You can not do that. Because you tried to trick your tutor, he decided to not help you, and you hire a new tutor who will come later."
            money=money-100
            print
            print "He charged you $100 to be your tutor."
            print ("You now have $" + str(money) + ".")
        if amountsm<0:
            print
            print "You can not do that. Because you tried to trick your tutor, he decided to not help you, and you hire a new tutor who will come later."
            money=money-100
            print "He charged you $100 to be your tutor."
            print ("You now have $" + str(money) + ".")
        if amountsm>=0 and checker>=0:
            smarts=smarts+amountsm
            money=money-(amountsm*400)
            salary=salary+(amountsm*100)
            print
            print "Your level of smarts is now " + str(smarts) + "."
            print ("You now have $" + str(money) + ".")
            print "Your boss decided to raise your salary to $" + str(salary) + "."
    print
    print "You decide to go shopping."
    print
    shopping()
    
def instructions1():
    print "Welcome to LotteryPro, the only virtual lottery right on your screen!"
    print "Your ticket costs 1/100 of the jackpot."
    bet5()

def lotterypro():
    instructions1()
    
def bet5():
    global jackpot
    global notmoneylottery1
    notmoneylottery=0
    jackpot = input("Enter in the value of the jackpot you would like to play for.")
    global ticketamount
    ticketamount = input("Type (1) to buy your ticket. ")
    if jackpot<=0:
        print "You can not do that"
        print
        notmoneylottery=notmoneylottery+1
    if ticketamount<=0:
        print "You can not do that"
        print
        notmoneylottery=notmoneylottery+1
    if ticketamount>1:
        print "You can not do that, press (1) next time."
        print
        notmoneylottery=notmoneylottery+1
    global wager
    wager = ticketamount * jackpot / 100
    global money
    if wager>money:
        print "You do not have enough money."
        print
        notmoneylottery=notmoneylottery+1
    notmoneylottery1=notmoneylottery1+1
    check(notmoneylottery)
        
def check(notmoneylottery):
    global notmoneylottery1
    global money
    global jackpot
    global ticketamount
    global money2
    global wager
    if notmoneylottery1>=3:
        notmoneylottery1=0
        print
        print "You have tried too many times."
        print
        shopping()
    if notmoneylottery==1:
        bet5()
    if notmoneylottery<3:
        money2=money-wager
        money = money - wager
        print "You purchased a ticket and thus lose $" + str(wager) + ".  You now have $" + str(money) + "."
        main1()
    
def main1():
    i = 0
    global entrylist
    entrytype = raw_input("How would you like to choose your numbers?  (R)andom or (M)anual Entry? ")
    if entrytype == "R" or entrytype == "r" or entrytype == "Random" or entrytype == "random" or entrytype == "RANDOM":
        while i < ticketamount:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            d = random.randint(1, 10)
            e = random.randint(1, 10)
            f = random.randint(1, 10)
            i = i + 1
            print a, b, c, d, e, f 
            entrylist = [a, b, c, d, e, f]
            compare1()
    elif entrytype == "M" or entrytype == "m" or entrytype == "Manual" or entrytype == "manual" or entrytype == "MANUAL":
        while i < ticketamount:
            ma = int(raw_input("Enter in your first number: "))
            mb = int(raw_input("Enter in your second number: "))
            mc = int(raw_input("Enter in your third number: "))
            md = int(raw_input("Enter in your fourth number: "))
            me = int(raw_input("Enter in your fifth number: "))
            mf = int(raw_input("Enter in your sixth number: "))
            i = i + 1
            print ma, mb, mc, md, me, mf
            entrylist = [ma, mb, mc, md, me, mf]
            compare1()
    else:
        print "Invalid entry."
        main1()
        
def compare1():
    COM1 = random.randint (1, 10)
    COM2 = random.randint (1, 10)
    COM3 = random.randint (1, 10)
    COM4 = random.randint (1, 10)
    COM5 = random.randint (1, 10)
    COM6 = random.randint (1, 10)
    global COMlist
    COMlist = [COM1, COM2, COM3, COM4, COM5, COM6]
    global matchingnumbers
    matchingnumbers = [set(COMlist) & set(entrylist)]
    print "The JACKPOT numbers generated by the computer are: " + str(COMlist)
    print "The matching numbers are: " + str(matchingnumbers)
    winnings1()

def winnings1():
    global money
    global jackpot
    global amountmatchingnumbers
    amountmatchingnumbers = len(set(COMlist) & set(entrylist))
    if amountmatchingnumbers == 5:
        money = money + jackpot / 2
    elif amountmatchingnumbers == 6:
        money = money + jackpot
    print
    if money==money2:
        print "You did not win anything."
    print ("You now have $" + str(money) + ".")
    print
    print "That attempt at winning the lottery sure made you want to buy things."
    print
    shopping()

                   
starting()

    
                   

    
    
    
        
    
    
        
    
