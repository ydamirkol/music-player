from tkinter import *
import pygame
import os
window=Tk()
window.geometry("400x150")

pygame.mixer.init()

n=0

def start_stop():
    global n
    n=n+1
    if n==1:
        song_name=songs_listbox.get()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(0)
        print("music started")
    elif (n%2)==0:
        pygame.mixer.music.pause()
        print("paused")
    elif (n%2)!=0:
        pygame.mixer.music.unpaused()
        print("unpaused")

l1=Label(window,text="MUSIC PLAYER",font ="times 20")
l1.grid(row=1,column=1)


b2=button(window,text='start/stop',width=20,command=start_stop)
b2.grid(row=4,column=1)

song_list=os.listdir()
song_listbox=stringVar(window)
song_listbox.set("select songs")
menu=optionMenu(window,songs_listbox,*songs_list)

window.mainloop()
