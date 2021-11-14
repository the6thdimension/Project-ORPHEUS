import pyaudio
import tkinter as tk
from tkinter import *
import numpy
import time
from synthesizer import Player, Synthesizer, Waveform


player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

def playC4():
    r=260.7
def playD4():
    r=293.3
def playE4():
    r=330
def playF4():
    r=347.7
def playG4():
    r=391.1
def playA4():
    r=440.0
def playB4():
    r=495
   
root = tk.Tk()
v =DoubleVar()  
b = tk.IntVar()
r=5
s=0
t=0
f=0

def Major():
    s=r*(5/4)
    t=r*(6/4)
    f=0
    print(r,s,t)
def Minor():
    s=r*(12/10)
    t=r*(15/10)
    f=0
    print(r,s,t)
def Diminished():
    s=r*(192/160)
    t=r*(231/160)
    f=0
    print(r,s,t)
def MinorSeventh():
    s=r*(12/10)
    t=r*(15/10)
    f=r*(18/10)
    print(r,s,t)
def MajorSeventh():
    s=r*(10/8)
    t=r*(12/8)
    f=r*(15/8)
    print(r,s,t)
def playsound():
    print(r)
    #chord = [r,  s, t, f]
    #player.play_wave(synthesizer.generate_chord(chord, 3.0))


noteselect = LabelFrame(root, text="Note Select")
noteselect.grid()

chordselect = Frame(root)
chordselect.grid()

playbar = Frame(root)
playbar.grid(row=3)



Radiobutton(noteselect, text="C", variable=b, value=1, command=playC4).grid(row=0, column=0)
Radiobutton(noteselect, text="D", variable=r, value=2, command=playD4).grid(row=0, column=1)
Radiobutton(noteselect, text="E", variable=r, value=3, command=playE4).grid(row=0, column=2)
Radiobutton(noteselect, text="F", variable=r, value=4, command=playF4).grid(row=0, column=3)
Radiobutton(noteselect, text="G", variable=r, value=5, command=playG4).grid(row=0, column=4)
Radiobutton(noteselect, text="A", variable=r, value=6, command=playA4).grid(row=0, column=5)
Radiobutton(noteselect, text="B", variable=r, value=7, command=playB4).grid(row=0, column=6)

b = Button(chordselect, text="Major",  command=Major).pack()
b= Button(chordselect, text="Minor",  command=Minor).pack()
b= Button(chordselect,text="Diminished",  command=Diminished).pack()
b= Button(chordselect, text="Major Seventh", command=MajorSeventh).pack()
b= Button(chordselect,text="Minor Seventh", command=MinorSeventh).pack()
b= Button(chordselect,text="Dominant Seventh",).pack()
b= Button(chordselect,text="Suspended",).pack()
b= Button(chordselect,text="Augmented",).pack()
b= Button(chordselect,text="Extended",).pack()

Button(playbar,text='Play!', command=playsound).pack()

root.mainloop()