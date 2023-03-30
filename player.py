from tkinter import *
import tkinter as tk
import tkinter.messagebox
import threading
from tkinter import ttk, filedialog
from pygame import mixer
import os
import time
import keyboard
from tkinter import messagebox

root = Tk()
root.title("Music Player")
root.geometry("920x670")
root.resizable(False, False)

background = PhotoImage(file="images\colorful.png") 
background_label = Label(root, image=background)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
image1 = PhotoImage(file="images\colorful.png")
image2 = PhotoImage(file="images\Blue.png")
image3 = PhotoImage(file="images\purple.png")

app_icon = PhotoImage(file="images\musicNote.png")
root.iconphoto(False, app_icon)

mixer.init()

def animation():
    global background, image1, image2, image3
    background=image1
    image1=image2
    image2=image3
    image3=background
    background_label.config(image=background)
    background_label.after(6000,animation)

def open_folder():
    animation()
    filename_path = filedialog.askdirectory()
    if filename_path:
        os.chdir(filename_path)
        songs=os.listdir(filename_path)
        for song in songs:
            if song.endswith(".mp3") or song.endswith(".wav") or song.endswith(".ogg"):
               songlist.insert(END, filename_path+'/'+song)

keyboard.add_hotkey('ctrl+o', open_folder)

def play_song():    
    music_name = songlist.get(songlist.curselection())
    mixer.music.load(music_name)
    mixer.music.play()   
    music.config(text=music_name[0:-4])

keyboard.add_hotkey('space', play_song)

def play_next_song():
    current_song_index = songlist.curselection()[0]
    next_song_index = current_song_index + 1
    songlist.selection_clear(0, END)
    songlist.selection_set(next_song_index)
    play_song()


def play_previous_song():
    current_song_index = songlist.curselection()[0]
    previous_song_index = current_song_index - 1
    songlist.selection_clear(0, END)
    songlist.selection_set(previous_song_index)
    play_song()


def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

def mute_music():
    mixer.music.set_volume(0)
    scale.set(0)

def noise_music():
    mixer.music.set_volume(0.7)
    scale.set(70)

def about():
    messagebox.showinfo("About", "Produced by Ahmet Alaçam\n              2023")

##ICONS AND BUTTONS
Button(root, text="PLAY", width=10, height=2, font=("arial", 13, "bold"), fg="black", bg="gold", bd=4, command=play_song).place(x=155, y=300)
Button(root, text=">", width=5, height=2, font=("arial", 13, "bold"), fg="black", bg="gold", bd=4, command=play_next_song).place(x=300, y=300)
Button(root, text="<", width=5, height=2, font=("arial", 13, "bold"), fg="black", bg="gold", bd=4, command=play_previous_song).place(x=60, y=300)

resume_button = PhotoImage(file="images\Resume.png")
Button(root,image=resume_button,bg="gold",bd=4, command=mixer.music.unpause).place(x=120 ,y=380)

pause_button = PhotoImage(file="images\pause.png")
Button(root,image=pause_button,bg="gold",bd=4, command=mixer.music.pause).place(x=210 ,y=380)

repeat_button = PhotoImage(file="images\Repeat.png")
Button(root,image=repeat_button,bg="gold",bd=4, command=play_song).place(x=165, y=480)

playlistFrame_background = PhotoImage(file="images\menu.png")
Label(root, image=playlistFrame_background, bg="black", bd=2).pack(padx=10,pady=50,side=RIGHT)

mute_icon = PhotoImage(file="images\mute.png")
noise_icon = PhotoImage(file="images\musicNoise.png")

##MENU BAR
menu_bar = Menu(root)
root.configure(menu=menu_bar)

m1 = Menu(menu_bar,background="grey",tearoff=False,bd=8,activebackground="black")
menu_bar.add_cascade(label="File",menu=m1)
m1.add_command(label="Open...       Ctrl+O", command=open_folder)

m2 = Menu(menu_bar,background="grey",tearoff=False,bd=8,activebackground="black")
menu_bar.add_cascade(label="Play",menu=m2)
m2.add_command(label="Play...       Space", command=play_song)
m2.add_command(label="Repeat", command=play_song)

m3 = Menu(menu_bar, background="grey",tearoff=False,bd=8,activebackground="black")
menu_bar.add_cascade(label="Help",menu=m3)
m3.add_command(label="About", command=about)

music = Label(root,text="",font=("arial", 15),fg="white", bg="black")
music.place(x=0, y=40, anchor="w")

##PLAYLIST FRAME
music_frame = Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=475, y=100, width=420, height=410)

##VOLUME FRAME
topframe = Frame(music_frame)
topframe.pack()

scale = Scale(topframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.grid(row=0, column=2, pady=15, padx=30)

mute_button = Button(topframe, image=mute_icon, command=mute_music)
mute_button.grid(row=0, column=1)

noise_button = Button(topframe, image=noise_icon, command=noise_music)
noise_button.grid(row=0, column=3)

##PLAYLIST PLACE
scroll = Scrollbar(music_frame)
songlist = Listbox(music_frame, width=100, font=("arial", 10), bg="grey", fg="black", selectbackground="lightblue", 
                   cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=songlist.yview)
scroll.pack(side=RIGHT, fill=Y)
songlist.pack(side=LEFT, fill=BOTH)


root.mainloop()