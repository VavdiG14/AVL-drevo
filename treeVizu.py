import tkinter as tk
import math as m
import AVLDrevo as avl
import analizaAVL as analiza
import random
import time

def _create_circle(self, x, y, r, **kwargs):
    """Naredi krog"""
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

def naredi_levo_crto(x,y,r, a, **kwargs):
    """Izriše levo crto"""
    x1 = m.tan(a)*r
    return (canvas.create_line(x,y, x - x1, y+r), x-x1, y+r)

def naredi_desno_crto(x,y,r, a, **kwargs):
    """Izrise desno crto"""
    x1 = m.tan(a)*r
    return (canvas.create_line(x,y, x+x1, y+r), x+x1, y+r)


def naredi_drevo(drevo,x0,y0,r,phi):
    """Iz vozlisc zacnes"""
    if drevo.prazno():
        return
    canvas.create_text(x0,y0-20,text = str(drevo.koren.kljuc))
    canvas.create_circle(x0, y0, 5, fill="black")
    if drevo.koren.levi.prazno() and drevo.koren.desni.prazno():
        return
    if not drevo.koren.levi.prazno():
        l = naredi_levo_crto(x0,y0, r, phi)
        l[0]
        naredi_drevo(drevo.koren.levi, l[1], l[2], r-0.45, phi-0.2)
    if not drevo.koren.desni.prazno():
        d = naredi_desno_crto(x0,y0, r, phi)
        d[0]
        naredi_drevo(drevo.koren.desni, d[1], d[2], r-0.45, phi-0.2)
    return


def izrisi(d, x):
    x0 = SIRINA/2-250
    y0 = VISINA/100+20
    r = 150
    phi = 1
    d.vstavi(x)
    naredi_drevo(d,x0,y0,r,phi)
    return

def izrisi_brisanje(d,x):
    x0 = SIRINA/2-250
    y0 = VISINA/100+20
    r = 150
    phi = 1
    d.izbrisi(x)
    naredi_drevo(d,x0,y0,r,phi)
    return


root = tk.Tk()
SIRINA = 2000
VISINA = 1000
canvas = tk.Canvas(root, width=SIRINA, height=VISINA, borderwidth=0, highlightthickness=0, bg="white")
canvas.grid(row=0, column=1)
frame = tk.Frame(root)
frame.grid(row=0,column=0, sticky="n")
tk.Label(frame, text="Število vozlišc: ").grid(row=0,column=0, sticky="nw")
tk.Label(frame, text="Dolžina najdaljše poti do korena: ").grid(row=1, column=0, sticky="nw")
tk.Label(frame, text="Povprecna dolžina poti v drevesu: ").grid(row=2,column=0, sticky="nw")
tk.Label(frame, text="Povprecna globina: ").grid(row=3,column=0, sticky="nw")

tk.Canvas.create_circle = _create_circle

x0 = SIRINA/2 
y0 = (VISINA/100) 
r = 80
d = avl.AVLDrevo()
x = 0
sez = [4, 4, 4, 3,6,9, 1]

def risi_vstavljanje():
    global sez
    global x
    if  x == 5:
        #print(sez)
        return risi_brisanje()
    canvas.delete("all")
    tk.Label(frame,text= str(x)).grid(row=0,column=1, sticky="nw")
    #rand = random.randint(1,10)
    izrisi(d,sez[x])
    print(d.pravilno())
    maxGlobina = analiza.max_globina(d)
    tk.Label(frame,text= str(maxGlobina)).grid(row=1,column=1, sticky="nw")
    avg  = analiza.povprecna_globina(d)
    tk.Label(frame,text= str(avg)).grid(row=2,column=1, sticky="nw")
    avg_idelano = analiza.opt_povprecna_globina(x)
    tk.Label(frame,text="").grid(row=0,column=2, sticky="nw")
    tk.Label(frame,text= str(avg_idelano)).grid(row=3,column=1, sticky="nw")
    x += 1
    root.after(1500,risi_vstavljanje)

sez1 = [4, 4, 4, 3, 6, 9, 1]
x1 = 0

def risi_brisanje():
    global sez1
    global x1
    if  len(sez1) == 0:
        root.quit()
        return
    canvas.delete("all")
    tk.Label(frame,text= str(len(sez))).grid(row=0,column=1, sticky="nw")
    v = random.choice(sez)
    izrisi_brisanje(d,sez[x1])
    x1 +=1
    maxGlobina = analiza.max_globina(d)
    tk.Label(frame,text= str(maxGlobina)).grid(row=1,column=1, sticky="nw")
    avg  = analiza.povprecna_globina(d)
    tk.Label(frame,text= str(avg)).grid(row=2,column=1, sticky="nw")
    avg_idelano = analiza.opt_povprecna_globina(len(sez))
    tk.Label(frame,text="").grid(row=0,column=2, sticky="nw")
    tk.Label(frame,text= str(avg_idelano)).grid(row=3,column=1, sticky="nw")
    root.after(1000,risi_brisanje)

#tk.Button(frame, text = "Izbrisi", command = risi_brisanje()).grid(row = 4,column=2, sticky="nw")
risi_vstavljanje()

root.wm_title("Circles and Arcs")
root.mainloop()


