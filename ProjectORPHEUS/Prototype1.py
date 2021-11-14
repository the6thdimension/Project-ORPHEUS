import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import pyaudio
import numpy
import time
from synthesizer import Player, Synthesizer, Waveform
from PIL import Image, ImageTk
import os
import sys
import tkmacosx


# create a class for music player
class MusicPlayer:

    # create a definition for note names and frequencies

    def __init__(self, musicbox):
        self.musicbox = musicbox
        self.player = Player()
        self.synthesizer = Synthesizer()
        self.waveform = Waveform()
        self.player.set_waveform(self.waveform)
        self.player.set_synthesizer(self.synthesizer)
        self.player.set_samplerate(41000)
        self.player.set_channels(2)
        self.player.set_bitdepth(16)
        self.player.set_buffersize(1024)
        self.player.set_volume(1.0)
        self.player.set_loop(False)
        self.player.set_looping_end(0)
        self.player.set_looping_start(0)
        self.player.set_position(0)
        self.player.set_playback(False)
        self.player.set_waveform(self.waveform)
        self.player.set_synthesizer(self.synthesizer)
        self.player.set_samplerate(41000)
        self.player.set_channels(2)
        self.player.set_bitdepth(16)
        self.player.set_buffersize(1024)
        self.player.set_volume(1.0)
        self.player.set_loop(False)
        self.player.set_looping_end(0)
        self.player.set_looping_start(0)
        self.player.set_position(0)
        self.player.set_playback(False)
        self.player.set_waveform(self.waveform)
        self.player.set_synthesizer(self.synthesizer)
        self.player.set_samplerate(41000)


# create a class to build and run the GUI
class Prototype1:

    note_frequencies = {
        'C': 16.35,
        'C#': 17.32,
        'D': 18.35,
        'D#': 19.45,
        'E': 20.60,
        'F': 21.83,
        'F#': 23.12,
        'G': 24.50,
        'G#': 25.96,
        'A': 27.50,
        'A#': 29.4,
        'B': 30.87
    }

    # create a function to play music when button is clicked and use note_frequencies to find the frequency of the note. Also multiply the frequency by the current_octave number.
    def play_sound(self, note, current_octave):
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine,
                                  osc1_volume=1.0, use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(
            (self.note_frequencies[note] * (2**current_octave)), 1.0))
        freq = self.note_frequencies[note] * (2**current_octave)
        print(note + ' was played at ' + str(freq) + ' Hz')

    # create a change current_octave function
    global default_octave
    default_octave = 4
    global current_octave
    current_octave = default_octave
    global octave_number

    def change_current_octave(self, change):
        global current_octave
        current_octave = current_octave + change
        print(current_octave)

    # create a function to play major chords

    def play_major_chord(self, note, current_octave):
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine,
                                  osc1_volume=1.0, use_osc2=False)
        r = self.note_frequencies[note] * (2**current_octave)
        s = r*(5/4)
        t = r*(6/4)
        f = 0
        chord = [r,  s, t, f]
        player.play_wave(synthesizer.generate_chord(chord, 2.0))
        print(note+' Maj chord' + ' was played at ' +
              str(r)+','+str(s)+','+str(t) + ' Hz')

    # create a function to play minor chords
    def play_minor_chord(self, note, current_octave):
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine,
                                  osc1_volume=1.0, use_osc2=False)
        r = self.note_frequencies[note] * (2**current_octave)
        s = r*(12/10)
        t = r*(15/10)
        f = 0
        chord = [r,  s, t, f]
        player.play_wave(synthesizer.generate_chord(chord, 2.0))
        print(note+' Min chord' + ' was played at ' +
              str(r)+','+str(s)+','+str(t) + ' Hz')

    # create a function to play a scale
    def play_diminished_chord(self, note, current_octave):
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine,
                                  osc1_volume=1.0, use_osc2=False)
        r = self.note_frequencies[note] * (2**current_octave)
        s = r*(192/160)
        t = r*(231/160)
        f = 0
        chord = [r,  s, t, f]
        player.play_wave(synthesizer.generate_chord(chord, 2.0))
        print(note+' Dim chord' + ' was played at ' +
              str(r)+','+str(s)+','+str(t) + ' Hz')

    def play_major_7th_chord(self, note, current_octave):
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine,
                                  osc1_volume=1.0, use_osc2=False)
        r = self.note_frequencies[note] * (2**current_octave)
        s = r*(10/8)
        t = r*(12/8)
        f = r*(15/8)
        chord = [r,  s, t, f]
        player.play_wave(synthesizer.generate_chord(chord, 2.0))
        print(note+' Maj7 chord' + ' was played at ' +
              str(r)+','+str(s)+','+str(t) + ' Hz')

    def play_minor_7th_chord(self, note, current_octave):
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine,
                                  osc1_volume=1.0, use_osc2=False)
        r = self.note_frequencies[note] * (2**current_octave)
        s = r*(12/10)
        t = r*(15/10)
        f = r*(18/10)
        chord = [r,  s, t, f]
        player.play_wave(synthesizer.generate_chord(chord, 2.0))
        print(note+' Min7 chord' + ' was played at ' +
              str(r)+','+str(s)+','+str(t) + ' Hz')

    def play_dominant_7th_chord(self, note, current_octave):
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine,
                                  osc1_volume=1.0, use_osc2=False)
        r = self.note_frequencies[note] * (2**current_octave)
        s = r*(5/4)
        t = r*(6/4)
        f = r*(9/8)
        chord = [r,  s, t, f]
        player.play_wave(synthesizer.generate_chord(chord, 2.0))
        print(note+' Dom7 chord' + ' was played at ' +
              str(r)+','+str(s)+','+str(t) + ' Hz')

    def play_suspended_2nd_chord(self, note, current_octave):
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine,
                                  osc1_volume=1.0, use_osc2=False)
        r = self.note_frequencies[note] * (2**current_octave)
        s = r*(1/1)
        t = r*(1/1)
        f = 0
        chord = [r,  s, t, f]
        player.play_wave(synthesizer.generate_chord(chord, 2.0))
        print(note+' Sus2 chord' + ' was played at ' +
              str(r)+','+str(s)+','+str(t) + ' Hz')

    def play_suspended_4th_chord(self, note, current_octave):
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine,
                                  osc1_volume=1.0, use_osc2=False)
        r = self.note_frequencies[note] * (2**current_octave)
        s = r*(5/4)
        t = r*(7/4)
        f = 0
        chord = [r,  s, t, f]
        player.play_wave(synthesizer.generate_chord(chord, 2.0))
        print(note+' Sus4 chord' + ' was played at ' +
              str(r)+','+str(s)+','+str(t) + ' Hz')

    def play_aug_chord(self, note, current_octave):
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine,
                                  osc1_volume=1.0, use_osc2=False)
        r = self.note_frequencies[note] * (2**current_octave)
        s = r*(4/3)
        t = r*(5/3)
        f = 0
        chord = [r,  s, t, f]
        player.play_wave(synthesizer.generate_chord(chord, 2.0))
        print(note+' Aug chord' + ' was played at ' +
              str(r)+','+str(s)+','+str(t) + ' Hz')

    def play_maj9_chord(self, note, current_octave):
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine,
                                  osc1_volume=1.0, use_osc2=False)
        r = self.note_frequencies[note] * (2**current_octave)
        s = r*(5/4)
        t = r*(6/4)
        f = r*(9/8)
        chord = [r,  s, t, f]
        player.play_wave(synthesizer.generate_chord(chord, 2.0))
        print(note+' Maj9 chord' + ' was played at ' +
              str(r)+','+str(s)+','+str(t) + ' Hz')

    # create a function to play a

    def __init__(self, master):

        self.master = master
        self.master.title("ProjectORPHEUS")
        self.master.geometry("1000x800")
        self.master.resizable(0, 0)
        self.master.configure(background='#FFFFFF')

        # create a menu bar
        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)
        # create a pulldown menu, and add it to the menu bar
        # tearoff=0 means no tearoff menu
        self.file_menu = Menu(self.menu_bar, tearoff=0)

        # add the menu to the menu bar
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # create a information frame
        self.info_frame = tk.LabelFrame(self.master, text="Information")
        self.info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        # describe the application
        self.info_label = ttk.Label(self.info_frame, text="ProjectORPHEUS is a prototype of a synthesizer that can be used to create a soundscape.\n\n"
                                    "The synthesizer is capable of playing a variety of sounds, and can be used to create a soundscape.\n\n"
                                    "The soundscape can be saved to a .wav file, and can be played back.\n\n")
        self.info_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.current_octave_label = tk.Label(
            self.master, text="current_octave")
        self.current_octave_label.grid(row=0, column=1, padx=10,
                                       pady=10, sticky="nsew")
        # add a label showing the current_octave number
        self.current_octave_button_minus = tk.Button(
            self.master, text="-", command=lambda: self.change_current_octave(-1))
        self.current_octave_button_minus.grid(
            row=0, column=2, padx=10, pady=10, sticky="nsew")
        self.current_octave_button_plus = tk.Button(
            self.master, text="+", command=lambda: self.change_current_octave(1))
        self.current_octave_button_plus.grid(
            row=0, column=3, padx=10, pady=10, sticky="nsew")
        self.current_octave_number = tk.Label(
            self.master, textvariable=current_octave)
        self.current_octave_number.grid(row=0, column=4, padx=10,)


