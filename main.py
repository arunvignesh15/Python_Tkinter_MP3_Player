# Import libraries
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
import os

# Make the Window...
root = Tk()  # Open the Window
mixer.init()  # Initializing the mixer

# Create MenuBar
menubar = Menu(root)
root.config(menu=menubar)

# Create the Submenu
subMenu = Menu(menubar, tearoff=0)

def browseFile():
    global filename
    filename = filedialog.askopenfile()
    print(filename)


menubar.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label="Open", command=browseFile)
subMenu.add_command(label="Exit", command=root.destroy)  # Destroy the Tkinter Window by clicking the Exit Button


# Add the details of About US
def about_us():
    tkinter.messagebox.showinfo("About Melody", "This is a Music App developed by @Arun Vignesh by using Tkinter ")


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)

#root.geometry("300x300")  # Increase the size of the window, i will be bigger
root.title("Melody")  # Title of the Project
root.iconbitmap(r"favicon.ico")  # Add image to the Title bar

#################### Adding Widgets ##########################


# Add Text Data Field...
text = Label(root, text="Lets make some noise!...")  # Add the widget text, act as container to add image
text.pack(pady=10)  # just pack the text to keep them


# Add Picture...
# photo = PhotoImage(file="play.png")               # Add image in the Tkinder
# photolabel = Label(root, image=photo)               # Specfiy image= is need to be added
# photolabel.pack()                                   # just pack the text to keep them

# Add Button function...
def play_song():

    try:
        paused # check whether the pause variable is initialized or not
    except: # If not initialized then execute the code under the except conditions
        try:
            # mixer.music.load(r"Ellu Vaya Pookalaye.mp3")
            mixer.music.load(filename)
            mixer.music.play()
            statusBar['text'] = "Playing Music" + ' : ' + os.path.basename(filename.name)
            print("The Loop for Song is Working!...")
        except:
            tkinter.messagebox.showerror("Error", "Please check whether the Song is added or not")
            print("Error")
    else: # if initialized it goes to the else condition
        mixer.music.unpause()
        statusBar['text'] = "Music Resumed"

def pause_song():
    global paused # Once the Pause button is being clicked the song will be Paused by assigning the pause globally
    paused = True
    mixer.music.pause()
    statusBar['text'] = "Music Paused"

# Stop the Music
def stop_song():
    mixer.music.stop()
    statusBar['text'] = "Music Stopped"

def rewind_song():
    mixer.music.rewind()
    statusBar['text'] = "Music Rewind"

# Mute the Music
muted=FALSE
def mute_music():
    global muted
    if muted:
        #Unmute the music
        pass
        mixer.music.set_volume(0.7)
        volumeBtn.configure(image=volumePhoto)
        scale.set(70)
        muted = FALSE
        statusBar['text'] = "Music Unmted"
    else:
        #mute the music
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted= TRUE
        statusBar['text'] = "Music Muted"


# Adjust the Volume Button
def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(
        volume)  # Set the volume can take the values between 0 to 1, thats why we divide with 100 after casting the String into int

# Creating Frame in between, grouping the icons.
middleFrame = Frame(root, relief=RAISED, borderwidth=1)
middleFrame.pack(padx=40, pady=10)

# Play Button
# btn = Button(root, text="Play the Song!", command=play_song)
photo = PhotoImage(file="play.png")
#btn = Button(root, image=photo, command=play_song)  # once clicked it will find the function play_song function
btn = Button(middleFrame, image=photo, command=play_song)  # once clicked it will find the function play_song function
#btn.pack(side=LEFT,padx=10)
btn.grid(row=0,column=0,padx=10)

# Pause Button
pausePhoto = PhotoImage(file="pause.png")  # Add the Pause button
#pausebtn = Button(root, image=pausePhoto, command=pause_song) # Once its be clicked, the puase_song function will be activated
pausebtn = Button(middleFrame, image=pausePhoto, command=pause_song) # Once its be clicked, the puase_song function will be activated
#pausebtn.pack(side=LEFT,padx=10)
pausebtn.grid(row=0,column=1,padx=10)


# Stop Button
stopPhoto = PhotoImage(file="stop.png") # Add the Stop Button
#stopbtn = Button(root, image=stopPhoto, command=stop_song)
stopbtn = Button(middleFrame, image=stopPhoto, command=stop_song)
#stopbtn.pack(side=LEFT,padx=10)
stopbtn.grid(row=0,column=2,padx=10)

# Bottom Grid
bottomFrame = Frame(root, relief=RAISED, borderwidth=1)
bottomFrame.pack(padx=50, pady=10)


# Adding Rewind button
rewindPhoto = PhotoImage(file="rewind.png")  # Add the Pause button
#pausebtn = Button(root, image=pausePhoto, command=pause_song) # Once its be clicked, the puase_song function will be activated
rewindbtn = Button(bottomFrame, image=rewindPhoto, command=rewind_song) # Once its be clicked, the puase_song function will be activated
#pausebtn.pack(side=LEFT,padx=10)
#rewindbtn.pack(row=0,column=1,padx=10)
rewindbtn.grid(row=0,column=0,padx=20)


# Adding Mute button
mutePhoto = PhotoImage(file="mute.png")

volumePhoto = PhotoImage(file="sound.png")

volumeBtn = Button(bottomFrame, image=volumePhoto, command=mute_music)
volumeBtn.grid(row=0,column=2,padx=15)
# Volume Control
scale = Scale(bottomFrame, from_=0, to=100, orient=HORIZONTAL,
              command=set_vol)  # scale function to adjust the volume, Orient is Horizontal
# by default its a Vertical
scale.set(70)
mixer.music.set_volume(0.7)
scale.grid(row=0,column=1,pady=15)

# Add a status bar
statusBar = Label(root,text="Welcome to Melody", relief=SUNKEN, anchor = W)
statusBar.pack(side=BOTTOM, fill=X)

root.mainloop()  # infinte time the window to active all the time..
