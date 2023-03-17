from tkinter import *
import tkinter as tk
import tkinter.messagebox
import threading
from tkinter import ttk, filedialog
from pygame import mixer
import os
import time
import keyboard
from mutagen.mp3 import MP3

root = Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg = "grey")
root.resizable(False, False)

app_icon = PhotoImage(file="nota.png")
root.iconphoto(False, app_icon)

mixer.init()

#functions():
def open_folder():
    global muzik
    muzik = filedialog.askdirectory()
    if muzik:
        os.chdir(muzik)
        songs=os.listdir(muzik)
        for song in songs:
            if song.endswith(".mp3") or song.endswith(".wav") or song.endswith(".ogg"):
               playlist.insert(END, song)  
        
keyboard.add_hotkey('ctrl+o', open_folder)

##İLK GÖSTERİMDE OLMAYACAK
def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    ##add_to_playlist(filename_path)
    ##filename = os.path.basename(filename_path)
    ##index = 0
    ##playlist.insert(END, filename)
    playlist.insert(END, filename_path)
    ##index += 1

##İKİNCİ GÖSTERİMDE OLACAK
def del_song():
    selected_song = playlist.curselection()
    selected_song = int(selected_song[0])
    playlist.delete(selected_song)

##İKİNCİ GÖSTERİMDE OLACAK
def shuffle_playlist():  
   import random
   a = playlist.size()
   b = random.randint(0, a)
   music_name = playlist.get(b)
   mixer.music.load(playlist.get(b))
   mixer.music.play()
   music.config(text=music_name[0:-4])

keyboard.add_hotkey('ctrl+s', shuffle_playlist)


def play_song():    
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()   
    music.config(text=music_name[0:-4])
    ##add playback history list
    playback.insert(END, music_name)


def play_next_song():
    current_song_index = playlist.curselection()[0]
    next_song_index = current_song_index + 1
    playlist.selection_clear(0, END)
    playlist.selection_set(next_song_index)
    mixer.music.stop()
    play_song()

keyboard.add_hotkey('2', play_next_song)

def play_previous_song():
    current_song_index = playlist.curselection()[0]
    previous_song_index = current_song_index - 1
    playlist.selection_clear(0, END)
    playlist.selection_set(previous_song_index)
    mixer.music.stop()
    play_song()

keyboard.add_hotkey('8', play_next_song)

def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

def mute_music():
    mixer.music.set_volume(0)
    scale.set(0)

def noise_music():
    mixer.music.set_volume(0.7)
    scale.set(70)

"""def length_song():
    song_mutagen = MP3(filename)
    song_length = song_mutagen.info.length

    convert_length = time.strftime('%M:%S',time.gmtime(song_length))
    length_bar.config(text=f'Total Length:-00:00:{convert_length}')

length_bar = Label(root, text='Total Length:-00:00', font=20)
length_bar.place(x=5, y=27)"""

##ICONS AND BUTTONS
Button(root, text="PLAY", width=10, height=2, font=("arial", 13, "bold"), fg="black", bg="yellow", command=play_song).place(x=155, y=400)

Button(root, text=">", width=5, height=2, font=("arial", 13, "bold"), fg="black", bg="yellow", command=play_song).place(x=300, y=500)
Button(root, text="<", width=5, height=2, font=("arial", 13, "bold"), fg="black", bg="yellow", command=play_song).place(x=50, y=500)

resume_button = PhotoImage(file="resume.png")
Button(root,image=resume_button,bg="black",bd=0, command=mixer.music.unpause).place(x=120 ,y=490)

pause_button = PhotoImage(file="pause.png")
Button(root,image=pause_button,bg="black",bd=0, command=mixer.music.pause).place(x=210 ,y=490)


##İKİNCİ GÖSTERİMDE
repeat_button = PhotoImage(file="repeat.png")
Button(root,image=repeat_button,bg="black",bd=0, command=play_song).place(x=160 ,y=580)

shuffle_button = PhotoImage(file="shuffle.png")
Button(root,image=shuffle_button,bg="white",bd=0, command=play_song).place(x=260, y=580)
####


playlistFrame_background = PhotoImage(file="menu.png")
Label(root, image=playlistFrame_background, bg="black").pack(padx=10,pady=50,side=RIGHT)

mute_icon = PhotoImage(file="mute.png")
noise_icon = PhotoImage(file="noise.png")


##MENU BAR
menu_bar = Menu(root)
root.configure(menu=menu_bar)

m1 = Menu(menu_bar,background="grey",tearoff=False,bd=8,activebackground="black")
menu_bar.add_cascade(label="File",menu=m1)
m1.add_command(label="Open...       Ctrl+O", command=open_folder)

##İLK GÖSTERİMDE OLMAYACAK
m1.add_command(label="Add Song",command=browse_file)

##İKİNCİ GÖSTERİMDE
m2 = Menu(menu_bar,background="grey",tearoff=False,bd=8,activebackground="black")
menu_bar.add_cascade(label="Play",menu=m2)
m2.add_command(label="Shuffle...        Ctrl+S",command=shuffle_playlist)
m2.add_command(label="Repeat", command=play_song)
####
##FİNAL PRODUCT
m2.add_command(label="Playback History...       Ctrl+H")

####


#Music name and display
music = Label(root,text="",font=("arial", 15),fg="white", bg="grey")
music.place(x=250, y=300, anchor="center")


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
playlist = Listbox(music_frame, width=100, font=("arial", 10), bg="grey", fg="black", selectbackground="lightblue", 
                   cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

##BOTTOM FRAME #İKİNCİ GÖSTERİMDE
Button(root, text="OPEN PLAYLIST", width=15, height=2, font=("arial", 12, "bold"), fg="white", bg="cyan", command=open_folder).place(x=595, y=515)
Button(root, text="+", width=5, height=2, font=("arial", 13, "bold"), fg="white", bg="cyan", command=browse_file).place(x=805, y=515)
Button(root, text="-", width=5, height=2, font=("arial", 13, "bold"), fg="white", bg="cyan", command=del_song).place(x=475, y=515)



##FİNAL PRODUCT
##playback history place
new_frame = Frame(root, bd=2, relief=RIDGE)
new_frame.place(x=40, y=150, width=400, height=200) 

playback = Listbox(new_frame, width=100, font=("arial", 10), bg="grey", fg="black", selectbackground="lightblue", 
                        cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playback.pack(side=LEFT, fill=BOTH)




####


root.mainloop()