# =======================================================================================================================
# =======================================================================================================================
# ===========ROOT NOTES================================================================================================
# =======================================================================================================================
# =======================================================================================================================

        self.rootnotes = tk.Frame(self.master)
        self.rootnotes.grid(row=1)
        # create a label for the root notes
        self.rootnotes_label = tk.Label(
            self.rootnotes, text="Root Notes", font=("Helvetica", 16))
        self.rootnotes_label.grid(row=0, column=0)
        # create buttons for the root notes
        self.rootnotes_C = tk.Button(
            self.rootnotes, text="C", command=lambda: self.play_sound('C', current_octave))
        self.rootnotes_C.grid(row=1, column=1)
        self.rootnotes_Csharp = tk.Button(
            self.rootnotes, text="C#", highlightbackground='black', fg='black', command=lambda: self.play_sound('C#', current_octave))
        self.rootnotes_Csharp.grid(row=1, column=2)
        self.rootnotes_D = tk.Button(
            self.rootnotes, text="D", command=lambda: self.play_sound('D', current_octave))
        self.rootnotes_D.grid(row=1, column=3)
        self.rootnotes_Dsharp = tk.Button(
            self.rootnotes, text="D#", highlightbackground='black', fg='black', command=lambda: self.play_sound('D#', current_octave))
        self.rootnotes_Dsharp.grid(row=1, column=4)
        self.rootnotes_E = tk.Button(
            self.rootnotes, text="E", command=lambda: self.play_sound('E', current_octave))
        self.rootnotes_E.grid(row=1, column=5)
        self.rootnotes_F = tk.Button(
            self.rootnotes, text="F", command=lambda: self.play_sound('F', current_octave))
        self.rootnotes_F.grid(row=1, column=6)
        self.rootnotes_Fsharp = tk.Button(
            self.rootnotes, text="F#", highlightbackground='black', command=lambda: self.play_sound('F#', current_octave))
        self.rootnotes_Fsharp.grid(row=1, column=7)
        self.rootnotes_G = tk.Button(
            self.rootnotes, text="G", command=lambda: self.play_sound('G', current_octave))
        self.rootnotes_G.grid(row=1, column=8)
        self.rootnotes_Gsharp = tk.Button(
            self.rootnotes, text="G#", highlightbackground='black', command=lambda: self.play_sound('G#', current_octave))
        self.rootnotes_Gsharp.grid(row=1, column=9)
        self.rootnotes_A = tk.Button(
            self.rootnotes, text="A", command=lambda: self.play_sound('A', current_octave))
        self.rootnotes_A.grid(row=1, column=10)
        self.rootnotes_Asharp = tk.Button(
            self.rootnotes, text="A#", highlightbackground='black', command=lambda: self.play_sound('A#', current_octave))
        self.rootnotes_Asharp.grid(row=1, column=11)
        self.rootnotes_B = tk.Button(
            self.rootnotes, text="B", command=lambda: self.play_sound('B', current_octave))
        self.rootnotes_B.grid(row=1, column=12)

