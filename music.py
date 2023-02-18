from tkinter import *
from tkinter import filedialog
import pygame
import os #standard library module


root = Tk()
root.title('MUSIC PLAYER')
root.geometry("700x800")

pygame.mixer.init() ##mixer module

menu_bar = Menu(root)
root.config(menu=menu_bar)

songs = []
current_song = ""
paused = False

def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        playlist.insert("end", song)
    
    playlist.selection_set(0)
    current_song = songs[playlist.curselection()[0]]

def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global pause
    pygame.mixer.music.pause()
    paused = True

def resume_music():
    pass

def next_music():
    global current_song, paused

    try:
        playlist.selection_clear(0, END)
        playlist.select_set(songs.index(current_song) + 1)
        current_song = songs[playlist.curselection()[0]]
        play_music()
    except:
        pass

def previous_music():
    global current_song, paused

    try:
        playlist.selection_clear(0, END)
        playlist.selection_set(songs.index(current_song)-1)
        current_song = songs[playlist.curselection()[0]]
        play_music()
    except:
        pass




organize_menu = Menu(menu_bar, tearoff=False)
organize_menu.add_command(label='Select playlist', command=load_music)
menu_bar.add_cascade(label='Playlists', menu=organize_menu)

playlist = Listbox(root, bg="black", fg="white", width=400, height=42)
playlist.pack()

playButton = PhotoImage(file='play.png')
pauseButton = PhotoImage(file='pause.png')
resumeButton = PhotoImage(file='resume.png')
nextButton = PhotoImage(file='right.png')
previousButton = PhotoImage(file='left.png')
repeatButton = PhotoImage(file='repeat.png')

control_frame = Frame(root)
control_frame.pack()

playButton_image = Button(control_frame, image=playButton, borderwidth=0, command=play_music)
pauseButton_image = Button(control_frame, image=pauseButton, borderwidth=0, command=pause_music)
resumeButton_image = Button(control_frame, image=resumeButton, borderwidth=0, command=resume_music)
nextButton_image = Button(control_frame, image=nextButton, borderwidth=0, command=next_music)
previousButton_image = Button(control_frame, image=previousButton, borderwidth=0, command=previous_music)
repeatButton_image = Button(control_frame, image=repeatButton, borderwidth=0)

playButton_image.grid(row=0, column=0, padx=7, pady=10)
pauseButton_image.grid(row=0, column=1, padx=7, pady=10)
resumeButton_image.grid(row=0, column=2,padx=7, pady=10)
nextButton_image.grid(row=0, column=3, padx=7, pady=10)
previousButton_image.grid(row=0, column=4, padx=7, pady=10)
repeatButton_image.grid(row=0, column=5, padx=7, pady=10)

root.mainloop()

