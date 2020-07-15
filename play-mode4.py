from tkinter import *
import pygame
from tkinter import filedialog
import time
import random
import tkinter.ttk as ttk
from mutagen.mp3 import MP3
from tinytag import TinyTag


root = Tk()
root.title('Play Mode')
#put your directory that all the project files is in it
root.iconbitmap('D:\\computer\\cs@aut\\term2\\AP\\music player\\icons\\title-icon.ico')
root.geometry("500x350")

pygame.mixer.init()

songs_list = []
n_shuffle = None

class Song(object):
	def __init__(self, title, artist, genre):
		self.title = title
		self.artist = artist
		self.genre = genre
	def get_title(self):
		return self.title
	def get_artist(self):
		return self.artist
	def get_genre(self):
		return self.genre

def choose_directory():
	global folder_selected
	folder_selected = filedialog.askdirectory()


def add_song():
	song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ("WAV Files","*.WAV"),))
	song = song.replace(folder_selected, "")
	song = song.replace("/", "")
	song = song.replace(".mp3", "")
	song_box.insert(END, song)
	songs_list.append(song)


def play_time():

	if stopped:
		return 
	# Grab Current Song Elapsed Time
	current_time = pygame.mixer.music.get_pos() / 1000

	# convert to time format
	converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

	#current playing song
	song = song_box.get(ACTIVE)
	song = folder_selected + '/' + song + '.mp3'

	
	song_mut = MP3(song)
	#song Length
	global song_length
	song_length = song_mut.info.length
   	
	# convert to time
	converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

	# Increase current time by 1 second
	current_time +=1
	
	if int(slider.get()) == int(song_length):
		status_bar.config(text=f'Time Elapsed: {converted_song_length}  of  {converted_song_length}  ')
	elif paused:
		pass
	elif int(slider.get()) == int(current_time):
		# Update Slide
		slider_position = int(song_length)
		slider.config(to=slider_position, value=int(current_time))

	else:
		# Update Slider To position
		slider_position = int(song_length)
		slider.config(to=slider_position, value=int(slider.get()))
		
		# convert to time format
		converted_current_time = time.strftime('%M:%S', time.gmtime(int(slider.get())))

		# Output time to status bar
		status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}  ')

		# Move this thing along by one second
		next_time = int(slider.get()) + 1
		slider.config(value=next_time)

	status_bar.after(1000, play_time)



def add_many_songs():
	songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))	
	
	for song in songs:
		song = song.replace(folder_selected, "")
		song = song.replace("/", "")
		song = song.replace(".mp3", "")
		songs_list.append(song)
		song_box.insert(END, song)


def slide(x):
	song = song_box.get(ACTIVE)
	song = folder_selected + '/' + song + '.mp3'
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0, start=(int(slider.get())))



def play():
	song = song_box.get(ACTIVE)
    
	song = folder_selected + '/' + song + '.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	play_time()

def play_my_song(song):
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0) 
	play_time()

global stopped
stopped = False
def stop():
	status_bar.config(text='')
	slider.config(value=0)

	pygame.mixer.music.stop()
	song_box.selection_clear(ACTIVE)

	status_bar.config(text='')

	global stopped
	stopped = True



def next_song():
	status_bar.config(text='')
	slider.config(value=0)
	next_one = song_box.curselection()
	next_one = next_one[0]+1
	song = song_box.get(next_one)
	song = folder_selected + '/' + song + '.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)
	song_box.selection_clear(0, END)
	song_box.activate(next_one)
	song_box.selection_set(next_one, last=None)


def previous_song():
	next_one = song_box.curselection()
	next_one = next_one[0]-1
	song = song_box.get(next_one)
	song = folder_selected + '/' + song + '.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)
	song_box.selection_clear(0, END)
	song_box.activate(next_one)
	song_box.selection_set(next_one, last=None)



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
		
		pygame.mixer.music.unpause()
		paused = False
	else:
		
		pygame.mixer.music.pause()
		paused = True

def shuffle():
	#when you click on shuffle button a new song will play immediately
	i = 0
	play()
	play_time()
	for i in range(len(songs_list)):
		songs_number = random.randint(0,len(songs_list)+1)
		song = folder_selected + '/' + songs_list[songs_number] + '.mp3'
		play_my_song(song)



def repeat():
	play_time()
	song = song_box.get(ACTIVE)
	song = folder_selected + '/' + song + '.mp3'
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(-1)



song_box = Listbox(root, bg="black", fg="red", width=60, selectbackground="red", selectforeground="black")
song_box.pack(pady=10)


back_img = PhotoImage(file='D:/computer/cs@aut/term2/AP/music player/icons/back.png')
stop_img = PhotoImage(file='D:/computer/cs@aut/term2/AP/music player/icons/stop.png')
play_img = PhotoImage(file='D:/computer/cs@aut/term2/AP/music player/icons/play.png')
pause_img = PhotoImage(file='D:/computer/cs@aut/term2/AP/music player/icons/pause.png')
next_img = PhotoImage(file='D:/computer/cs@aut/term2/AP/music player/icons/next.png')
shuffle_img = PhotoImage(file='D:/computer/cs@aut/term2/AP/music player/icons/shuffle.png')
repeat_img = PhotoImage(file='D:/computer/cs@aut/term2/AP/music player/icons/repeat.png')

#creat slider
slider = ttk.Scale(root, from_=0 , to=100, length=380, orient=HORIZONTAL, value=0, command=slide)
slider.pack()

controls_frame = Frame(root)
controls_frame.pack(pady=10)


back_button = Button(controls_frame, image=back_img, borderwidth=0, command= previous_song)
next_button = Button(controls_frame, image=next_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_img, borderwidth=0, command=lambda: pause(paused))
stop_button =  Button(controls_frame, image=stop_img, borderwidth=0, command=stop)
shuffle_button = Button(controls_frame, image=shuffle_img, borderwidth=0, command=shuffle)
repeat_button = Button(controls_frame, image=repeat_img, borderwidth=0, command=repeat)

back_button.grid(row=0, column=0, padx=10)
stop_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
next_button.grid(row=0, column=4, padx=10)
shuffle_button.grid(row=0, column=5, padx=10)
repeat_button.grid(row=0, column=6, padx=10)

#menu part
my_menu = Menu(root)
root.config(menu=my_menu)

#choose directory for menu
choose_directory_menu = Menu(my_menu)
my_menu.add_cascade(label="Directory", menu=choose_directory_menu)
choose_directory_menu.add_command(label="Choose Directory", command=choose_directory)

#add song for menu 
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add A Song To Queue", command=add_song)
add_song_menu.add_command(label="Add Many Songs To Queue", command=add_many_songs)

#remove song for menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="delete A Song from Queue", command=delete_song)
remove_song_menu.add_command(label="delete All Songs from Queue", command=delete_all_songs)

#status
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)


your_playlist = Menu(my_menu)
my_menu.add_cascade(label="fav music",menu=add_song_menu)
your_playlist.add_command(label="you're fav music", command = your_playlist)



root.mainloop() 