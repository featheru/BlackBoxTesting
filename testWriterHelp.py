"""
Automatically writes out different test cases by parsing .tsl file

"""

class AutomatedTestCaseGenerator:

    def __init__(self):
        self.testCaseList = []
        self.currTestCase = ""
        self.currPrefix = ""
        self.currLength = -1  #append at this point
        self.currCCNum = ""

    def testWriter(self):
        for idx in range(len(self.testCaseList)):
            testCase = self.testCaseList[idx][0]
            prefix = self.testCaseList[idx][1]
            length = self.testCaseList[idx][2]
            ccNum = self.testCaseList[idx][3]

            print(f"def testCase{testCase}(self):\n" + \
            f"\t# Test Case: {testCase}; Prefix: {prefix}; Length: {length}, CCNum: {ccNum}\n" + \
            f"\tccnum = \"{ccNum}\"\n" + \
            "\tself.assertTrue(credit_card_validator(ccNum), msg=getErrorMessage(ccNum))\n" + \
            "\n")
            
            

    def GenerateCC(self, prefix, length):
        newCC = ""
        newCC += prefix
        counter = 0
        while len(newCC) != length:
            if str(counter) not in prefix:
                newCC += str(counter)
            counter = (counter + 1) % 10
        return newCC

    def AppendString(self, testCase, prefix, length):
        ccNum = self.GenerateCC(prefix, length)
        self.testCaseList.append([testCase,prefix,length,ccNum]);

    def getDigits(self,line):
        newStr = ""
        for letter in line:
            if letter.isdigit():
                newStr += letter
        return newStr

    def getTestCaseDigits(self,line):
        newStr = ""
        for letter in line:
            if letter.isdigit():
                newStr += letter
            elif letter == "K":
                return newStr
        return newStr

    def getTestCases(self):
        #parse cc.spec.tsl line by line
        with open('cc.spec.tsl') as specFile:
            for line in specFile.readlines():
                if "Test Case" in line:
                    currTestCase = self.getTestCaseDigits(line)
                    
                if "Prefix" in line:
                    currPrefix = self.getDigits(line)

                if "Length" in line:
                    currLength = int(self.getDigits(line))
                    self.AppendString(currTestCase, currPrefix, currLength)
        return self.testWriter()

if __name__ == '__main__':
    AutomatedTestCaseGenerator().getTestCases()
