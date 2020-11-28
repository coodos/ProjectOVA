# hi soham LOL

import difflib 

class lowerUtils: 

    @staticmethod
    def fuzzyCompare(string, lst): 

        highest = None
        highesRatio = 0
        
        for word in lst:
            ratio = difflib.SequenceMatcher(None, word, string).ratio()
                        
            if ratio > highesRatio:
                highesRatio = ratio
                highest = word
            
        return highest


if __name__ == "__main__": 
    lowerUtils.fuzzyCompare('hello', ['hola', 'halo', 'hallo'])
