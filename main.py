# builtins
import json
import os
import sys
import subprocess
import threading
import difflib

# outcasts
import bs4
import duckduckpy as doge # for ze MayMays B)
import pyttsx3
import requests
import speech_recognition as Recognizer
import urbandictionary as ud
from youtubesearchpython import SearchVideos
import pychromecast
from pychromecast.controllers.youtube import YouTubeController

# homies
import dictionaryAPI as dictAPI
from winApps import winapps
import chromecastchecker as ccc
from lowerUtils import lowerUtils as lU 
from newsApi import news as newsApi

# One Class to rule em all
# One Class to find them 
# One Class to bring them all 
# in the darkness and bind them 

class voiceCommands: 

    # this class deals with launching windows apps 
    # that are installed onto thy systeme 

    class news: 

        def __init__(self, arg, fullcmd):
            print('here')
            print(newsApi.getNews())
            utilities.SpeakText(newsApi.getNews())
        

    class win:

        class launchThread: 

            def __init__(self, app):
                try:
                    self.thread = threading.Thread(target=winapps.launch, args=(app, )) 
                    self.thread.daemon = True
                    self.thread.start()
                except Exception: 
                    utilities.SpeakText(f"Oops I ran into an issue, I am unable to launch {app} at the moment")

        def __init__(self, app, fullcmd):
            utilities.SpeakText(f"Opening {app}")
            voiceCommands.win.launchThread(winapps.searchForApp(app))
            
        

    # this class is for the sole purpose of todos 
    # probably the largest subclass yet * G U L P S * 

    class toDo: 

        # initialise a todos object and process 
        # the voice command that voice provided 
        # by it's masters

        def __init__(self, task, fullcmd):
            print(f"todo {task}")
            self.task = task
            self.fullcmd = fullcmd
            self.processTodo()

        # scan the todos.json file and see that 
        # what on earth are the person's to dos 

        @staticmethod
        def listToDos(lst = ''): 
            print("listing")

            try: 
                with open("todos.json", 'a+') as jsonFile: 
                    jsonFile.seek(0)
                    utilities.SpeakText("you have the to dos. ")
                    for todo in json.load(jsonFile)['todos']: 
                        utilities.SpeakText(todo) 

            except json.decoder.JSONDecodeError:
                utilities.SpeakText("it seems that you don't have anything to do! enjoy your day!")    
    
        # listen to the to dos on voice 
        # and then add the to dos to the 
        # todos.json file and if it doesn't 
        # exist then heck create one smh

        @staticmethod
        def addToDos(task): 
            try: 
                with open('todos.json', 'r') as jsonFile: 
                    out = {}
                    todos = json.load(jsonFile)["todos"]
                    todos.append(task.strip())
                    out["todos"] = todos
                os.remove("todos.json")
                utilities.writeToJson(out, "todos.json")
            except Exception as e:
                print(e) 
                try: 
                    os.remove("todos.json")
                except Exception:
                    pass
                todos = {"todos" : []}
                todos["todos"].append(task.strip())
                utilities.writeToJson(todos, "todos.json")
            finally: 
                utilities.SpeakText(f"Added the to do, {task}")

        # remove the lonely todo that has been used 
        # poor lil to do was emotionally tortured :(
        
        @staticmethod
        def remove(task):
            with open("todos.json", 'r') as jsonFile:
                data = json.load(jsonFile)
            try: 
                data["todos"].pop(data["todos"].index(task.strip()))
                os.remove("todos.json")
                utilities.writeToJson(data, 'todos.json')
                utilities.SpeakText(f"Removed to do, {task}")
            except Exception as e:
                print(e) 
                utilities.SpeakText("I can't seem to find that task")

        # perform a mass genocide of todos OwO

        @staticmethod
        def removeAll(lst):
            try: 
                os.remove("todos.json")
            except FileNotFoundError: 
                utilities.SpeakText("You don't seem to have any thing to do ")
            finally: 
                utilities.SpeakText("Removed all todos")

        # the dreaded SCUFFED NLP UwU

        def processTodo(self):             

            todoCommands = {
                "list": [
                    'what are my to dos',
                    'what are the things to do', 
                    'show my to dos', 
                    'list my to dos',
                    'things to do', 
                    {
                        'command': voiceCommands.toDo.listToDos
                    }
                ], 
                "add": [
                    'add to my to dos',
                    'add to do',
                    'at to do',
                    {
                        'command': voiceCommands.toDo.addToDos
                    }
                ], 
                "done": [
                    'mark as done',
                    'remove to do', 
                    'done to do ',
                    {
                        'command': voiceCommands.toDo.remove
                    }
                ], 
                "removeAll": [
                    'remove all', 
                    'remove all to dos',
                    'remove all to do', 
                    'mark all to do as done', 
                    'done all to dos', 
                    'remove all to do', 
                    'remove all two doors', 
                    'done all to do', 
                    'dun all to dos', 
                    'done all', 
                    'dun all',
                    'remove all tuduz',
                    'remove all todos',
                    {
                        'command': voiceCommands.toDo.removeAll
                    }
                ]
            }

            for command in todoCommands: 
                try: 
                    for cmd in todoCommands[command]: 
                        if cmd in self.fullcmd:
                            try: 
                                task = utilities.greaterOf(self.task.split('cmd')[0], self.task.split('cmd')[1])
                                todoCommands[command][-1]['command'](task)  
                            except IndexError: 
                                task = self.task.split('cmd')[0]
                                todoCommands[command][-1]['command'](task)     
                except TypeError: 
                    pass 



    class dictionary: 

        # use the scalper thing I made in the dictionaryAPI.py
        # and use its function to get the meaning of the word
        # requested by it's masters ^ \\\ ^

        def __init__(self, word, fullcmd): 
            print(f'searching for the meaning of {word}')
            self.word = word
            self.meaning = dictAPI.getMeaning(word)
            if self.meaning: 
                utilities.SpeakText(f'the meaning of {self.word} is, {self.meaning}')
            else: 
                utilities.SpeakText("hmmmmmmmmmm, I don't know that word")

    class youtubeSearch:

        # search ze zutube for content 
        # then play the content B)

        def __init__(self, keyword, fullcmd):
            self.keyword = keyword
            try:
                results = SearchVideos(keyword, offset = 1, mode = "dict", max_results = 1)

                # driver = webdriver.Chrome()
                # driver.get(results.result()['search_result'][0]['link'])
                url = results.result()['search_result'][0]['link']
                if sys.platform=='win32':
                    os.startfile(url)
                elif sys.platform=='darwin':
                    subprocess.Popen(['open', url])
                else:
                    try: 
                        subprocess.Popen(['xdg-open', url])
                    except OSError:
                        utilities.SpeakText("You ran into browser issue")
            except Exception as e:
                print(e)
            

    class searchWeb: 

        # use the doge, sorry duckduckgo API to 
        # get the top result and speak that 

        def __init__(self, keyword, fullcmd):
            self.keyword = keyword  
            print(f"searching for {keyword}")
            try:
                response = doge.query(keyword)
                utilities.SpeakText(f'top result on internet says that, {response.related_topics[0].text}')
            except IndexError: 
                pass

    class googleCast:

        def __init__(self, device, fullcmd):
            print('Reached atleast here....')
            self.connection = False
            self.processCmd(fullcmd)

        def connect(self):
            try:
                self.chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[self.device])
                print('reached here')
                utilities.SpeakText('Connection succeeded!')
                self.connection = True
            except Exception as e:
                utilities.SpeakText(f'{e}')

        def concheck(self):
            while True:
                if self.chromecasts:
                    continue
                else:
                    utilities.SpeakText('Connection Broke!')
                    self.connection = False
                    return

        def processCmd(self, fullcmd):
            cmd = fullcmd.split('cast')
            cmdlets = ['to my device', 'on the device', 'on device', 'to device']
            print('reached to processing')
            for cmdlet in cmdlets:
                print(cmdlet, cmd)
                cmd = sorted(cmd)[-1]
                if cmdlet in cmd:
                    deviceName = cmd.split(cmdlet)[1]
                    self.cccComparator(deviceName)
                    url = self.searchVid(cmd.split(cmdlet)[0])    
                    if self.connection == False:
                        self.connect() 

                    vidId = url.split("?v=")[-1].split("&")[0]
                    self.playContent(vidId)           
            

        def playContent(self, videoID):
            print("video shud play but won't :(")
            cast = self.chromecasts[0]
            cast.wait()
            yt = YouTubeController()
            cast.register_handler(yt)
            yt.play_video(videoID)

        def searchVid(self, keyword):
            results = SearchVideos(keyword, offset = 1, mode = "dict", max_results = 1)
            url = results.result()['search_result'][0]['link']
            return url        

    
        def cccComparator(self, device):
            with open('cache/chromecast.txt', 'r+') as f:
                shit = f.readlines()
                newshit=[]
                for element in shit:
                    newelement = element[0:-1]
                    newshit.append(newelement)
                f.close()
            print(newshit)
            self.device = (lU.fuzzyCompare(device, newshit))


    class urban: 

            # urban dictionary OwO

        def __init__(self, word, fullcmd): 
            print(f"searching for {word}")
            self.word = word
            try:
                self.meaning = ud.define(word)[0].definition
                utilities.SpeakText(f"according to urban dictionary, {word} means {self.meaning}")
            except Exception: 
                utilities.SpeakText(f"oof, stupid urban dictionary doesn't even know the meaning of {word}.")
            
