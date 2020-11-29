import pytube
import os
import moviepy.editor as moviepy
from playsound import playsound
import multiprocessing
import time

class youtubeAudio: 

    processNodes = []

    def __init__(self, link):
        try: 
            os.mkdir('temp')
        except FileExistsError: 
            pass
        self.localName = utilities.getName(pytube.YouTube(link).title)
        
        if f'{self.localName}.mp3' in os.listdir("./temp/"):
            self.sound = multiprocessing.Process(target=self.playAudio, args=(self, ))
            self.__class__.processNodes.append(self.sound)
            self.sound.start()

        else:

            self.audio = pytube.YouTube(link).streams.filter(progressive=True).order_by('resolution').first()
            self.audio.download('./temp/', filename=self.localName)
            # Insert Local Video File Path  
            clip = moviepy.VideoFileClip(f"./temp/{self.localName}.mp4")         
            # Insert Local Audio File Path 
            clip.audio.write_audiofile(f"./temp/{self.localName}.mp3") 

            clip.close()

            os.remove(f"./temp/{self.localName}.mp4")
            self.sound = multiprocessing.Process(target=self.playAudio, args=(self, ))
            self.__class__.processNodes.append(self.sound)
            self.sound.start()

    def playAudio(self, arg):
        playsound(f'./temp/{self.localName}.mp3')


    def killSong(self):
        self.sound.terminate()

    @classmethod
    def killAll(cls): 
        for process in cls.processNodes: 
            process.terminate()


class utilities:

    @staticmethod
    def getName(name):
        outputName = ''
        for char in name: 
            if ord(char.lower()) in range(97, 122) or char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                outputName += char
            if char == " ":
                outputName += "_"
        return outputName

if __name__ == "__main__":
    yt = youtubeAudio("https://www.youtube.com/watch?v=SutNw462mxU")
    time.sleep(10)
    youtubeAudio.killAll()