# =======================================================================================================================
# =======================================================================================================================
# ===========MAJOR CHORDS===============================================================================================
# =======================================================================================================================
# =======================================================================================================================

        self.maj = tk.Frame(self.master)
        self.maj.grid(row=2)
        # create a label for the major chords
        self.maj_label = tk.Label(
            self.maj, text="Major Chords", font=("Helvetica", 16))
        self.maj_label.grid(row=0, column=0)

        # create buttons for the major chords
        self.maj_C = tk.Button(
            self.maj, text="C", command=lambda: self.play_major_chord('C', current_octave))
        self.maj_C.grid(row=1, column=1)
        self.maj_Csharp = tk.Button(
            self.maj, text="C#", highlightbackground='black', command=lambda: self.play_major_chord('C#', current_octave))
        self.maj_Csharp.grid(row=1, column=2)
        self.maj_D = tk.Button(
            self.maj, text="D", command=lambda: self.play_major_chord('D', current_octave))
        self.maj_D.grid(row=1, column=3)
        self.maj_Dsharp = tk.Button(
            self.maj, text="D#", highlightbackground='black', fg='black', command=lambda: self.play_major_chord('D#', current_octave))
        self.maj_Dsharp.grid(row=1, column=4)
        self.maj_E = tk.Button(
            self.maj, text="E", command=lambda: self.play_major_chord('E', current_octave))
        self.maj_E.grid(row=1, column=5)
        self.maj_F = tk.Button(
            self.maj, text="F", command=lambda: self.play_major_chord('F', current_octave))
        self.maj_F.grid(row=1, column=6)
        self.maj_Fsharp = tk.Button(
            self.maj, text="F#", highlightbackground='black', command=lambda: self.play_major_chord('F#', current_octave))
        self.maj_Fsharp.grid(row=1, column=7)
        self.maj_G = tk.Button(
            self.maj, text="G", command=lambda: self.play_major_chord('G', current_octave))
        self.maj_G.grid(row=1, column=8)
        self.maj_Gsharp = tk.Button(
            self.maj, text="G#", highlightbackground='black', command=lambda: self.play_major_chord('G#', current_octave))
        self.maj_Gsharp.grid(row=1, column=9)
        self.maj_A = tk.Button(
            self.maj, text="A", command=lambda: self.play_major_chord('A', current_octave))
        self.maj_A.grid(row=1, column=10)
        self.maj_Asharp = tk.Button(
            self.maj, text="A#", highlightbackground='black', command=lambda: self.play_major_chord('A#', current_octave))
        self.maj_Asharp.grid(row=1, column=11)
        self.maj_B = tk.Button(
            self.maj, text="B", command=lambda: self.play_major_chord('B', current_octave))
        self.maj_B.grid(row=1, column=12)

# =======================================================================================================================
# =======================================================================================================================
# ===========MINOR CHORDS===============================================================================================
# =======================================================================================================================
# =======================================================================================================================

        self.min = tk.Frame(self.master)
        self.min.grid(row=3)
        # create a label for the minor chords
        self.min_label = tk.Label(
            self.min, text="Minor Chords", font=("Helvetica", 16))
        self.min_label.grid(row=0, column=0)
        # create buttons for the minor chords
        self.min_C = tk.Button(
            self.min, text="C", command=lambda: self.play_minor_chord('C', current_octave))
        self.min_C.grid(row=1, column=1)
        self.min_Csharp = tk.Button(
            self.min, text="C#", highlightbackground='black', command=lambda: self.play_minor_chord('C#', current_octave))
        self.min_Csharp.grid(row=1, column=2)
        self.min_D = tk.Button(
            self.min, text="D", command=lambda: self.play_minor_chord('D', current_octave))
        self.min_D.grid(row=1, column=3)
        self.min_Dsharp = tk.Button(
            self.min, text="D#", highlightbackground='black', fg='black', command=lambda: self.play_minor_chord('D#', current_octave))
        self.min_Dsharp.grid(row=1, column=4)
        self.min_E = tk.Button(
            self.min, text="E", command=lambda: self.play_minor_chord('E', current_octave))
        self.min_E.grid(row=1, column=5)
        self.min_F = tk.Button(
            self.min, text="F", command=lambda: self.play_minor_chord('F', current_octave))
        self.min_F.grid(row=1, column=6)
        self.min_Fsharp = tk.Button(
            self.min, text="F#", highlightbackground='black', command=lambda: self.play_minor_chord('F#', current_octave))
        self.min_Fsharp.grid(row=1, column=7)
        self.min_G = tk.Button(
            self.min, text="G", command=lambda: self.play_minor_chord('G', current_octave))
        self.min_G.grid(row=1, column=8)
        self.min_Gsharp = tk.Button(
            self.min, text="G#", highlightbackground='black', command=lambda: self.play_minor_chord('G#', current_octave))
        self.min_Gsharp.grid(row=1, column=9)
        self.min_A = tk.Button(
            self.min, text="A", command=lambda: self.play_minor_chord('A', current_octave))
        self.min_A.grid(row=1, column=10)
        self.min_Asharp = tk.Button(
            self.min, text="A#", highlightbackground='black', command=lambda: self.play_minor_chord('A#', current_octave))
        self.min_Asharp.grid(row=1, column=11)
        self.min_B = tk.Button(
            self.min, text="B", command=lambda: self.play_minor_chord('B', current_octave))
        self.min_B.grid(row=1, column=12)

# =======================================================================================================================
# =======================================================================================================================
# ===========HARMONIC MINOR CHORDS=======================================================================================
# =======================================================================================================================
# =======================================================================================================================


# =======================================================================================================================
# =======================================================================================================================
# ===========DIMINISHED CHORDS=======================================================================================
# =======================================================================================================================
# =======================================================================================================================

        self.dim = tk.Frame(self.master)
        self.dim.grid(row=4)
        # create a label for the diminished chords
        self.dim_label = tk.Label(
            self.dim, text="Diminished Chords", font=("Helvetica", 16))
        self.dim_label.grid(row=0, column=0)
        # create buttons for the diminished chords
        self.dim_C = tk.Button(
            self.dim, text="C", command=lambda: self.play_diminished_chord('C', current_octave))
        self.dim_C.grid(row=1, column=1)
        self.dim_Csharp = tk.Button(
            self.dim, text="C#", highlightbackground='black', command=lambda: self.play_diminished_chord('C#', current_octave))
        self.dim_Csharp.grid(row=1, column=2)
        self.dim_D = tk.Button(
            self.dim, text="D", command=lambda: self.play_diminished_chord('D', current_octave))
        self.dim_D.grid(row=1, column=3)
        self.dim_Dsharp = tk.Button(
            self.dim, text="D#", highlightbackground='black', fg='black', command=lambda: self.play_diminished_chord('D#', current_octave))
        self.dim_Dsharp.grid(row=1, column=4)
        self.dim_E = tk.Button(
            self.dim, text="E", command=lambda: self.play_diminished_chord('E', current_octave))
        self.dim_E.grid(row=1, column=5)
        self.dim_F = tk.Button(
            self.dim, text="F", command=lambda: self.play_diminished_chord('F', current_octave))
        self.dim_F.grid(row=1, column=6)
        self.dim_Fsharp = tk.Button(
            self.dim, text="F#", highlightbackground='black', command=lambda: self.play_diminished_chord('F#', current_octave))
        self.dim_Fsharp.grid(row=1, column=7)
        self.dim_G = tk.Button(
            self.dim, text="G", command=lambda: self.play_diminished_chord('G', current_octave))
        self.dim_G.grid(row=1, column=8)
        self.dim_Gsharp = tk.Button(
            self.dim, text="G#", highlightbackground='black', command=lambda: self.play_diminished_chord('G#', current_octave))
        self.dim_Gsharp.grid(row=1, column=9)
        self.dim_A = tk.Button(
            self.dim, text="A", command=lambda: self.play_diminished_chord('A', current_octave))
        self.dim_A.grid(row=1, column=10)
        self.dim_Asharp = tk.Button(
            self.dim, text="A#", highlightbackground='black', command=lambda: self.play_diminished_chord('A#', current_octave))
        self.dim_Asharp.grid(row=1, column=11)
        self.dim_B = tk.Button(
            self.dim, text="B", command=lambda: self.play_diminished_chord('B', current_octave))
        self.dim_B.grid(row=1, column=12)


