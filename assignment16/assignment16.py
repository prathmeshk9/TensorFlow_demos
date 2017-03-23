from Tkinter import *
 
master = Tk()
 
def callback():
    print "Button click Event called!"
 
b = Button(master, text="Hello World !", command=callback)
b.pack()
 
mainloop()