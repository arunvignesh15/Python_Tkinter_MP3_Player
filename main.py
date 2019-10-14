# Import libraries
from tkinter import *
from pygame import mixer


# Make the Window...
root = Tk()
mixer.init() #Initializing the mixer

root.geometry("300x300")
root.title("Melody")
root.iconbitmap(r"favicon.ico")

# Add Text Data Field...
text = Label(root, text="Lets make some noise!...")
text.pack()

# Add Picture...
photo = PhotoImage(file="play_24.png")
#photolabel = Label(root, image=photo)
#photolabel.pack()

# Add Button function...
def play_song():
    mixer.music.load(r"Ellu Vaya Pookalaye.mp3")
    mixer.music.play()
    print("The Loop for Song is Working!...")

#btn = Button(root, text="Play the Song!", command=play_song)
btn = Button(root, image=photo , command=play_song)
btn.pack()


root.mainloop() # infinte time the window to active all the time..