# =======================================================================================================================
# =======================================================================================================================
# ===========MAJOR 7TH CHORDS===========================================================================================
# =======================================================================================================================
# =======================================================================================================================

        self.maj7 = tk.Frame(self.master)
        self.maj7.grid(row=5)
        # create a label for the major 7th chords
        self.maj7_label = tk.Label(
            self.maj7, text="Major 7th Chords", font=("Helvetica", 16))
        self.maj7_label.grid(row=0, column=0)
        # create buttons for the major 7th chords
        self.maj7_C = tk.Button(
            self.maj7, text="C", command=lambda: self.play_major_7th_chord('C', current_octave))
        self.maj7_C.grid(row=1, column=1)
        self.maj7_Csharp = tk.Button(
            self.maj7, text="C#", highlightbackground='black', command=lambda: self.play_major_7th_chord('C#', current_octave))
        self.maj7_Csharp.grid(row=1, column=2)
        self.maj7_D = tk.Button(
            self.maj7, text="D", command=lambda: self.play_major_7th_chord('D', current_octave))
        self.maj7_D.grid(row=1, column=3)
        self.maj7_Dsharp = tk.Button(
            self.maj7, text="D#", highlightbackground='black', fg='black', command=lambda: self.play_major_7th_chord('D#', current_octave))
        self.maj7_Dsharp.grid(row=1, column=4)
        self.maj7_E = tk.Button(
            self.maj7, text="E", command=lambda: self.play_major_7th_chord('E', current_octave))
        self.maj7_E.grid(row=1, column=5)
        self.maj7_F = tk.Button(
            self.maj7, text="F", command=lambda: self.play_major_7th_chord('F', current_octave))
        self.maj7_F.grid(row=1, column=6)
        self.maj7_Fsharp = tk.Button(
            self.maj7, text="F#", highlightbackground='black', command=lambda: self.play_major_7th_chord('F#', current_octave))
        self.maj7_Fsharp.grid(row=1, column=7)
        self.maj7_G = tk.Button(
            self.maj7, text="G", command=lambda: self.play_major_7th_chord('G', current_octave))
        self.maj7_G.grid(row=1, column=8)
        self.maj7_Gsharp = tk.Button(
            self.maj7, text="G#", highlightbackground='black', command=lambda: self.play_major_7th_chord('G#', current_octave))
        self.maj7_Gsharp.grid(row=1, column=9)
        self.maj7_A = tk.Button(
            self.maj7, text="A", command=lambda: self.play_major_7th_chord('A', current_octave))
        self.maj7_A.grid(row=1, column=10)
        self.maj7_Asharp = tk.Button(
            self.maj7, text="A#", highlightbackground='black', command=lambda: self.play_major_7th_chord('A#', current_octave))
        self.maj7_Asharp.grid(row=1, column=11)
        self.maj7_B = tk.Button(
            self.maj7, text="B", command=lambda: self.play_major_7th_chord('B', current_octave))
        self.maj7_B.grid(row=1, column=12)


# =======================================================================================================================
# =======================================================================================================================
# ===========MINOR 7TH CHORDS===========================================================================================
# =======================================================================================================================
# =======================================================================================================================

        self.min7 = tk.Frame(self.master)
        self.min7.grid(row=6)
        # create a label for the minor 7th chords
        self.min7_label = tk.Label(
            self.min7, text="Minor 7th Chords", font=("Helvetica", 16))
        self.min7_label.grid(row=0, column=0)
        # create buttons for the minor 7th chords
        self.min7_C = tk.Button(
            self.min7, text="C", command=lambda: self.play_minor_7th_chord('C', current_octave))
        self.min7_C.grid(row=1, column=1)
        self.min7_Csharp = tk.Button(
            self.min7, text="C#", highlightbackground='black', command=lambda: self.play_minor_7th_chord('C#', current_octave))
        self.min7_Csharp.grid(row=1, column=2)
        self.min7_D = tk.Button(
            self.min7, text="D", command=lambda: self.play_minor_7th_chord('D', current_octave))
        self.min7_D.grid(row=1, column=3)
        self.min7_Dsharp = tk.Button(
            self.min7, text="D#", highlightbackground='black', fg='black', command=lambda: self.play_minor_7th_chord('D#', current_octave))
        self.min7_Dsharp.grid(row=1, column=4)
        self.min7_E = tk.Button(
            self.min7, text="E", command=lambda: self.play_minor_7th_chord('E', current_octave))
        self.min7_E.grid(row=1, column=5)
        self.min7_F = tk.Button(
            self.min7, text="F", command=lambda: self.play_minor_7th_chord('F', current_octave))
        self.min7_F.grid(row=1, column=6)
        self.min7_Fsharp = tk.Button(
            self.min7, text="F#", highlightbackground='black', command=lambda: self.play_minor_7th_chord('F#', current_octave))
        self.min7_Fsharp.grid(row=1, column=7)
        self.min7_G = tk.Button(
            self.min7, text="G", command=lambda: self.play_minor_7th_chord('G', current_octave))
        self.min7_G.grid(row=1, column=8)
        self.min7_Gsharp = tk.Button(
            self.min7, text="G#", highlightbackground='black', command=lambda: self.play_minor_7th_chord('G#', current_octave))
        self.min7_Gsharp.grid(row=1, column=9)
        self.min7_A = tk.Button(
            self.min7, text="A", command=lambda: self.play_minor_7th_chord('A', current_octave))
        self.min7_A.grid(row=1, column=10)
        self.min7_Asharp = tk.Button(
            self.min7, text="A#", highlightbackground='black', command=lambda: self.play_minor_7th_chord('A#', current_octave))
        self.min7_Asharp.grid(row=1, column=11)
        self.min7_B = tk.Button(
            self.min7, text="B", command=lambda: self.play_minor_7th_chord('B', current_octave))
        self.min7_B.grid(row=1, column=12)


