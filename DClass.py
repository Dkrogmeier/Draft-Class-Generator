import random


#-------------------List of Names---------------------
draft = []
name_list = open("DClass.txt","r")
POS = ['QB','OL','WR']

#---------------------End List of Names------------------------


POS = ['QB','OL','WR']

class Player:

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.passing = []
        self.blocking = []
        self.catching = []

    def QB(self, grades):
        self.passing.append(grades)

    def OL(self, grades):
        self.blocking.append(grades)

    def WR(self, grades):
        self.catching.append(grades)

def makeDraftClass():
    for x in name_list:
        x = Player(x.strip().title(),random.choice(POS))
        if x.position == 'QB':
            x.QB(random.randint(70,92))
            x.OL(random.randint(10,33))
            x.WR(random.randint(10,50))
            draft.append(x)
        elif x.position == 'WR':
            x.WR(random.randint(70,92))
            x.OL(random.randint(30,55))
            x.QB(random.randint(30,55))
            draft.append(x)
        elif x.position == 'OL':
            x.OL(random.randint(70,92))
            x.WR(random.randint(20,40))
            x.QB(random.randint(30,60))
            draft.append(x)

    print("\n-------DRAFT CLASS GENERATOR-----------")
    for m in draft:
        print(m.name, m.position, "Passing: ", m.passing, "Catching: ", m.catching, "Blocking: ", m.blocking, sep = " ")


makeDraftClass()

#variable = Player('tom','qb')
#variable = Player(draft[2],POS[random.randint(0,2)])

#variable.OL/QB/WR('A/B/C/D')   ASSIGNMENT
#variable.blocking/passing/catching   CHECK