# Scuffed Natural Language Processing 
# this class is gonna be * H E C T I C *

class naturalLanguage: 

    # so basically ughh I would 
    # initialize some shit here and
    # then we would convert it to command
    # please end this fast ;_;

    # a dictionary of commands to figure out 
    # that the hell is the thing that the voice 
    # assistant is asked to bloody do

    commands = {
        'dictionary' : [
            'what is the meaning of ', 
            'meaning of ', 
            'what is the definition of', 
            'what is ',
            'define ',
            {
                'command': voiceCommands.dictionary
            }
        ], 
        'web': [
            'search the web for',
            'search the web',
            {
                'command': voiceCommands.searchWeb
            }
        ],
        'urban': [ 
            'urban dictionary',
            {
                'command': voiceCommands.urban
            } 
        ],
        'toDo': [
            'to do',
            'to dos',
            'todo', 
            'todos',
            {
                'command': voiceCommands.toDo
            }
        ],        
        'youtube':[
            'search youtube for',
            'search on youtube for',
            'search youtube',
            'search yt',
            {
                'command': voiceCommands.youtubeSearch
            }
        ],
        'connect': [
            'connect to',
            'cast',
            'cast to',
            {
                'command': voiceCommands.googleCast
            }
        ],
        'win': [
            'open the app', 
            'launch ', 
            'open ',
            'run ',  
            {
                'command': voiceCommands.win
            }
        ],
        'news': [
            'get news', 
            'latest news', 
            'news flash', 
            'what is happing',
            'get headlines',
            {
                'command': voiceCommands.news
            }
        ]    
    }


    def __init__(self, command, trigger):

        self.command = command
       
        for command in list(self.__class__.commands.keys()):
            try: 
                for cmd in self.__class__.commands[command]: 
                    if cmd in self.command:
                        try: 
                            self.command = self.command.split(trigger, 1)[1]
                            argument = utilities.greaterOf(self.command.split(cmd, 1)[0], self.command.split(cmd, 1)[1])
                        except IndexError: 
                            argument = self.command.split(command, 1)[0] 
                        finally: 
                            self.__class__.commands[command][-1]['command'](argument, self.command)       
            except TypeError: 
                pass
  