# =======================================================================================================================
# =======================================================================================================================
# ===========DOMINANT 7TH CHORDS========================================================================================
# =======================================================================================================================
# =======================================================================================================================

        self.dom7 = tk.Frame(self.master)
        self.dom7.grid(row=7)
        # create a label for the dominant 7th chords
        self.dom7_label = tk.Label(
            self.dom7, text="Dominant 7th Chords", font=("Helvetica", 16))
        self.dom7_label.grid(row=0, column=0)
        # create buttons for the dominant 7th chords
        self.dom7_C = tk.Button(
            self.dom7, text="C", command=lambda: self.play_dominant_7th_chord('C', current_octave))
        self.dom7_C.grid(row=1, column=1)
        self.dom7_Csharp = tk.Button(
            self.dom7, text="C#", highlightbackground='black', command=lambda: self.play_dominant_7th_chord('C#', current_octave))
        self.dom7_Csharp.grid(row=1, column=2)
        self.dom7_D = tk.Button(
            self.dom7, text="D", command=lambda: self.play_dominant_7th_chord('D', current_octave))
        self.dom7_D.grid(row=1, column=3)
        self.dom7_Dsharp = tk.Button(
            self.dom7, text="D#", highlightbackground='black', fg='black', command=lambda: self.play_dominant_7th_chord('D#', current_octave))
        self.dom7_Dsharp.grid(row=1, column=4)
        self.dom7_E = tk.Button(
            self.dom7, text="E", command=lambda: self.play_dominant_7th_chord('E', current_octave))
        self.dom7_E.grid(row=1, column=5)
        self.dom7_F = tk.Button(
            self.dom7, text="F", command=lambda: self.play_dominant_7th_chord('F', current_octave))
        self.dom7_F.grid(row=1, column=6)
        self.dom7_Fsharp = tk.Button(
            self.dom7, text="F#", highlightbackground='black', command=lambda: self.play_dominant_7th_chord('F#', current_octave))
        self.dom7_Fsharp.grid(row=1, column=7)
        self.dom7_G = tk.Button(
            self.dom7, text="G", command=lambda: self.play_dominant_7th_chord('G', current_octave))
        self.dom7_G.grid(row=1, column=8)
        self.dom7_Gsharp = tk.Button(
            self.dom7, text="G#", highlightbackground='black', command=lambda: self.play_dominant_7th_chord('G#', current_octave))
        self.dom7_Gsharp.grid(row=1, column=9)
        self.dom7_A = tk.Button(
            self.dom7, text="A", command=lambda: self.play_dominant_7th_chord('A', current_octave))
        self.dom7_A.grid(row=1, column=10)
        self.dom7_Asharp = tk.Button(
            self.dom7, text="A#", highlightbackground='black', command=lambda: self.play_dominant_7th_chord('A#', current_octave))
        self.dom7_Asharp.grid(row=1, column=11)
        self.dom7_B = tk.Button(
            self.dom7, text="B", command=lambda: self.play_dominant_7th_chord('B', current_octave))
        self.dom7_B.grid(row=1, column=12)


# =======================================================================================================================
# =======================================================================================================================
# ===========SUSPENDED CHORDS===========================================================================================
# =======================================================================================================================
# =======================================================================================================================

        self.sus2 = tk.Frame(self.master)
        self.sus2.grid(row=8)
        # create a label for the suspended 2nd chords
        self.sus2_label = tk.Label(
            self.sus2, text="Suspended 2nd Chords", font=("Helvetica", 16))
        self.sus2_label.grid(row=0, column=0)
        # create buttons for the suspended 2nd chords
        self.sus2_C = tk.Button(
            self.sus2, text="C", command=lambda: self.play_suspended_2nd_chord('C', current_octave))
        self.sus2_C.grid(row=1, column=1)
        self.sus2_Csharp = tk.Button(
            self.sus2, text="C#", highlightbackground='black', command=lambda: self.play_suspended_2nd_chord('C#', current_octave))
        self.sus2_Csharp.grid(row=1, column=2)
        self.sus2_D = tk.Button(
            self.sus2, text="D", command=lambda: self.play_suspended_2nd_chord('D', current_octave))
        self.sus2_D.grid(row=1, column=3)
        self.sus2_Dsharp = tk.Button(
            self.sus2, text="D#", highlightbackground='black', command=lambda: self.play_suspended_2nd_chord('D#', current_octave))
        self.sus2_Dsharp.grid(row=1, column=4)
        self.sus2_E = tk.Button(
            self.sus2, text="E", command=lambda: self.play_suspended_2nd_chord('E', current_octave))
        self.sus2_E.grid(row=1, column=5)
        self.sus2_F = tk.Button(
            self.sus2, text="F", command=lambda: self.play_suspended_2nd_chord('F', current_octave))
        self.sus2_F.grid(row=1, column=6)
        self.sus2_Fsharp = tk.Button(
            self.sus2, text="F#", highlightbackground='black', command=lambda: self.play_suspended_2nd_chord('F#', current_octave))
        self.sus2_Fsharp.grid(row=1, column=7)
        self.sus2_G = tk.Button(
            self.sus2, text="G", command=lambda: self.play_suspended_2nd_chord('G', current_octave))
        self.sus2_G.grid(row=1, column=8)
        self.sus2_Gsharp = tk.Button(
            self.sus2, text="G#", highlightbackground='black', command=lambda: self.play_suspended_2nd_chord('G#', current_octave))
        self.sus2_Gsharp.grid(row=1, column=9)
        self.sus2_A = tk.Button(
            self.sus2, text="A", command=lambda: self.play_suspended_2nd_chord('A', current_octave))
        self.sus2_A.grid(row=1, column=10)
        self.sus2_Asharp = tk.Button(
            self.sus2, text="A#", highlightbackground='black', command=lambda: self.play_suspended_2nd_chord('A#', current_octave))
        self.sus2_Asharp.grid(row=1, column=11)
        self.sus2_B = tk.Button(
            self.sus2, text="B", command=lambda: self.play_suspended_2nd_chord('B', current_octave))
        self.sus2_B.grid(row=1, column=12)


