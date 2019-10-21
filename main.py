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

root.geometry("300x300")  # Increase the size of the window, i will be bigger
root.title("Melody")  # Title of the Project
root.iconbitmap(r"favicon.ico")  # Add image to the Title bar

#################### Adding Widgets ##########################


# Add Text Data Field...
text = Label(root, text="Lets make some noise!...")  # Add the widget text, act as container to add image
text.pack()  # just pack the text to keep them


# Add Picture...
# photo = PhotoImage(file="play.png")               # Add image in the Tkinder
# photolabel = Label(root, image=photo)               # Specfiy image= is need to be added
# photolabel.pack()                                   # just pack the text to keep them

# Add Button function...
def play_song():
    try:
        # mixer.music.load(r"Ellu Vaya Pookalaye.mp3")
        mixer.music.load(filename)
        mixer.music.play()
        statusBar['text'] = "Playing Music" #+ ' ' + os.path.basename(filename)
        print("The Loop for Song is Working!...")
    except:
        tkinter.messagebox.showerror("Error", "Please check whether the Song is added or not")
        print("Error")


# Stop the Music
def stop_song():
    mixer.music.stop()
    statusBar['text'] = "Music Stopped"


# Adjust the Volume Button
def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(
        volume)  # Set the volume can take the values between 0 to 1, thats why we divide with 100 after casting the String into int


# Play Button
# btn = Button(root, text="Play the Song!", command=play_song)
photo = PhotoImage(file="play.png")
btn = Button(root, image=photo, command=play_song)  # once clicked it will find the function play_song function
btn.pack()

# Stop Button
stopPhoto = PhotoImage(file="stop.png")
stopbtn = Button(root, image=stopPhoto, command=stop_song)
stopbtn.pack()

# Volume Control
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL,
              command=set_vol)  # scale function to adjust the volume, Orient is Horizontal
# by default its a Vertical
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack()

# Add a status bar
statusBar = Label(root,text="Welcome to Melody", relief=SUNKEN, anchor = W)
statusBar.pack(side=BOTTOM, fill=X)

root.mainloop()  # infinte time the window to active all the time..
