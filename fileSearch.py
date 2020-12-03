from tkinter import *
from tkinter.filedialog import askdirectory
import os 

class guiMethods():

    dirnum = 0

    # get the directory
    @staticmethod
    def getPath():
        folder = askdirectory()
        return folder

    @staticmethod
    def processData():
        global fileNameEntry, root

        loc = guiMethods.getPath()
        print(loc)
        fileName = fileNameEntry.get()

        global dirs
        dirs = []

        for r, d, f in os.walk(loc):
            for file in f:
                filePath = os.path.join(r, file)                
                if file == fileName: 
                    print(filePath, 'found')
                    dirs.append('/'.join(filePath.replace('\\', '/').split('/')[:-1]))
        print(dirs)
        if dirs != []:
            root.destroy() 
            guiMethods.makeDirsPopup(dirs)

    @classmethod
    def nextDir(cls):
        global dirs, dirLabel
        try:
            dirLabel["text"] = dirs[cls.dirnum + 1]
            cls.dirnum += 1
        except IndexError:
            dirLabel["text"] = dirs[0]
            cls.dirnum = 0
    
    @classmethod
    def prevDir(cls):
        global dirs, dirLabel
        if cls.dirnum >= 1:
            dirLabel["text"] = dirs[cls.dirnum - 1]
            cls.dirnum -= 1
        else:
            dirLabel["text"] = dirs[len(dirs) - 1]
            cls.dirnum = len(dirs) - 1

    @classmethod
    def openFolder(cls):
        global dirs
        os.startfile(dirs[cls.dirnum])

    @classmethod
    def makeDirsPopup(cls, dirs):
        window = Tk()
        window.geometry('400x300')
        window.title('Found File in Dirs')

        Label(window, text="File found at", font=("arial", 30, "bold")).pack(pady=10, padx=10)

        global dirLabel
        dirLabel = Label(window, text=dirs[cls.dirnum])
        dirLabel.pack(pady=10, padx=10)
        nextButton = Button(window, text='next', command=guiMethods.nextDir, width=25, bg='#6d6d6d', fg='#fff')
        nextButton.pack()

        backButton = Button(window, text='back', command=guiMethods.prevDir, width=25, bg='#6d6d6d', fg='#fff')
        backButton.pack(padx=10, pady=10)

        openButton = Button(window, text='Open Folder', command=guiMethods.openFolder, width=25, bg='#3d3d3d', fg='#fff')
        openButton.pack(padx = 10, pady=10)

    # create the file dialog thing
    @staticmethod
    def fileSearch():
        global root
        root = Tk()
        root.geometry('600x400')
        root.title('Search File')
        
        global fileNameEntry
        Label(root, text="file to search", ).pack(pady=10, padx=10)
        fileNameEntry = Entry(root, width=25)
        fileNameEntry.pack()

        Label(root, text="Directory to search in").pack(pady=10, padx=10)
        browseButton = Button(root, text="Search", command=guiMethods.processData)
        browseButton.pack(pady=10, padx=10)

        root.mainloop()

if __name__ == "__main__":
    
    guiMethods.fileSearch()