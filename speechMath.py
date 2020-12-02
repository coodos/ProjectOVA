class speechMath:    

    @staticmethod
    def extractNums(string):
        isDigitList = []
        for word in string.split(' '):
            if word.replace('.', '').isdigit():
                isDigitList.append(word)
        return isDigitList 

    @staticmethod
    def multiply(number1, number2):
        return (f'Multiplying {number1} by {number2} gives result {number1 * number2}')
    
    @staticmethod
    def divide(number1, number2):
        return (f'{number1} divided by {number2} gives quotient {number1/number2}')
        

    @staticmethod
    def addition(number1, number2):
        return (f'{number1} added to {number2} gives sum {number1 + number2}')

    @staticmethod
    def subtraction(number1, number2):
        return (f'{number2} subracted from {number1} gives {number1 - number2}')

    @staticmethod
    def remainder(number1, number2):
        return (f'remainder on dividing {number1} by {number2} is {number1 % number2}')

    @staticmethod
    def exponents(number1, number2):
        return (f'{number1} raised to {number2} is {number1 ** number2}')

    def __init__(self, fullCommand):

        speechMathFunctions = {
            'divide' : speechMath.divide, 
            'multiply': speechMath.multiply,
            'add': speechMath.addition, 
            'subtract': speechMath.subtraction,
            'exponent': speechMath.exponents,
            'remainder of': speechMath.remainder
        } 

        for command in speechMathFunctions.keys():
            if command in fullCommand.split(' '):
                print(command, fullCommand)
                nums = speechMath.extractNums(fullCommand)
                try:
                    self.answer = speechMathFunctions[command](float(nums[0]), float(nums[1]))
                except ZeroDivisionError: 
                    self.answer = "Imagine that you have zero cookies and you split them evenly among zero friends. How many cookies does each person get? See? It doesn't make sense. And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends."
                except IndexError: 
                    self.answer = "Some error occured, please try again"
               
    def getAnswer(self):
        return self.answer

if __name__ == "__main__":
    a = speechMath('multiply 2 and 2')
    b = speechMath('add 3 and 2')
    c = speechMath('subtract 3 from 2')
    d = speechMath('divide 2 by 1')
    e = speechMath('remainder of 3 divided by 3')
    f = speechMath('2 raised to the power 5')