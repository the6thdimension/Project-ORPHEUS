import pyaudio
from tkinter import *
import numpy
import time
from synthesizer import Player, Synthesizer, Waveform


def playC4():
    player.play_wave(synthesizer.generate_constant_wave(260.7, 3.0))
def playD4():
    player.play_wave(synthesizer.generate_constant_wave(293.3, 3.0))
def playE4():
    player.play_wave(synthesizer.generate_constant_wave(330, 3.0))
def playF4():
    player.play_wave(synthesizer.generate_constant_wave(347.7, 3.0))
def playG4():
    player.play_wave(synthesizer.generate_constant_wave(391.1, 3.0))
def playA4():
    player.play_wave(synthesizer.generate_constant_wave(440.0, 3.0))
def playB4():
    player.play_wave(synthesizer.generate_constant_wave(495, 3.0))
def playC5():
    player.play_wave(synthesizer.generate_constant_wave(521.5, 3.0))
def playD5():
    player.play_wave(synthesizer.generate_constant_wave(586.7, 3.0))
def playE5():
    player.play_wave(synthesizer.generate_constant_wave(660, 3.0))
def playF5():
    player.play_wave(synthesizer.generate_constant_wave(695.3, 3.0))
def playG5():
    player.play_wave(synthesizer.generate_constant_wave(782.2, 3.0))
def playA5():
    player.play_wave(synthesizer.generate_constant_wave(880, 3.0))
def playB5():
    player.play_wave(synthesizer.generate_constant_wave(990, 3.0))
def playC6():
    player.play_wave(synthesizer.generate_constant_wave(1043, 3.0))


player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

root = Tk()
frame = Frame(root)
frame.pack()


bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

C4 = Button(frame, text="C4", fg="red",command=playC4)
C4.pack(side = LEFT)
D4 = Button(frame, text="D4", fg="orange",command=playD4)
D4.pack(side = LEFT)
E4 = Button(frame, text="E4", fg="gold",command=playE4)
E4.pack(side = LEFT)
F4 = Button(frame, text="F4", fg="green",command=playF4)
F4.pack(side = LEFT)
G4 = Button(frame, text="G4", fg="cyan",command=playG4)
G4.pack(side = LEFT)
A4 = Button(frame, text="A4", fg="sky blue",command=playA4)
A4.pack(side = LEFT)
B4 = Button(frame, text="B4", fg="blue",command=playB4)
B4.pack(side = LEFT)

C5 = Button(bottomframe, text="C5", fg="red",command=playC5)
C5.pack(side = LEFT)
D5 = Button(bottomframe, text="D5", fg="orange",command=playD5)
D5.pack(side = LEFT)
E5 = Button(bottomframe, text="E5", fg="gold",command=playE5)
E5.pack(side = LEFT)
F5 = Button(bottomframe, text="F5", fg="green",command=playF5)
F5.pack(side = LEFT)
G5 = Button(bottomframe, text="G5", fg="cyan",command=playG5)
G5.pack(side = LEFT)
A5 = Button(bottomframe, text="A5", fg="sky blue",command=playA5)
A5.pack(side = LEFT)
B5 = Button(bottomframe, text="B5", fg="blue",command=playB5)
B5.pack(side = LEFT)

root.mainloop()