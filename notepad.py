from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
def newFile():
    global file
    root.title("untitled-Notepad")
    file=None
    TextArea.delete(1.0,END)
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
     
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
    
    
   
def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Notepad by likhitha mahadev")


if __name__ == '__main__':
    root = Tk()        #basic tkinter set up 
    root.title("Untitles - Notepad")
    root.wm_iconbitmap("C:/Users/LIKITHA M/Downloads/notepad.png")
    root.geometry("644x788")
  
  #textarea
TextArea = Text(root, font="Arial 14")
file=None
TextArea.pack(expand=True, fill='both')
   
   #menubar
MenuBar = Menu(root)
FileMenu = Menu(MenuBar,tearoff=0)
   
   #to open new file
FileMenu.add_command(label="new",command=newFile)
   
   # to open existing file
FileMenu.add_command(label="open",command=openFile)
   
   #to save the current file
FileMenu.add_command(label="save",command=saveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit",command=quitApp) 
MenuBar.add_cascade(label="File",menu=FileMenu)

   #edit menu starts
EditMenu=Menu(MenuBar,tearoff=0)
   
   #cut ,copy & paste
EditMenu.add_command(label="Cut",command=cut)
EditMenu.add_command(label="Copy",command=copy)
EditMenu.add_command(label="Paste",command=paste)   
   
MenuBar.add_cascade(label="Edit",menu=EditMenu)
   
   
   #help menu starts
   
HelpMenu=Menu(MenuBar,tearoff=0)
   
HelpMenu.add_command(label="about notepad",command=about)
MenuBar.add_cascade(label="help",menu=HelpMenu)
   
   
   
root.config(menu=MenuBar)
   #adding scorllbar
Scroll=Scrollbar(TextArea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)   
   
root.mainloop()