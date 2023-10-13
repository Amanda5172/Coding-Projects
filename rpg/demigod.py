import random

class demigod:
    def __init__(selfself):
        self.name = ""
        self.attack = 0
        self.defence = 0
        self.health = 0
        self.experience = 0
        self.powers = 0
    def print_basics(self):
        print("Name:", self.name)
        print("Attack:", self.attack)
        print("Defence:", self.defence)
        print("Health:", self.health)
        print("Experience:", self.experience)
        print("Powers:",self.powers)
    def print_me(self):
        self.print_basics()
    def print_intro(self):
        print("This is an exciting story.")
    class weapon:
        def attack(wep):
            print("You strike with your", wep)
    class powers:
        def attack(pow):
            print("You attack with your",pow)

class zeus(demigod):
    def __init__(self):
        zeus.__init__(self)
        #special stats?

    def setter(self,name):
        self.name = name
        self.attack = random.randint(20,50)
        self.defence = random.randint(20,50)
        self.health = random.randint(0,50)
        self.powers = random.randint(100,170)

    def print_me(self):
        self.print_basics()

    #class lightning(powers):
        #attack("lightning")

class poseidon(demigod):
    def __init__(self):
        poseidon.__init__(self)
        #special stats?

    def setter(self,name):
        self.name = name
        self.attack = random.randint(20,50)
        self.defence = random.randint(20,50)
        self.health = random.randint(0,50)
        self.powers = random.randint(100,170)

    def print_me(self):
        self.print_basics()

class hades(demigod):
    def __init__(self):
        hades.__init__(self)
        #special stats?

    def setter(self,name):
        self.name = name
        self.attack = random.randint(20,50)
        self.defence = random.randint(20,50)
        self.health = random.randint(0,50)
        self.powers = random.randint(100,170)

    def print_me(self):
        self.print_basics()

class ares(demigod):
    def __init__(self):
        ares.__init__(self)
        #special stats?

    def setter(self,name):
        self.name = name
        self.attack = random.randint(35,50)
        self.defence = random.randint(20,50)
        self.health = random.randint(0,50)
        self.powers = 300

    def print_me(self):
        self.print_basics()

class hephaestus(demigod):
    def __init__(self):
        ares.__init__(self)
        #special stats?

    def setter(self,name):
        self.name = name
        self.attack = random.randint(35,50)
        self.defence = random.randint(20,50)
        self.health = random.randint(0,50)
        self.powers = random.randint(70,150)

    def print_me(self):
        self.print_basics()






#useer = demigod()
#user.weapon.attack(weapon of choice)
#user.powers.attack(powers based on parents)
#user.print_me()

parent = input("Who is your godly parent out of the olympians ig? ")
#godly parent, have extra stats based on that
#if not you're a mortal and you die, yay, probably - you can't see the monster tho??
#zeus, poseidon, hades, dionysus, hephaestus, athena, (hera), artemis?, aphrodite, ares, hermes, apollo, demeter

#everyone has a weapon - sword & shield, bow, dagger = wep

#we're gonna go fight a hydra ig - health like 250 300??
#only way to beat is burn the stumps // run away





#basic layout

#enter parent,name, weapon of choice
#roll for the stats

#on a quest

#zeus kids
#lightning

#poseidon
#water powers?? controlling water
#you need help sorry

#hades
#? unless you summon skeletons or smt. can sense death
#depending on power you will most likely win

#ares
#the red glowing blessing of mars, you WILL defeat your enemy


#dionysus


#hephaestus
#craft, give choices of what to craft, give choices of what to do with it
#there's a way to win with everything as long as you use it right
#if powers level is high enough, you are flammable

#apollo
#bow powers or your terrible singing confuses(there's a better word that starts with d but 
# it's not disillusioned or disfigured) it or you give it a disease
#bow powers kinda useless ngl
#singing could probably drive it off or you can run away
#disease has a chance of killing depnding on which you choose

#hunter of artemis
#you get natural backup if you are close to death
#every stat is boosted cos immortality
#can win by yourself if you pick all right

#favoured mortal of hera
#might die without a team ngl

#