# =======================================================================================================================
# =======================================================================================================================
# ===========SUSPENDED 4TH CHORDS========================================================================================
# =======================================================================================================================
# =======================================================================================================================

        self.sus4 = tk.Frame(self.master)
        self.sus4.grid(row=9)
        # create a label for the suspended current_octaveth chords
        self.sus4_label = tk.Label(
            self.sus4, text="Suspended 4th Chords", font=("Helvetica", 16))
        self.sus4_label.grid(row=0, column=0)
        # create buttons for the suspended 4th chords
        self.sus4_C = tk.Button(
            self.sus4, text="C", command=lambda: self.play_suspended_4th_chord('C', current_octave))
        self.sus4_C.grid(row=1, column=1)
        self.sus4_Csharp = tk.Button(
            self.sus4, text="C#", highlightbackground='black', command=lambda: self.play_suspended_4th_chord('C#', current_octave))
        self.sus4_Csharp.grid(row=1, column=2)
        self.sus4_D = tk.Button(
            self.sus4, text="D", command=lambda: self.play_suspended_4th_chord('D', current_octave))
        self.sus4_D.grid(row=1, column=3)
        self.sus4_Dsharp = tk.Button(
            self.sus4, text="D#", highlightbackground='black', command=lambda: self.play_suspended_4th_chord('D#', current_octave))
        self.sus4_Dsharp.grid(row=1, column=4)
        self.sus4_E = tk.Button(
            self.sus4, text="E", command=lambda: self.play_suspended_4th_chord('E', current_octave))
        self.sus4_E.grid(row=1, column=5)
        self.sus4_F = tk.Button(
            self.sus4, text="F", command=lambda: self.play_suspended_4th_chord('F', current_octave))
        self.sus4_F.grid(row=1, column=6)
        self.sus4_Fsharp = tk.Button(
            self.sus4, text="F#", highlightbackground='black', command=lambda: self.play_suspended_4th_chord('F#', current_octave))
        self.sus4_Fsharp.grid(row=1, column=7)
        self.sus4_G = tk.Button(
            self.sus4, text="G", command=lambda: self.play_suspended_4th_chord('G', current_octave))
        self.sus4_G.grid(row=1, column=8)
        self.sus4_Gsharp = tk.Button(
            self.sus4, text="G#", highlightbackground='black', command=lambda: self.play_suspended_4th_chord('G#', current_octave))
        self.sus4_Gsharp.grid(row=1, column=9)
        self.sus4_A = tk.Button(
            self.sus4, text="A", command=lambda: self.play_suspended_4th_chord('A', current_octave))
        self.sus4_A.grid(row=1, column=10)
        self.sus4_Asharp = tk.Button(
            self.sus4, text="A#", highlightbackground='black', command=lambda: self.play_susperved_4th_chord('A#', current_octave))
        self.sus4_Asharp.grid(row=1, column=11)
        self.sus4_B = tk.Button(
            self.sus4, text="B", command=lambda: self.play_suspended_4th_chord('B', current_octave))


# =======================================================================================================================
# =======================================================================================================================
# ===========AUGMENTED CHORDS========================================================================================
# =======================================================================================================================
# =======================================================================================================================

        self.aug = tk.Frame(self.master)
        self.aug.grid(row=10)
        # create a label for the augmented chords
        self.aug_label = tk.Label(
            self.aug, text="Augmented Chords", font=("Helvetica", 16))
        self.aug_label.grid(row=0, column=0)
        # create buttons for the augmented chords
        self.aug_C = tk.Button(
            self.aug, text="C", command=lambda: self.play_augmented_chord('C', current_octave))
        self.aug_C.grid(row=1, column=1)
        self.aug_Csharp = tk.Button(
            self.aug, text="C#", highlightbackground='black', command=lambda: self.play_augmented_chord('C#', current_octave))
        self.aug_Csharp.grid(row=1, column=2)
        self.aug_D = tk.Button(
            self.aug, text="D", command=lambda: self.play_augmented_chord('D', current_octave))
        self.aug_D.grid(row=1, column=3)
        self.aug_Dsharp = tk.Button(
            self.aug, text="D#", highlightbackground='black', command=lambda: self.play_augmented_chord('D#', current_octave))
        self.aug_Dsharp.grid(row=1, column=4)
        self.aug_E = tk.Button(
            self.aug, text="E", command=lambda: self.play_augmented_chord('E', current_octave))
        self.aug_E.grid(row=1, column=5)
        self.aug_F = tk.Button(
            self.aug, text="F", command=lambda: self.play_augmented_chord('F', current_octave))
        self.aug_F.grid(row=1, column=6)
        self.aug_Fsharp = tk.Button(
            self.aug, text="F#", highlightbackground='black', command=lambda: self.play_augmented_chord('F#', current_octave))
        self.aug_Fsharp.grid(row=1, column=7)
        self.aug_G = tk.Button(
            self.aug, text="G", command=lambda: self.play_augmented_chord('G', current_octave))
        self.aug_G.grid(row=1, column=8)
        self.aug_Gsharp = tk.Button(
            self.aug, text="G#", highlightbackground='black', command=lambda: self.play_augmented_chord('G#', current_octave))
        self.aug_Gsharp.grid(row=1, column=9)
        self.aug_A = tk.Button(
            self.aug, text="A", command=lambda: self.play_augmented_chord('A', current_octave))
        self.aug_A.grid(row=1, column=10)
        self.aug_Asharp = tk.Button(
            self.aug, text="A#", highlightbackground='black', command=lambda: self.play_augmented_chord('A#', current_octave))
        self.aug_Asharp.grid(row=1, column=11)
        self.aug_B = tk.Button(
            self.aug, text="B", command=lambda: self.play_augmented_chord('B', current_octave))
        self.aug_B.grid(row=1, column=12)

# =======================================================================================================================
# =======================================================================================================================
# ===========MAJOR 9TH CHORDS========================================================================================
# =======================================================================================================================
# =======================================================================================================================
        self.maj9 = tk.Frame(self.master)
        self.maj9.grid(row=11)
        # create a label for the major 9th chords
        self.maj9_label = tk.Label(
            self.maj9, text="Major 9th Chords", font=("Helvetica", 16))
        self.maj9_label.grid(row=0, column=0)
        # create buttons for the major 9th chords
        self.maj9_C = tk.Button(
            self.maj9, text="C", command=lambda: self.play_major_9th_chord('C', current_octave))
        self.maj9_C.grid(row=1, column=1)
        self.maj9_Csharp = tk.Button(
            self.maj9, text="C#", highlightbackground='black', command=lambda: self.play_major_9th_chord('C#', current_octave))
        self.maj9_Csharp.grid(row=1, column=2)
        self.maj9_D = tk.Button(
            self.maj9, text="D", command=lambda: self.play_major_9th_chord('D', current_octave))
        self.maj9_D.grid(row=1, column=3)
        self.maj9_Dsharp = tk.Button(
            self.maj9, text="D#", highlightbackground='black', command=lambda: self.play_major_9th_chord('D#', current_octave))
        self.maj9_Dsharp.grid(row=1, column=4)
        self.maj9_E = tk.Button(
            self.maj9, text="E", command=lambda: self.play_major_9th_chord('E', current_octave))
        self.maj9_E.grid(row=1, column=5)
        self.maj9_F = tk.Button(
            self.maj9, text="F", command=lambda: self.play_major_9th_chord('F', current_octave))
        self.maj9_F.grid(row=1, column=6)
        self.maj9_Fsharp = tk.Button(
            self.maj9, text="F#", highlightbackground='black', command=lambda: self.play_major_9th_chord('F#', current_octave))
        self.maj9_Fsharp.grid(row=1, column=7)
        self.maj9_G = tk.Button(
            self.maj9, text="G", command=lambda: self.play_major_9th_chord('G', current_octave))
        self.maj9_G.grid(row=1, column=8)
        self.maj9_Gsharp = tk.Button(
            self.maj9, text="G#", highlightbackground='black', command=lambda: self.play_major_9th_chord('G#', current_octave))
        self.maj9_Gsharp.grid(row=1, column=9)
        self.maj9_A = tk.Button(
            self.maj9, text="A", command=lambda: self.play_major_9th_chord('A', current_octave))
        self.maj9_A.grid(row=1, column=10)
        self.maj9_Asharp = tk.Button(
            self.maj9, text="A#", highlightbackground='black', command=lambda: self.play_major_9th_chord('A#', current_octave))
        self.maj9_Asharp.grid(row=1, column=11)
        self.maj9_B = tk.Button(
            self.maj9, text="B", command=lambda: self.play_major_9th_chord('B', current_octave))
        self.maj9_B.grid(row=1, column=12)


