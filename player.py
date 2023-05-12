from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os
import time
import keyboard
from tkinter import messagebox
import pywhatkit as kit
import webbrowser
from mutagen.mp3 import MP3 


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
    global background, image1, image2, image3, animation_id
    background=image1
    image1=image2
    image2=image3
    image3=background
    background_label.config(image=background)
    animation_id = background_label.after(6000,animation)

def open_folder():
    filename_path = filedialog.askdirectory()
    if filename_path:
        songs=os.listdir(filename_path)
        for song in songs:
            if song.endswith(".mp3") or song.endswith(".wav") or song.endswith(".ogg"):
               songlist.insert(END, filename_path+'/'+song)

keyboard.add_hotkey('ctrl+o', open_folder)

def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    songlist.insert(END, filename_path)

def del_song():
    selected_song = songlist.curselection()
    selected_song = int(selected_song[0])
    songlist.delete(selected_song)

def play_song():  
    length_bar_mp3()
    animation_id = animation()
    music_name = songlist.get(songlist.curselection())
    mixer.music.load(music_name)
    mixer.music.play()   
    music.config(text=music_name[67:-4])
    #playback History
    playback.insert(END, music_name)
    return animation_id

keyboard.add_hotkey('space', play_song)

def pause_music():
    mixer.music.pause()
    background_label.after_cancel(animation_id)

def unpause_music():
    mixer.music.unpause()
    background_label.after(6000,animation)

def repeat_music():
    mixer.music.play()  
    background_label.after(6000,animation)

def play_next_song():
    current_song_index = songlist.curselection()[0]
    next_song_index = current_song_index + 1
    songlist.selection_clear(0, END)
    songlist.selection_set(next_song_index)
    music_name = songlist.get(songlist.curselection())    
    mixer.music.load(music_name)
    mixer.music.play()
    music.config(text=music_name[67:-4])

def play_previous_song():
    current_song_index = songlist.curselection()[0]
    previous_song_index = current_song_index - 1
    songlist.selection_clear(0, END)
    songlist.selection_set(previous_song_index)
    music_name = songlist.get(songlist.curselection())    
    mixer.music.load(music_name)
    mixer.music.play()
    music.config(text=music_name[67:-4])    

def shuffle_playlist():  
   import random
   a = songlist.size()
   b = random.randint(0, a)
   music_name = songlist.get(b)
   songlist.selection_clear(0, END)
   songlist.selection_set(b)
   mixer.music.load(music_name)
   mixer.music.play()
   music.config(text=music_name[67:-4])

keyboard.add_hotkey('ctrl+s', shuffle_playlist)

def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

def mute_music():
    mixer.music.set_volume(0)
    scale.set(0)

def noise_music():
    mixer.music.set_volume(1.0)
    scale.set(100)

def about():
    messagebox.showinfo("About", "Produced by Ahmet Alaçam\n              2023")

def help_page():
    html_url='file:///C:/Users/ahmet/Desktop/Second Review of Engineering Project\SUPPORT-MaSNo.html'
    webbrowser.open_new_tab(html_url)



def playOnYT():
    L2=E1.get()
    kit.playonyt(L2)

def searchFrame():
    global E1, L1, search, exit_button       
    L1=Label(root, text="Search on Youtube", font=60,bg="black",fg="white")
    L1.pack()
   
    E1 = Entry(root, font=60, bd=5)
    E1.pack()

    search = Button(root, text="Search", font=40,bd=5,bg="black",fg="white", command=playOnYT)
    search.pack()

    exit_button = Button(root, text="X", font=("arial", 13, "bold"), bd=5, bg="black",fg="red", command=hideSearchFrame)
    exit_button.pack()

def hideSearchFrame():
    L1.pack_forget()
    E1.pack_forget()
    search.pack_forget()
    exit_button.pack_forget()

def length_bar_mp3():
    global current_time
    current_time=mixer.music.get_pos()/1000
    seconds=time.strftime('%M:%S', time.gmtime(current_time))
    song_name = songlist.get(songlist.curselection())

    song_mut=MP3(song_name)
    song_mut_length=song_mut.info.length
    minute_second=time.strftime('%M:%S', time.gmtime(song_mut_length))
  
    filelabel.after(1000, length_bar_mp3)
    filelabel.config(text=f'Current Time:{seconds}-:{minute_second}:Total Length')

def playback_history():
    global new_frame
    global playback
    new_frame = Frame(root, bd=2, relief=RIDGE)
    new_frame.place(x=300, y=10, width=400, height=400) 

    playback = Listbox(new_frame, width=100, font=("arial", 10), bg="grey", fg="black", selectbackground="lightblue", 
                            cursor="hand2", bd=0)
    playback.pack(side=LEFT, fill=BOTH)
    new_frame.pack()

