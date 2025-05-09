import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("LilyEmerald")
canvas.geometry("600x800")
canvas.config(bg = '#e8bcf0')

rootpath = "C:\\Users\mradw427\Documents\GitHub\MusicPlayer\Music"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file = r"C:\Users\mradw427\Documents\GitHub\MusicPlayer\MusicPlayer\prevButton.png")
stop_img = tk.PhotoImage(file = r"C:\Users\mradw427\Documents\GitHub\MusicPlayer\MusicPlayer\stopButton.png")
play_img = tk.PhotoImage(file = r"C:\Users\mradw427\Documents\GitHub\MusicPlayer\MusicPlayer\playButton.png")
pause_img = tk.PhotoImage(file = r"C:\Users\mradw427\Documents\GitHub\MusicPlayer\MusicPlayer\pauseButton.png")
next_img = tk.PhotoImage(file = r"C:\Users\mradw427\Documents\GitHub\MusicPlayer\MusicPlayer\nextButton.png")

def select():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():       #Previus button but kept "next"                 
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"


listBox = tk.Listbox(canvas, fg = "#98569D", bg = "black", width = 100, font = ('poppins', 14))
listBox.pack(padx = 15, pady = 15)

label = tk.Label(canvas, text = '', bg = '#e8bcf0', fg = 'yellow', font = ('poppins', 18))
label.pack(pady = 15)

top = tk.Frame(canvas, bg = "#e8bcf0")
top.pack(padx = 10, pady = 5, anchor = 'center')

prevButton = tk.Button(canvas, text = "Prev", image = prev_img, bg = '#e8bcf0', borderwidth =0, command = play_prev)
prevButton.pack(pady = 15, in_=top, side = 'left')

stopButton = tk.Button(canvas, text = "Stop", image = stop_img, bg = '#e8bcf0', borderwidth =0, command = stop)
stopButton.pack(pady = 15, in_=top, side = 'left')

playButton = tk.Button(canvas, text = "Play", image = play_img, bg = '#e8bcf0', borderwidth =0, command = select)
playButton.pack(pady = 15, in_=top, side = 'left')

pauseButton = tk.Button(canvas, text = "Pause", image = pause_img, bg = '#e8bcf0', borderwidth =0, command = pause_song)
pauseButton.pack(pady = 15, in_=top, side = 'left')

nextButton = tk.Button(canvas, text = "Next", image = next_img, bg = '#e8bcf0', borderwidth =0, command = play_next)
nextButton.pack(pady = 15, in_=top, side = 'left')


for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()