# class related to utilites. 
# primarily contains static methods

class utilities: 

    @staticmethod
    def startSlaves():
        chromecastchecker = threading.Thread(target=ccc.check, args=())
        chromecastchecker.daemon = True
        chromecastchecker.start()

    # this static method is for checking
    # which of the two arguments is greater

    @staticmethod   
    def greaterOf(arg1, arg2, category="str"):
        if category == "str": 
            if len(arg1) > len(arg2):
                return arg1
            else: 
                return arg2

        elif category == "int": 
            if arg1 > arg2: 
                return arg1
            else: 
                return arg2

    # speak text that has been passed :) 
    
    @staticmethod
    def SpeakText(command):       
        engine.say(command)  
        engine.runAndWait() 

    # write stuff to json, what else did you think this would do LMAO

    @staticmethod
    def writeToJson(data, file = "settings.json"): 
        with open(file, 'a+') as f: 
            json.dump(data, f)

    # reset settings

    @staticmethod
    def runConfigurator():
        try: 
            os.remove("settings.json")
        except Exception: 
            pass
        settings = {}
        triggerWord = input("what would you like your personal assistant to be called ?\n--> ")
        settings['trigger'] = triggerWord    
        print("\n==============================================================\n")
        for index, name in enumerate(Recognizer.Microphone.list_microphone_names()):
            print(f" [ devide id : {index} ] {name} ")
        print("\n==============================================================\n")
        device_id = input("enter device id of the microphone you would like to use\n--> ")
        settings["micID"] = device_id
        print("\n==============================================================\n")
        gender = input('What gender would you like your assistant to sound like?\n[ m ] Male\n[ f ] Female\n\n--> ')
        settings["gender"] = gender
        utilities.writeToJson(settings)       