def hide_playback_history():
    new_frame.pack_forget()



##ICONS, BUTTONS and LABELS
Button(root, text="PLAY", width=10, height=2, font=("arial", 13, "bold"), fg="black", bg="gold", bd=4, command=play_song).place(x=147, y=260)
Button(root, text=">", width=5, height=2, font=("arial", 13, "bold"), fg="black", bg="gold", bd=4, command=play_next_song).place(x=300, y=260)
Button(root, text="<", width=5, height=2, font=("arial", 13, "bold"), fg="black", bg="gold", bd=4, command=play_previous_song).place(x=60, y=260)

resume_button = PhotoImage(file="images\Resume.png")
Button(root,image=resume_button,bg="gold",bd=4, command=unpause_music).place(x=180, y=380)

pause_button = PhotoImage(file="images\pause.png")
Button(root,image=pause_button,bg="gold",bd=4, command=pause_music).place(x=80, y=380)

repeat_button = PhotoImage(file="images\Repeat.png")
Button(root,image=repeat_button,bg="gold",bd=4, command=repeat_music).place(x=280, y=380)

shuffle_button = PhotoImage(file="images\shuffle.png")
Button(root,image=shuffle_button,bg="white",bd=0, command=shuffle_playlist).place(x=180, y=480)

playlistFrame_background = PhotoImage(file="images\white.png")
Label(root, image=playlistFrame_background, bg="black", bd=2).pack(padx=10,pady=50,side=RIGHT)

filelabel = Label(text="MAKE SOME NOISE!", bg="white", fg="black",font=("arial", 13, "bold"))
filelabel.place(x=480, y=63)

music = Label(root,text="",font=("arial", 15, "bold"),fg="white", bg="black")
music.place(x=0, y=32, anchor="w")

mute_icon = PhotoImage(file="images\mute.png")
noise_icon = PhotoImage(file="images\musicNoise.png")

#progress_scale=Scale(root,orient="horizontal",from_=0,length=380,
 #                                       command="command",cursor='hand2')
#progress_scale.place(x=80,y=400)

##BOTTOM FRAME
Button(root, text="OPEN PLAYLIST", width=15, height=2, font=("arial", 12, "bold"), fg="white", bg="cyan", command=open_folder).place(x=585, y=515)
Button(root, text="+", width=5, height=2, font=("arial", 13, "bold"), fg="white", bg="cyan", command=browse_file).place(x=805, y=515)
Button(root, text="-", width=5, height=2, font=("arial", 13, "bold"), fg="white", bg="cyan", command=del_song).place(x=475, y=515)

##MENU BAR
menu_bar = Menu(root)
root.configure(menu=menu_bar)

m1 = Menu(menu_bar,background="grey",tearoff=False,bd=8,activebackground="black")
menu_bar.add_cascade(label="File",menu=m1)
m1.add_command(label="Open...       Ctrl+O", command=open_folder)
m1.add_command(label="Add Song",command=browse_file)

m2 = Menu(menu_bar,background="grey",tearoff=False,bd=8,activebackground="black")
menu_bar.add_cascade(label="Play",menu=m2)
m2.add_command(label="Play...              Space", command=play_song)
m2.add_command(label="Repeat...         Ctrl+R", command=repeat_music)
m2.add_command(label="Shuffle...         Ctrl+S",command=shuffle_playlist)

m3 = Menu(menu_bar, background="grey",tearoff=False, bd=8, activebackground="black")
menu_bar.add_cascade(label="Search",menu=m3)
m3.add_command(label="Search on Youtube", command=searchFrame)

m4 = Menu(menu_bar, background="grey",tearoff=False,bd=8,activebackground="black")
menu_bar.add_cascade(label="Help",menu=m4)
m4.add_command(label="About", command=about)
m4.add_command(label="Help", command=help_page)

m5 = Menu(menu_bar, background="grey",tearoff=False,bd=8,activebackground="black")
menu_bar.add_cascade(label="History", menu=m5)
m5.add_command(label="Playback History", command=playback_history)

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
scroll_y = Scrollbar(music_frame)
scroll_x = Scrollbar(music_frame, orient=HORIZONTAL)
songlist = Listbox(music_frame, width=100, font=("arial", 10), bg="grey", fg="black", selectbackground="lightblue", 
                   cursor="hand2", bd=0, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

scroll_y.config(command=songlist.yview)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=songlist.xview)
scroll_x.pack(side=BOTTOM, fill=X)

songlist.pack(side=LEFT, fill=BOTH)



root.mainloop()