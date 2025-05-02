import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("LilyEmerald")
canvas.geometry("600x800")
canvas.config(bg = 'black')

rootpath = "C:\\Users\mradw427\Documents\GitHub\PythonMusicPlayer\Music"
pattern = "*.mp3"

prev_img = tk.PhotoImage(file = "prevButton.png")
stop_img = tk.PhotoImage(file = "stopButton.png")
play_img = tk.PhotoImage(file = "playButton.png")
pause_img = tk.PhotoImage(file = "pauseButton.png")
next_img = tk.PhotoImage(file = "nextButton.png")

listBox = tk.Listbox(canvas, fg = "cyan", bg = "black", width = 100, font = ('poppins', 14))
listBox.pack(padx = 15, pady = 15)

label = tk.Label(canvas, text = '', bg = 'black', fg = 'yellow', font = ('poppins', 18))
label.pack(pady = 15)

top = tk.Frame(canvas, bg = "black")
top.pack(padx = 10, pady = 5, anchor = 'center')

prevButton = tk.Button(canvas, text = "Prev", image = prev_img, bg = 'black', borderwidth =0)
prevButton.pack(pady = 15, in_=top, side = 'left')

stopButton = tk.Button(canvas, text = "Stop", image = stop_img, bg = 'black', borderwidth =0)
stopButton.pack(pady = 15, in_=top, side = 'left')

playButton = tk.Button(canvas, text = "Play", image = play_img, bg = 'black', borderwidth =0)
playButton.pack(pady = 15, in_=top, side = 'left')

pauseButton = tk.Button(canvas, text = "Pause", image = pause_img, bg = 'black', borderwidth =0)
pauseButton.pack(pady = 15, in_=top, side = 'left')

nextButton = tk.Button(canvas, text = "Next", image = next_img, bg = 'black', borderwidth =0)
nextButton.pack(pady = 15, in_=top, side = 'left')


for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()