import random
import time
import threading
import signal
import os

class monster:
    def __init__(self):
        self.health = 0
    def print_me(self):
        print("Health:", self.health)

class drakon(monster):
    def __init__(self):
        monster.__init__(self)
    def setter(self):
        self.health = 200
    def print_me(self):
        print("Health:", self.health)

class demigod:
    def __init__(self):
        self.attack = 0
        self.defence = 0
        self.health = 0
        self.powers = 0
    def print_basics(self):
        print("Attack:", self.attack)
        print("Defence:", self.defence)
        print("Health:", self.health)
        print("Powers:",self.powers)
    def print_me(self):
        self.print_basics()

class zeus(demigod):
    def __init__(self):
        demigod.__init__(self)
        #special stats?

    def setter(self):
        self.attack = random.randint(20,50)
        self.defence = random.randint(20,50)
        self.health = 50
        self.powers = random.randint(100,170)

    def print_me(self):
        self.print_basics()

    #class lightning(powers):
        #attack("lightning")

class athena(demigod):
    def __init__(self):
        demigod.__init__(self)
        #special stats?

    def setter(self):
        self.attack = random.randint(20,50)
        self.defence = random.randint(20,50)
        self.health = 50
        self.powers = random.randint(100,150)

    def print_me(self):
        self.print_basics()

class apollo(demigod):
    def __init__(self):
        demigod.__init__(self)
        #special stats?

    def setter(self):
        self.attack = random.randint(20,50)
        self.defence = random.randint(20,50)
        self.health = 50
        self.powers = random.randint(50,150)

    def print_me(self):
        self.print_basics()

class ares(demigod):
    def __init__(self):
        demigod.__init__(self)
        #special stats?

    def setter(self):
        self.attack = random.randint(35,50)
        self.defence = random.randint(20,50)
        self.health = 50
        self.powers = 300

    def print_me(self):
        self.print_basics()

class hephaestus(demigod):
    def __init__(self):
        demigod.__init__(self)
        #special stats?

    def setter(self):
        self.attack = random.randint(35,50)
        self.defence = random.randint(20,50)
        self.health = 50
        self.powers = random.randint(100,150)

    def print_me(self):
        self.print_basics()


#basic layout

#enter parent,name, weapon of choice
#roll for the stats

def count():
    global ran
    ran = True
    print()

def attacked():
    global c
    timer = threading.Timer(5,count)
    timer.start()
    c = input()

def attack(user, parent, weapon, enemyhealth):
    #user.powers
    #based on attack skill?
    enemyhealth = enemyhealth - user.attack
    return enermyhealth

#should break the fighting scenes into multiple chunks of ifs depending on health etc
#gives more choices

print("Look, you didn't want to be a half-blood.")
time.sleep(1.5)
print("Well, too bad. However many years ago, a Greek god met your parent, and they had...", end='')
time.sleep(2)
print(" you.")
time.sleep(1)
print("(Zeus, Athena, Apollo, Ares and Hephaestus)")
parent = input("Choose your godly parent: ")
print()
print("Now choose your weapon. Depending on your godly parent you may have more affiliation with a certain type of weapon")
#add weapon skills for the dif parents: ares, apollo
#if you chose the correct weapons you automatically get a boost in combat

print("(sword, bow, dagger)")
weapon = input("Choose your weapon of choice: ")

match parent:
    case "Zeus":
        user = zeus()
    case "Athena":
        user = athena()
    case "Apollo":
        user = apollo()
    case "Ares":
        user = ares()
    case "Hepheastus":
        user = hepheastus()
        
user.setter()
print()
print("Your stats:")
user.print_me()
print()
drakon = drakon()
drakon.setter()

print(f"A child of {parent}, eh? Use your powers wisely to defeat your enemi- DRAKON!")
time.sleep(2)
print()
print("A drakon has just spotted you. Defeat it, or be defeated.")
print("1: 'Explain to me what a drakon is'")
print("2: 'Start fighting'")
expl = int(input())
if expl==1:
    print("Check wikipedia.")
print()
print("There are timed choices ahead, each allowing 5 seconds. Be quick or be defeated.")
time.sleep(2)
print()
print("Drakon health:",drakon.health)
print("You focus on the drakon, preparing to fight.")
time.sleep(1)


print()
print("The drakon runs at you, spitting acidic venom!")
time.sleep(1)
print("1: 'Freeze'")
print("2: 'Dodge'")
print("3: 'Hesitate'")

ran=False
attacked()
print()

if ran == True:
    c=0
    print("\nToo slow")

match c:
    case '2':
        print("You dodge out of the way in time.")
    case _:
        print("You get hit and can immediately feel the effects.")
        user.health = user.health - 20
        print("Health:",user.health)

print()
time.sleep(2)
print("You see the drakon readying itself again.")
time.sleep(1)
#options are supposed to change based on class
print("1: 'Run away'") #preferably not a thing if ares
print(f"2: 'Use your {weapon}'")
print("3: 'Scream really loudly'")

c = int(input())
print()
if c == 1:
    print("The drakon blocks your path.")
elif c==3:
    print("The drakon looks at you unimpressed.")

time.sleep(1)
print()
print(f"You ready your {weapon}.")
time.sleep(1)
a = input("Press enter to attack!")
print()
print("Your attack glances off its titanium scales and does no harm.")
print()

time.sleep(1)
print("The drakon paralyses you with its fearsome stare.")
print("1: 'Attack its eyes'")
print("2: 'Stop and stare'")
print("3: 'Close your eyes'")

ran=False
attacked()
print()

if ran == True:
    c=0
    print("\nToo slow")

if c=='1':
    print("You successfully attack its eyes.")
    drakon.health = drakon.health - 50
    print("Drakon health:",drakon.health)
    print("You have made the drakon mad.")
print()
time.sleep(1)
print("The drakon crushes you.")
user.health = 0
print("Health: ",user.health)


        
#ways to win:
#run away
#ares op
#attack the eyes 

#ok there's no way to win this

