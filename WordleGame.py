
#Vstr: Versuch, Lstr: Lösungsstring
def determine_color(Vstr, Lstr, i) :
    erg=[]
    if Vstr[i] not in Lstr :
        erg.append("grey")
    elif Vstr[i] == Lstr[i] :
        pass


def check_all_found(Vstr, Lstr, i) :
    retVal = True



class Answer :
    def __init__(self, Versuch):
        self.Versuch = Versuch.lower()
        self.first = Versuch[0]
        self.second = Versuch[1]
        self.third = Versuch[2]
        self.forth = Versuch[3]
        self.fifth = Versuch[4]

        #Wörterbuch, dass jedem existenten Buchstaben
        #in unserem Versuch seine Indizes, an denen er versucht wurde, zuordnet
        self.wb_ind = {}
        for ind in range(0, len(self.Versuch)) :
            elem=self.Versuch[ind]
            if elem not in self.wb_ind.keys() :
                self.wb_ind[elem] = [ind]
            else :
                self.wb_ind[elem] = self.wb_ind[elem] + [ind]
        
        #dudenList soll dann eine Liste mit erlaubten Wörtern sein
        #if Versuch in dudenList:
        if True :
            self.isWord = True
        else: self.isWord = False

class RoundOfPlay:
    def __init__(self, solution):
        self.solution = solution.lower()
        self.tries_left = 6

        self.wb_ind = {}
        for ind in range(0, len(self.solution)) :
            elem=self.solution[ind]
            if elem not in self.wb_ind.keys() :
                self.wb_ind[elem] = [ind]
            else :
                self.wb_ind[elem] = self.wb_ind[elem] + [ind]
    

    def __str__(self):
        ret = "Versuche übrig: {}\n Lösung: {}".format(self.tries_left, self.solution)
        return ret
    

    def change_solution(self, new_solution) :
        self.solution = new_solution
        self.wb_ind = {}
        for ind in range(0, len(self.solution)) :
            elem=self.solution[ind]
            if elem not in self.wb_ind.keys() :
                self.wb_ind[elem] = [ind]
            else :
                self.wb_ind[elem] = self.wb_ind[elem] + [ind]


    
    def eval_try(self, Versuch):
        if Versuch.isWord :
            self.tries_left -= 1
            output = []  #-1: grey; 0: orange; 1: green; 2: green and orange
            for i in range(0, len(self.solution)):
                vb = Versuch.Versuch[i]  #VersuchsBuchstabe: vb
                if vb not in self.solution :  #vb nicht in Lösung
                    output.append(-1)
                elif vb != self.solution[i] :  #vb hier falsch
                    output.append(0)

                #siehe python built-in all()
                #https://www.geeksforgeeks.org/python-check-if-one-list-is-subset-of-other/
                elif all(index in Versuch.wb_ind[vb] for index in self.wb_ind[vb]) :  #alle Positionen von vb in der Lösung gefunden
                    output.append(1)
                else:
                    output.append(2)  #KEINE ECKIGEN KLAMMERN!!!
            print(output)
            return output
        else:
            print("Kein korrektes Wort eingegeben!!")
            return [-11]

            

RundenObj = RoundOfPlay("Engel")
Versuch1 = Answer("Angel")

print(RundenObj)
RundenObj.eval_try(Versuch1)
print(RundenObj)