from tkinter import *
from tkinter import ttk
import WordleGame

#PROBLEM: wb_ind wird im Objekt Runde out of date sein!!!!!!------------------------------------- 

# jetzt wird ein Runden-Objekt erzeugt
Runde = WordleGame.RoundOfPlay("Angel")

# hier wird definiert, wie die Lösung eingegeben werden kann
# und wie die Lösung dann in dem Runden-Objekt gesetzt wird
def get_lsg(event) :
    solution = lsg_frame.get()
    if len(solution) != 5 :
        print("Fehler! Länge der Lösung muss 5 sein!")
        return -1
    Runde.solution = solution
    for i in range(0,5) :
        VersuchsMuster[1].inhalt[i].configure(text=str(solution[i]))
        #print(VersuchsMuster[1])#.inhalt[i]))#.configure(text=str(solution[i]))

def proc_try(event) :
    if len(ant_frame.get()) != 5 :
        print("Fehler! Länge der Antwort muss 5 sein!")
        return -1
    VersuchsObj = WordleGame.Answer(ant_frame.get())
    vergleich = Runde.eval_try(VersuchsObj)
    current_row = 6 - Runde.tries_left
    for i in range(0,5) :
        match vergleich[i]:
            case -1:
                VersuchsMuster[current_row].inhalt[i].configure(text=VersuchsObj.Versuch[i], background="grey")
            case 0:
                VersuchsMuster[current_row].inhalt[i].configure(text=VersuchsObj.Versuch[i], background="orange")
            case 1:
                VersuchsMuster[current_row].inhalt[i].configure(text=VersuchsObj.Versuch[i], background="green")
            case 2:
                VersuchsMuster[current_row].inhalt[i].configure(text=VersuchsObj.Versuch[i], background="green", foreground="orange")
        #VersuchsMuster[1].inhalt[i].configure(text=str(VersuchsObj.Versuch[i]))

    print(VersuchsObj)


class Versuchszeile(ttk.Frame):
    def __init__(self, parent, row):
        Frame.__init__(self, parent)
        self.row = row
        self.inhalt = [ttk.Label(self,text="_", background="grey") for index in range(0,5)]
        #self.inhalt = [ttk.Label(self,text="_").grid(column = index, row= self.row) for index in range(0,5)]
        for index in range(len(self.inhalt)) :
            self.inhalt[index].grid(column = index, row= self.row)
    
    def __str__(self):
        return str(self.inhalt)
        #return super().__str__()


root = Tk()
root.title("Bjarnes Wordle")
solution = ttk.Frame(root, padding=10)
solution.grid()
ttk.Label(solution, text="Lösung: ").grid(column=0,row=0)
lsg_frame = ttk.Entry(root)
lsg_frame.grid(row=0, column=1)
lsg_frame.bind("<Return>",get_lsg)
VersuchsMuster = []
for i in range(1,7):  #läuft von 1 bis 6
    var = Versuchszeile(root, row=i)
    var.grid()
    VersuchsMuster.append(var)

versuch = ttk.Frame(root, padding=10)
versuch.grid()
ttk.Label(versuch, text="Antwort: ").grid(column=0,row=7)
ant_frame = ttk.Entry(root)
ant_frame.grid(row=7, column=1)
ant_frame.bind("<Return>",proc_try)

root.mainloop()