if __name__ == "__main__":

    # so here we start the shitty recognizer
    # code totally not stolen from GeeksForGeeks
    # :sweatsmile: 
    recognizer = Recognizer.Recognizer()  
    engine = pyttsx3.init() 
    engine.setProperty('rate', 140)
    
    def main():

        utilities.startSlaves()

        # read the config which has already been defined 
        # and use bloody use that LOL
        try: 
            with open('settings.json', 'r') as settingsFile: 
                settings = json.load(settingsFile)
                triggerWord = settings["trigger"]
                micId = int(settings["micID"])
                voiceGender = settings['gender']
        except KeyError or json.decoder.JSONDecodeError: 
            print("your local configuration appears to have been corrupted")
            print("Press [y] to continue with resseting your voice assistant or [n] to cancel")
            inp = input("--> ")
            if inp.lower().strip() == "y": 
                utilities.runConfigurator()
                main()
            elif inp.lower().strip() == "n":
                sys.exit()
            else: 
                print("ALERT : invalid input\n")
                main()
        
        # setting a female voice 
        voices = engine.getProperty('voices')   
        if voiceGender == "m":                
            engine.setProperty('voice', voices[0].id)
        elif voiceGender == "f": 
            engine.setProperty('voice', voices[1].id)         
    

        while True: 
            
            try: 
                # { mic ---> google api ---> text } ==> STONKS        
                # ^ /// ^      
                with Recognizer.Microphone(device_index=micId) as source: 
                    recognizer.adjust_for_ambient_noise(source, duration=0.1)  
                    audio = recognizer.listen(source) 
                    MyText = recognizer.recognize_google(audio) 
                    MyText = MyText.lower()
                    print(MyText)
                    if triggerWord in MyText: 
                        naturalLanguage(MyText, triggerWord)

            # ignore errors like a good programmer LMAO
            # it's all in ze mind
            except Recognizer.RequestError: 
                pass     

            # ignore errors like a good programmer LMAO
            # it's all in ze mind
            except Recognizer.UnknownValueError: 
                pass

    if "settings.json" in os.listdir():
        main()       
    
    else: 
        utilities.runConfigurator()
        main()