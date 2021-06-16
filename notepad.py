from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename , asksaveasfilename
import os

root=Tk()
root.geometry("500x500")
root.title("notepad")

# backend

def exit_1():
    root.destroy()

def about():
    messagebox.showinfo("About info","Currently unavailable")

def new_file():
    global file
    root.title("untitled notepad")
    file = None
    text_area.delete(1.0,END)

def open_file():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("text documents","*.txt")])

    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+ " - Notepad")    
        text_area.delete(1.0,END)
        f=open(file,"r")
        text_area.insert(1.0,f.read())
        f.close()      

def save_file():
    global file
    file = asksaveasfilename(initialfile = "Untitled.txt" , defaultextension = ".txt",
                                 filetypes = [("All Files" , "*.*"),("Text Documents",".txt")])


    if file == None :
        file = asksaveasfilename(initialfile = "Untitled.txt" , defaultextension = ".txt",
                                 filetypes = [("All Files" , "*.*"),("Text Documents",".txt")])

        if file == "":
            file = None
            
        else:
            f = open(file , "w")
            read_text_area = str(text_area.get(1.0 , END))
            f.write(read_text_area)
            f.close()
    else:
        print(file)
        f = open(file , "w")
        read_text_area = str(text_area.get(1.0 , END))
        f.write(read_text_area)
        f.close()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

# create menubar

menubar=Menu(root)

# create menu
# 1 - file menu

file=Menu(menubar,tearoff=0)

# add submenu to file menu

file.add_command(label="New file",command=new_file)
file.add_command(label="Open file",command=open_file)
file.add_command(label="Save file",command=save_file)

file.add_separator()

file.add_command(label="Exit",command=exit_1)

# configure menubar to main window

root.configure(menu=menubar)

# add menu to menubar

menubar.add_cascade(label="file",menu=file)
##############################################################

# 2 - Edit menu

edit=Menu(menubar,tearoff=0)

# add submenu to main menu

edit.add_command(label="cut",command=cut)
edit.add_command(label="copy",command=copy)
edit.add_command(label="paste",command=paste)
edit.add_command(label="undo")


# add menu to menubar

menubar.add_cascade(label="Edit",menu=edit)

##########################################################

# 3 - Help

help=Menu(menubar,tearoff=0)

help.add_command(label="About",command=about)
help.add_command(label="help")

# add menu to menubar

menubar.add_cascade(label="Help",menu=help)


# create scorll bar

sb = Scrollbar(root)
sb.pack(side = RIGHT  , fill = Y)


# create Text widgets

text_area = Text(root,font = ("arial 15") , yscrollcommand = sb.set)
text_area.pack(fill = BOTH , expand = YES)

#
sb.config(command = text_area.yview )


root.mainloop()


