from tkinter import *
from tkinter.filedialog import askdirectory
import os 

class guiMethods():

    dirNum = 0

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

        for r, d, f in os.walk(loc):
            for file in f:
                filePath = os.path.join(r, file)                
                if file == fileName: 
                    print(filePath, 'found')
                    os.startfile('/'.join(filePath.split('\\')[:-1]))
                    root.destroy() 

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