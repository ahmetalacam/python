from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg = "grey")
root.resizable(False, False)

mixer.init()
#functions():
def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

def play_song():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-15])

image_icon = PhotoImage(file="repeat.png")
root.iconphoto(False, image_icon)

Top = PhotoImage(file="mcIcon.png")
Label(root,image=Top,bg="red").pack()

##buttons
play_button = PhotoImage(file="play.png")
Button(root, image=play_button,bg="black",bd=0, command=play_song).place(x=155, y=400)

next_button = PhotoImage(file="right.png")
Button(root,image=next_button,bg="white",bd=0).place(x=10 ,y=470)

previous_button = PhotoImage(file="left.png")
Button(root,image=previous_button,bg="white",bd=0).place(x=110 ,y=470)

resume_button = PhotoImage(file="resume.png")
Button(root,image=resume_button,bg="black",bd=0, command=mixer.music.unpause).place(x=210 ,y=470)

pause_button = PhotoImage(file="pause.png")
Button(root,image=pause_button,bg="black",bd=0, command=mixer.music.pause).place(x=310 ,y=470)

##repeat_button = PhotoImage(file="repeat.png")
##Button(root,image=repeat_button,bg="black",bd=0).place(x=410 ,y=470)

music = Label(root,text="",font=("arial", 15),fg="white", bg="grey")
music.place(x=250, y=300, anchor="center")

Menu = PhotoImage(file="menu.png")
Label(root, image=Menu, bg="white").pack(padx=10,pady=50,side=RIGHT)

music_frame = Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=475, y=268, width=420, height=340)

Button(root, text="Open Folder", width=15, height=2, font=("arial", 10, "bold"), fg="white", bg="cyan", command=open_folder).place(x=455, y=205)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=("arial", 10), bg="grey", fg="black", selectbackground="lightblue", 
                   cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)


root.mainloop()