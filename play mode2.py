from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3


root = Tk()
root.title('Play Mode')

root.iconbitmap('D:\\computer\\cs@aut\\term2\\AP\\music player\\icons\\title-icon.ico')
root.geometry("500x350")

pygame.mixer.init()

def add_song():
	song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ("WAV Files","*.WAV"),))
	
	song = song.replace("D:/computer/cs@aut/term2/AP/music player/music/", "")
    
	song = song.replace(".mp3", "")

	# Add song to listbox
	song_box.insert(END, song)


# Add many songs to playlist
def add_many_songs():
	songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))	
	
	for song in songs:
		song = song.replace("C:", "")
		song = song.replace(".mp3", "")
		# Insert into playlist
		song_box.insert(END, song)


def play_time():
	current_time = pygame.mixer.music.get_pos() /1000

	converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

	song = song_box.get(ACTIVE)

	song = f'D:/computer/cs@aut/term2/AP/music player/{song}.mp3'

	song_mut = MP3(song)

	song_length = song_mut.info.Length
	
	converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))
	
	status_bar.config.(text= f 'Time Elapsed: {converted_current_time} of {converted_song_length} ')
	
	status_bar.after(1000, play_time)
	
	play_time()


def play():
	song = song_box.get(ACTIVE)
    
	song = f'D:/computer/cs@aut/term2/AP/music player/music/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)


# Stop playing current song
def stop():
	pygame.mixer.music.stop()
	song_box.selection_clear(ACTIVE)

	status_bar.config(text='')



def next_song():
	next_one = song_box.curselection()
	next_one = next_one[0] + 1
	song = song_box.get(next_one)
	song = f'D:/computer/cs@aut/term2/AP/music player/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)
	song_box.selection_clear(0, END)
	song_box.activate(next_one)
	song_box.selection_set(next_one, last=None)


def previous_song():
	next_one = song_box.curselection()
	next_one = next_one[0] - 1
	song = song_box.get(next_one)
	song = f'D:/computer/cs@aut/term2/AP/music player/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)
	song_box.selection_clear(0, END)
	song_box.activate(next_one)
	song_box.selection_set(next_one, last=None)



# Create Global Pause Variable
global paused
paused = False

def delete_song():
	song_box.delete(ANCHOR)
	pygame.mixer.music.stop()


def delete_all_songs():
	song_box.delete(0, END)
	pygame.mixer.music.stop()



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
		
		
def division_by_artist():
	pass
	
	
	
def your_playlist():
	pass



# Create Playlist Box
song_box = Listbox(root, bg="black", fg="red", width=60, selectbackground="red", selectforeground="black")
song_box.pack(pady=20)

# Define Player Control Button Images
back_img = PhotoImage(file='D:/computer/cs@aut/term2/AP/music player/icons/back.png')
stop_img = PhotoImage(file='D:/computer/cs@aut/term2/AP/music player/icons/stop.png')
play_img = PhotoImage(file='D:/computer/cs@aut/term2/AP/music player/icons/play.png')
pause_img = PhotoImage(file='D:/computer/cs@aut/term2/AP/music player/icons/pause.png')
next_img = PhotoImage(file='D:/computer/cs@aut/term2/AP/music player/icons/next.png')

# Create Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()

# Create Player Control Buttons
back_button = Button(controls_frame, image=back_img, borderwidth=0, command= previous_song)
next_button = Button(controls_frame, image=next_img, borderwidth=0, command=next_song)
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
add_song_menu.add_command(label="Add Many Songs To Queue", command=add_many_songs)


remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="remove Songs", menu=add_song_menu)
remove_song_menu.add_command(label="delete A Song To Queue", command=delete_song)
remove_song_menu.add_command(label="delete Many Songs To Queue", command=delete_many_songs)


status_bar = Label(root, text='', bd=1, relief=GROOVE,anchor=E )
status_bar.pack(fill=X, side=BOTTOM, ipady=2)


division_by_artist = Menu(my_menu)
my_menu.add_cascade(label="Artists",menu=add_song_menu)
division_by_artist.add_command(label="Artists", command= division_by_artist)


your_playlist = Menu(my_menu)
my_menu.add_cascade(label="fav music",menu=add_song_menu)
your_playlist.add_command(label="you're fav music", command = your_playlist)


root.mainloop() 