import speech_recognition as Recognizer
import pyttsx3  
import urbandictionary as ud
 

# One Class to rule em all
# One Class to find them 
# One Class to bring them all 
# in the darkness and bind them 

class voiceCommands: 

    class toDo: 

        def __init__(self, task):
            self.task = task

    class dictionary: 

        def __init__(self, word): 
            self.word = word
            self.meaning = ud.define(word)[0].definition
            utilities.SpeakText(f'according to urban dictionary, the meaning of {self.word} is, {self.meaning}')
            

    class searchWeb: 

        def __init__(self, keyword):
            self.keyword = keyword
            print(keyword)


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
        'toDo': [
            'to do', 
            {
                'command': voiceCommands.toDo
            }
        ]
    }


    def __init__(self, command):

        self.command = command
        
        try:
            for command in self.__class__.commands:
                for cmd in self.__class__.commands[command]: 
                    if cmd in self.command:
                        try: 
                            argument = utilities.greaterOf(self.command.split(cmd)[0], self.command.split(cmd)[1])
                        except IndexError: 
                            argument = self.command.split(command)[0] 
                        finally: 
                            self.__class__.commands[command][-1]['command'](argument)
                        break
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


if __name__ == "__main__":

    # so here we start the shitty recognizer
    # code totally not stolen from GeeksForGeeks
    # :sweatsmile: 
    
    recognizer = Recognizer.Recognizer()  
    engine = pyttsx3.init() 
    # setting a female voice 
    voices = engine.getProperty('voices')      
    engine.setProperty('voice', voices[1].id)   
    engine.setProperty('rate', 140)

    while True: 

        try: 
            # { mic ---> google api ---> text } ==> STONKS        
            # ^ /// ^      
            with Recognizer.Microphone() as source: 
                recognizer.adjust_for_ambient_noise(source, duration=0.2)  
                audio = recognizer.listen(source) 
                MyText = recognizer.recognize_google(audio) 
                MyText = MyText.lower()
                naturalLanguage(MyText)

        # ignore errors like a good programmer LMAO
        # it's all in ze mind
        except Recognizer.RequestError: 
            pass     

        # ignore errors like a good programmer LMAO
        # it's all in ze mind
        except Recognizer.UnknownValueError: 
            pass