# ==============================================================================
# ==============================================================================
# =============MINOR 9TH CHORDS=================================================
# ==============================================================================
# ==============================================================================

        self.min9 = tk.Frame(self.master)
        self.min9.grid(row=12)
        # create a label for the minor 9th chords
        self.min9_label = tk.Label(
            self.min9, text="Minor 9th Chords", font=("Helvetica", 16))
        self.min9_label.grid(row=0, column=0)
        # create buttons for the minor 9th chords
        self.min9_C = tk.Button(
            self.min9, text="C", command=lambda: self.play_minor_9th_chord('C', current_octave))
        self.min9_C.grid(row=1, column=1)
        self.min9_Csharp = tk.Button(
            self.min9, text="C#", highlightbackground='black', command=lambda: self.play_minor_9th_chord('C#', current_octave))
        self.min9_Csharp.grid(row=1, column=2)
        self.min9_D = tk.Button(
            self.min9, text="D", command=lambda: self.play_minor_9th_chord('D', current_octave))
        self.min9_D.grid(row=1, column=3)
        self.min9_Dsharp = tk.Button(
            self.min9, text="D#", highlightbackground='black', command=lambda: self.play_minor_9th_chord('D#', current_octave))
        self.min9_Dsharp.grid(row=1, column=4)
        self.min9_E = tk.Button(
            self.min9, text="E", command=lambda: self.play_minor_9th_chord('E', current_octave))
        self.min9_E.grid(row=1, column=5)
        self.min9_F = tk.Button(
            self.min9, text="F", command=lambda: self.play_minor_9th_chord('F', current_octave))
        self.min9_F.grid(row=1, column=6)
        self.min9_Fsharp = tk.Button(
            self.min9, text="F#", highlightbackground='black', command=lambda: self.play_minor_9th_chord('F#', current_octave))
        self.min9_Fsharp.grid(row=1, column=7)
        self.min9_G = tk.Button(
            self.min9, text="G", command=lambda: self.play_minor_9th_chord('G', current_octave))
        self.min9_G.grid(row=1, column=8)
        self.min9_Gsharp = tk.Button(
            self.min9, text="G#", highlightbackground='black', command=lambda: self.play_minor_9th_chord('G#', current_octave))
        self.min9_Gsharp.grid(row=1, column=9)
        self.min9_A = tk.Button(
            self.min9, text="A", command=lambda: self.play_minor_9th_chord('A', current_octave))
        self.min9_A.grid(row=1, column=10)
        self.min9_Asharp = tk.Button(
            self.min9, text="A#", highlightbackground='black', command=lambda: self.play_minor_9th_chord('A#', current_octave))
        self.min9_Asharp.grid(row=1, column=11)
        self.min9_B = tk.Button(
            self.min9, text="B", command=lambda: self.play_minor_9th_chord('B', current_octave))
        self.min9_B.grid(row=1, column=12)


# =======================================================================================================================
# =======================================================================================================================
# ============DOMINANT 9TH CHORDS========================================================================================
# =======================================================================================================================
# =======================================================================================================================
        self.dom9 = tk.Frame(self.master)
        self.dom9.grid(row=13)
        # create a label for the dominant 9th chords
        self.dom9_label = tk.Label(
            self.dom9, text="Dominant 9th Chords", font=("Helvetica", 16))
        self.dom9_label.grid(row=0, column=0)
        # create buttons for the dominant 9th chords
        self.dom9_C = tk.Button(
            self.dom9, text="C", command=lambda: self.play_dominant_9th_chord('C', current_octave))
        self.dom9_C.grid(row=1, column=1)
        self.dom9_Csharp = tk.Button(
            self.dom9, text="C#", highlightbackground='black', command=lambda: self.play_dominant_9th_chord('C#', current_octave))
        self.dom9_Csharp.grid(row=1, column=2)
        self.dom9_D = tk.Button(
            self.dom9, text="D", command=lambda: self.play_dominant_9th_chord('D', current_octave))
        self.dom9_D.grid(row=1, column=3)
        self.dom9_Dsharp = tk.Button(
            self.dom9, text="D#", highlightbackground='black', command=lambda: self.play_dominant_9th_chord('D#', current_octave))
        self.dom9_Dsharp.grid(row=1, column=4)
        self.dom9_E = tk.Button(
            self.dom9, text="E", command=lambda: self.play_dominant_9th_chord('E', current_octave))
        self.dom9_E.grid(row=1, column=5)
        self.dom9_F = tk.Button(
            self.dom9, text="F", command=lambda: self.play_dominant_9th_chord('F', current_octave))
        self.dom9_F.grid(row=1, column=6)
        self.dom9_Fsharp = tk.Button(
            self.dom9, text="F#", highlightbackground='black', command=lambda: self.play_dominant_9th_chord('F#', current_octave))
        self.dom9_Fsharp.grid(row=1, column=7)
        self.dom9_G = tk.Button(
            self.dom9, text="G", command=lambda: self.play_dominant_9th_chord('G', current_octave))
        self.dom9_G.grid(row=1, column=8)
        self.dom9_Gsharp = tk.Button(
            self.dom9, text="G#", highlightbackground='black', command=lambda: self.play_dominant_9th_chord('G#', current_octave))
        self.dom9_Gsharp.grid(row=1, column=9)
        self.dom9_A = tk.Button(
            self.dom9, text="A", command=lambda: self.play_dominant_9th_chord('A', current_octave))
        self.dom9_A.grid(row=1, column=10)
        self.dom9_Asharp = tk.Button(
            self.dom9, text="A#", highlightbackground='black', command=lambda: self.play_dominant_9th_chord('A#', current_octave))
        self.dom9_Asharp.grid(row=1, column=11)
        self.dom9_B = tk.Button(
            self.dom9, text="B", command=lambda: self.play_dominant_9th_chord('B', current_octave))
        self.dom9_B.grid(row=1, column=12)

