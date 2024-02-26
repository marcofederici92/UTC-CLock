
from tkinter import *
import time
from tkinter import messagebox
from webbrowser import *
root = Tk()

root.resizable()
root.title('Python Clock')
root.attributes('-topmost',True) #sempre in primo piano
root.overrideredirect(True)      #mostra solo il contenuto togliendo la finestra




lastClickX = 0
lastClickY = 0

def repositioning(event):
    x1=0
    y1=0
    root.geometry("+%s+%s" % (x1 , y1))

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , y))



def on_closing(event):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        print(event)


def watch():
    string = time.strftime("%H:%M:%S", time.gmtime())
    mark.config(text = string)
    mark.after(1000, watch)
mark = Label(root, 
            font = ('Microsoft Sans Serif', 7),
            foreground = 'yellow',
            relief="ridge",
            background='black')
mark.pack(anchor = 'center')

watch()
root.bind('<Button-2>', repositioning)
root.bind('<Button-1>', SaveLastClickPos)
root.bind('<Button-3>', on_closing, )
root.bind('<B1-Motion>', Dragging)



root.mainloop()


"""version 1.0.0 
    powered by trebbia92
    30/03/2022"""