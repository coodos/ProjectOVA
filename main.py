# builtins
import json
import os
import sys

# outcasts
import bs4
import duckduckpy as doge
import pyttsx3
import requests
import speech_recognition as Recognizer
import urbandictionary as ud

# homies
import dictionaryAPI as dictAPI

# One Class to rule em all
# One Class to find them 
# One Class to bring them all 
# in the darkness and bind them 

class voiceCommands: 

    class toDo: 

        def __init__(self, task):
            self.task = task
            self.processTodo()

        def processTodo(): 
            todoCommands = {
                "list": [
                    'what are my to dos',
                    'what are the things to do', 
                    'show my to dos', 
                    'list my to dos',
                    'things to do'
                ], 
                "add": [
                    'add to my to dos',
                    'add to do'
                ], 
                "done": [
                    'mark as done',
                    'remove to do', 
                    'done to do '
                ]
            }

    class dictionary: 

        def __init__(self, word): 
            print(f'searching for the meaning of {word}')
            self.word = word
            self.meaning = dictAPI.getMeaning(word)
            if self.meaning: 
                utilities.SpeakText(f'the meaning of {self.word} is, {self.meaning}')
            else: 
                utilities.SpeakText("hmmmmmmmmmm, I don't know that word")
            

    class searchWeb: 

        def __init__(self, keyword):
            self.keyword = keyword  
            print(f"searching for {keyword}")
            try:
                response = doge.query(keyword)
                utilities.SpeakText(f'top result on internet says that, {response.related_topics[0].text}')
            except IndexError: 
                pass

    class urban: 

        def __init__(self, word): 
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
            'search ',
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
            {
                'command': voiceCommands.toDo
            }
        ]        
    }


    def __init__(self, command, trigger):

        self.command = command
       
        for command in list(self.__class__.commands.keys()):
            try: 
                for cmd in self.__class__.commands[command]: 
                    if cmd in self.command and trigger in self.command:
                        try: 
                            self.command = self.command.split(trigger)[1]
                            argument = utilities.greaterOf(self.command.split(cmd)[0], self.command.split(cmd)[1])
                        except IndexError: 
                            argument = self.command.split(command)[0] 
                        finally: 
                            self.__class__.commands[command][-1]['command'](argument)       
            except TypeError: 
                pass
  
# class related to utilites. 
# primarily contains static methods

class utilities: 

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

    @staticmethod
    def SpeakText(command):       
        engine.say(command)  
        engine.runAndWait() 

    @staticmethod
    def writeToJson(data, file = "settings.json"): 
        with open(file, 'a+') as f: 
            json.dump(data, f)

    @staticmethod
    def runConfigurator():
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
    
    def main():

        # read the config which has already been defined 
        # and use bloody use that LOL
        try: 
            with open('settings.json', 'r') as settingsFile: 
                settings = json.load(settingsFile)
                triggerWord = settings["trigger"]
                micId = int(settings["micID"])
                voiceGender = settings['gender']
        except KeyError: 
            print("your local configuration appears to have been corrupted")
            print("Press [y] to continue with resseting your voice assistant or [n] to cancel")
            inp = input("--> ")
            if inp.lower().strip() == "y": 
                utilities.runConfigurator()
            elif inp.lower().strip() == "n":
                sys.exit()
            else: 
                print("ALERT : invalid input\n")
                main()


        recognizer = Recognizer.Recognizer()  
        engine = pyttsx3.init() 
        # setting a female voice 
        voices = engine.getProperty('voices')   
        if voiceGender == "m":                
            engine.setProperty('voice', voices[0].id)
        elif voiceGender == "f": 
            engine.setProperty('voice', voices[1].id)   
        engine.setProperty('rate', 140)
    

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