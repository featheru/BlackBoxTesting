import unittest
from credit_card_validator import credit_card_validator

"""
Test Cases for Credit Card Validation 
Cases generated using TSL Generator
testCases written using testWriterHelp.py
File written to conform with PEP8
"""

def getErrorMessage(string):
  return 'Does not meet the requirements (credit Card # ={})'.format(string)

class TestCase(unittest.TestCase):
  def testCase1(self):
    #Test Case: 1; Prefix: 4; Length: 15, CCNum: 401235678901235
    ccNum = "401235678901235"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase2(self):
    #Test Case: 2; Prefix: 4; Length: 16, CCNum: 4012356789012356
    ccNum = "4012356789012356"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase3(self):
    #Test Case: 3; Prefix: 4; Length: 17, CCNum: 40123567890123567
    ccNum = "40123567890123567"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase4(self):
    #Test Case: 4; Prefix: 33; Length: 15, CCNum: 330124567890124
    ccNum = "330124567890124"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase5(self):
    #Test Case: 5; Prefix: 34; Length: 14, CCNum: 34012567890125
    ccNum = "34012567890125"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase6(self):
    #Test Case: 6; Prefix: 34; Length: 15, CCNum: 340125678901256
    ccNum = "340125678901256"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase7(self):
    #Test Case: 7; Prefix: 34; Length: 16, CCNum: 3401256789012567
    ccNum = "3401256789012567"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase8(self):
    #Test Case: 8; Prefix: 36; Length: 15, CCNum: 360124578901245
    ccNum = "360124578901245"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase9(self):
    #Test Case: 9; Prefix: 37; Length: 14, CCNum: 37012456890124
    ccNum = "37012456890124"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase10(self):
    #Test Case: 10; Prefix: 37; Length: 15, CCNum: 370124568901245
    ccNum = "370124568901245"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase11(self):
    #Test Case: 11; Prefix: 37; Length: 16, CCNum: 3701245689012456
    ccNum = "3701245689012456"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase12(self):
    #Test Case: 12; Prefix: 38; Length: 15, CCNum: 380124567901245
    ccNum = "380124567901245"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase13(self):
    #Test Case: 13; Prefix: 50; Length: 16, CCNum: 5012346789123467
    ccNum = "5012346789123467"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase14(self):
    #Test Case: 14; Prefix: 51; Length: 15, CCNum: 510234678902346
    ccNum = "510234678902346"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase15(self):
    #Test Case: 15; Prefix: 51; Length: 16, CCNum: 5102346789023467
    ccNum = "5102346789023467"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase16(self):
    #Test Case: 16; Prefix: 51; Length: 17, CCNum: 51023467890234678
    ccNum = "51023467890234678"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase17(self):
    #Test Case: 17; Prefix: 52; Length: 15, CCNum: 520134678901346
    ccNum = "520134678901346"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase18(self):
    #Test Case: 18; Prefix: 52; Length: 16, CCNum: 5201346789013467
    ccNum = "5201346789013467"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase19(self):
    #Test Case: 19; Prefix: 52; Length: 17, CCNum: 52013467890134678
    ccNum = "52013467890134678"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase20(self):
    #Test Case: 20; Prefix: 55; Length: 15, CCNum: 550123467890123
    ccNum = "550123467890123"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase21(self):
    #Test Case: 21; Prefix: 55; Length: 16, CCNum: 5501234678901234
    ccNum = "5501234678901234"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase22(self):
    #Test Case: 22; Prefix: 55; Length: 17, CCNum: 55012346789012346
    ccNum = "55012346789012346"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase23(self):
    #Test Case: 23; Prefix: 56; Length: 16, CCNum: 5601234789012347
    ccNum = "5601234789012347"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase24(self):
    #Test Case: 24; Prefix: 2220; Length: 16, CCNum: 2220134567891345
    ccNum = "2220134567891345"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase25(self):
    #Test Case: 25; Prefix: 2221; Length: 15, CCNum: 222103456789034
    ccNum = "222103456789034"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase26(self):
    #Test Case: 26; Prefix: 2221; Length: 16, CCNum: 2221034567890345
    ccNum = "2221034567890345"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase27(self):
    #Test Case: 27; Prefix: 2221; Length: 17, CCNum: 22210345678903456
    ccNum = "22210345678903456"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase28(self):
    #Test Case: 28; Prefix: 2222; Length: 15, CCNum: 222201345678901
    ccNum = "222201345678901"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase29(self):
    #Test Case: 29; Prefix: 2222; Length: 16, CCNum: 2222013456789013
    ccNum = "2222013456789013"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase30(self):
    #Test Case: 30; Prefix: 2222; Length: 17, CCNum: 22220134567890134
    ccNum = "22220134567890134"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase31(self):
    #Test Case: 31; Prefix: 2720; Length: 15, CCNum: 272013456891345
    ccNum = "272013456891345"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase32(self):
    #Test Case: 32; Prefix: 2720; Length: 16, CCNum: 2720134568913456
    ccNum = "2720134568913456"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase33(self):
    #Test Case: 33; Prefix: 2720; Length: 17, CCNum: 27201345689134568
    ccNum = "27201345689134568"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


  def testCase34(self):
    #Test Case: 34; Prefix: 2721; Length: 16, CCNum: 2721034568903456
    ccNum = "2721034568903456"
    self.assertTrue(credit_card_validator(ccNum),msg=getErrorMessage(ccNum))


if __name__ == '__main__':
  unittest.main()