# =======================================================================================================================
# =======================================================================================================================
# ============MAJOR 11TH CHORDS==========================================================================================
# =======================================================================================================================
# =======================================================================================================================
        self.maj11 = tk.Frame(self.master)
        self.maj11.grid(row=14)
        # create a label for the major 11th chords
        self.maj11_label = tk.Label(
            self.maj11, text="Major 11th Chords", font=("Helvetica", 16))
        self.maj11_label.grid(row=0, column=0)
        # create buttons for the major 11th chords
        self.maj11_C = tk.Button(
            self.maj11, text="C", command=lambda: self.play_major_11th_chord('C', current_octave))
        self.maj11_C.grid(row=1, column=1)
        self.maj11_Csharp = tk.Button(
            self.maj11, text="C#", highlightbackground='black', command=lambda: self.play_major_11th_chord('C#', current_octave))
        self.maj11_Csharp.grid(row=1, column=2)
        self.maj11_D = tk.Button(
            self.maj11, text="D", command=lambda: self.play_major_11th_chord('D', current_octave))
        self.maj11_D.grid(row=1, column=3)
        self.maj11_Dsharp = tk.Button(
            self.maj11, text="D#", highlightbackground='black', command=lambda: self.play_major_11th_chord('D#', current_octave))
        self.maj11_Dsharp.grid(row=1, column=4)
        self.maj11_E = tk.Button(
            self.maj11, text="E", command=lambda: self.play_major_11th_chord('E', current_octave))
        self.maj11_E.grid(row=1, column=5)
        self.maj11_F = tk.Button(
            self.maj11, text="F", command=lambda: self.play_major_11th_chord('F', current_octave))
        self.maj11_F.grid(row=1, column=6)
        self.maj11_Fsharp = tk.Button(
            self.maj11, text="F#", highlightbackground='black', command=lambda: self.play_major_11th_chord('F#', current_octave))
        self.maj11_Fsharp.grid(row=1, column=7)
        self.maj11_G = tk.Button(
            self.maj11, text="G", command=lambda: self.play_major_11th_chord('G', current_octave))
        self.maj11_G.grid(row=1, column=8)
        self.maj11_Gsharp = tk.Button(
            self.maj11, text="G#", highlightbackground='black', command=lambda: self.play_major_11th_chord('G#', current_octave))
        self.maj11_Gsharp.grid(row=1, column=9)
        self.maj11_A = tk.Button(
            self.maj11, text="A", command=lambda: self.play_major_11th_chord('A', current_octave))
        self.maj11_A.grid(row=1, column=10)
        self.maj11_Asharp = tk.Button(
            self.maj11, text="A#", highlightbackground='black', command=lambda: self.play_major_11th_chord('A#', current_octave))
        self.maj11_Asharp.grid(row=1, column=11)
        self.maj11_B = tk.Button(
            self.maj11, text="B", command=lambda: self.play_major_11th_chord('B', current_octave))
        self.maj11_B.grid(row=1, column=12)


# =======================================================================================================================
# =======================================================================================================================
# ============MINOR 11TH CHORDS==========================================================================================
# =======================================================================================================================
# =======================================================================================================================
        self.min11 = tk.Frame(self.master)
        self.min11.grid(row=15)
        # create a label for the minor 11th chords
        self.min11_label = tk.Label(
            self.min11, text="Minor 11th Chords", font=("Helvetica", 16))
        self.min11_label.grid(row=0, column=0)
        # create buttons for the minor 11th chords
        self.min11_C = tk.Button(
            self.min11, text="C", command=lambda: self.play_minor_11th_chord('C', current_octave))
        self.min11_C.grid(row=1, column=1)
        self.min11_Csharp = tk.Button(
            self.min11, text="C#", highlightbackground='black', command=lambda: self.play_minor_11th_chord('C#', current_octave))
        self.min11_Csharp.grid(row=1, column=2)
        self.min11_D = tk.Button(
            self.min11, text="D", command=lambda: self.play_minor_11th_chord('D', current_octave))
        self.min11_D.grid(row=1, column=3)
        self.min11_Dsharp = tk.Button(
            self.min11, text="D#", highlightbackground='black', command=lambda: self.play_minor_11th_chord('D#', current_octave))
        self.min11_Dsharp.grid(row=1, column=4)
        self.min11_E = tk.Button(
            self.min11, text="E", command=lambda: self.play_minor_11th_chord('E', current_octave))
        self.min11_E.grid(row=1, column=5)
        self.min11_F = tk.Button(
            self.min11, text="F", command=lambda: self.play_minor_11th_chord('F', current_octave))
        self.min11_F.grid(row=1, column=6)
        self.min11_Fsharp = tk.Button(
            self.min11, text="F#", highlightbackground='black', command=lambda: self.play_minor_11th_chord('F#', current_octave))
        self.min11_Fsharp.grid(row=1, column=7)
        self.min11_G = tk.Button(
            self.min11, text="G", command=lambda: self.play_minor_11th_chord('G', current_octave))
        self.min11_G.grid(row=1, column=8)
        self.min11_Gsharp = tk.Button(
            self.min11, text="G#", highlightbackground='black', command=lambda: self.play_minor_11th_chord('G#', current_octave))
        self.min11_Gsharp.grid(row=1, column=9)
        self.min11_A = tk.Button(
            self.min11, text="A", command=lambda: self.play_minor_11th_chord('A', current_octave))
        self.min11_A.grid(row=1, column=10)
        self.min11_Asharp = tk.Button(
            self.min11, text="A#", highlightbackground='black', command=lambda: self.play_minor_11th_chord('A#', current_octave))
        self.min11_Asharp.grid(row=1, column=11)
        self.min11_B = tk.Button(
            self.min11, text="B", command=lambda: self.play_minor_11th_chord('B', current_octave))
        self.min11_B.grid(row=1, column=12)

# =======================================================================================================================
# =======================================================================================================================

        # create a frame and buttons for current_octave selection
        self.current_octave = tk.Frame(self.master)
        self.current_octave.grid(row=16)
        self.current_octave_label = tk.Label(
            self.current_octave, text="current_octave", font=("Helvetica", 16))
        self.current_octave_label.grid(row=0, column=0)

        self.current_octave_up = tk.Button(
            self.current_octave, text="Up", command=lambda: self.current_octave_up_clicked())

        self.current_octave_up.grid(row=0, column=1)

        self.current_octave_down = tk.Button(
            self.current_octave, text="Down", command=lambda: self.current_octave_down_clicked())

        self.current_octave_down.grid(row=0, column=2)

        self.master.mainloop()


app = Prototype1(tk.Tk())
