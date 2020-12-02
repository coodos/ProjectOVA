from tkinter import *
from tkinter.filedialog import askdirectory
import os 

class guiMethods():

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

        dirs = []

        for r, d, f in os.walk(loc):
            for file in f:
                filePath = os.path.join(r, file)                
                if file == fileName: 
                    print(filePath, 'found')
                    dirs.append('/'.join(filePath.replace('\\', '/').split('/')[:-1]))
                    root.destroy() 
                    if dirs != []:
                        guiMethods.makeDirsPopup(dirs)

    @staticmethod
    def nextDir(dirs, currLabel):
        pass

    @staticmethod
    def makeDirsPopup(dirs):
        window = Tk()
        window.geometry('400x300')
        window.title('Found File in Dirs')

        dirLabel = Label(window, text=dirs[0])
        dirLabel.pack(pady=10, padx=10)
        nextButton = Button(window, text='next', command=guiMethods.nextDir(dirs, dirLabel['text']), width=25)
        nextButton.pack()



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