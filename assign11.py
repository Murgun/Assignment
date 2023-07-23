from tkinter import *
from webbrowser import *

root = Tk(className= "gui")

Label(root).pack()
nameLabel = Label(root, text="Name:").pack()
userName = Entry(root).pack()
contactLabel = Label(root, text="Contact:").pack()
userContact = Entry(root).pack()
Label(root).pack()
questionLabel = Label(master = root, text= "Where did you see this Advertise ?", font=("Times new Roman",15)).pack()
userChoice = StringVar(root)
userChoice.set("Select an Option")
checkBox = OptionMenu(root, userChoice, "Youtube Ads", "Spotify Ads").pack()
Label(root).pack()
def submitOnClick():
    if userChoice.get() == "Spotify Ads":
        open("https://support.spotify.com/in-en/")
    elif userChoice.get() == "Youtube Ads":
        open("https://www.youtube.com/intl/en-GB/ads/")
    root.destroy()
submitButton = Button(root,text = "Submit",command = submitOnClick).pack()
Label(root).pack()

root.mainloop()