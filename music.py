#!/usr/bin/env python
from tkinter import *
import pygame
from tkinter import filedialog
import os
root = Tk()
root.title('Play Mode')
#felan directory khodeto mikhay bezar ta ye rahi vase gereftane directory barash peida konim
root.iconbitmap('title-icon.ico')
root.geometry("400x350")
mu= /music.py

pygame.mixer.init()


#Add Song Function for queue
def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)

    mixer.music.queue(filename_path)


def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1


menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)
    
   

def play():
	song = song_box.get(ACTIVE)
    #age tunesti ruye gereftane directory bebin chizi mishe zad inja man tuye khat payin directory khodamo zadam
	song = '/music.py'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

# Stop playing current song
def stop():
	pygame.mixer.music.stop()
	song_box.selection_clear(ACTIVE)

# Create Global Pause Variable
global paused
paused = False

# Pause and Unpause The Current Song
def pause(is_paused):
	global paused
	paused = is_paused

	if paused:
		# Unpause
		pygame.mixer.music.unpause()
		paused = False
	else:
		# Pause
		pygame.mixer.music.pause()
		paused = True
	


# Create Playlist Box
song_box = Listbox(root, bg="black", fg="red", width=60, selectbackground="red", selectforeground="black")
song_box.pack(pady=20)

# Define Player Control Button Images
back_img = PhotoImage(file= 'mu player/icons/back.png')
stop_img = PhotoImage(file= 'mu player/icons/stop.png')
play_img = PhotoImage(file= 'mu player/icons/play.png')
pause_img = PhotoImage(file= 'mu player/icons/pause.png')
next_img = PhotoImage(file='mu player/icons/next.png')

# Create Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()

# Create Player Control Buttons
back_button = Button(controls_frame, image=back_img, borderwidth=0)
next_button = Button(controls_frame, image=next_img, borderwidth=0)
play_button = Button(controls_frame, image=play_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_img, borderwidth=0, command=lambda: pause(paused))
stop_button =  Button(controls_frame, image=stop_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10, pady=10)
stop_button.grid(row=0, column=1, padx=10, pady=10)
play_button.grid(row=0, column=2, padx=10, pady=10)
pause_button.grid(row=0, column=3, padx=10, pady=10)
next_button.grid(row=0, column=4, padx=10, pady=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Add Song Menu 
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add A Song To Queue", command=add_song)
# Add Many Songs to Queue
#add_song_menu.add_command(label="Add Many Songs To Queue", command=add_many_songs)




root.mainloop()