import unittest
from credit_card_validator import credit_card_validator

"""
Test Cases for Credit Card Validation
Cases generated using TSL Generator in cc.spec into cc.spec.tsl
testCases written using testWriterHelp.py
File written to conform with PEP8
"""


def writeerror(string):
    return f'Incorrect credit Card # = {string}'


class TestCase(unittest.TestCase):
    def testCase1(self):
        # Test Case: 1; Prefix: 4; Length: 15
        ccnum = "401235678901239"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase2(self):
        # Test Case: 2; Prefix: 4; Length: 16
        ccnum = "4012356789012352"
        self.assertTrue(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase3(self):
        # Test Case: 3; Prefix: 4; Length: 17
        ccnum = "40123567890123561"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase4(self):
        # Test Case: 4; Prefix: 33; Length: 15
        ccnum = "330124567890123"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase5(self):
        # Test Case: 5; Prefix: 34; Length: 14
        ccnum = "34012567890129"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase6(self):
        # Test Case: 6; Prefix: 34; Length: 15
        ccnum = "340125678901251"
        self.assertTrue(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase7(self):
        # Test Case: 7; Prefix: 34; Length: 16
        ccnum = "3401256789012561"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase8(self):
        # Test Case: 8; Prefix: 36; Length: 15
        ccnum = "360124578901243"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase9(self):
        # Test Case: 9; Prefix: 37; Length: 14
        ccnum = "37012456890120"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase10(self):
        # Test Case: 10; Prefix: 37; Length: 15
        ccnum = "370124568901243"
        self.assertTrue(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase11(self):
        # Test Case: 11; Prefix: 37; Length: 16
        ccnum = "3701245689012455"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase12(self):
        # Test Case: 12; Prefix: 38; Length: 15
        ccnum = "380124567901242"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase13(self):
        # Test Case: 13; Prefix: 50; Length: 16
        ccnum = "5012346789123462"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase14(self):
        # Test Case: 14; Prefix: 51; Length: 15
        ccnum = "510234678902345"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase15(self):
        # Test Case: 15; Prefix: 51; Length: 16
        ccnum = "5102346789023465"
        self.assertTrue(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase16(self):
        # Test Case: 16; Prefix: 51; Length: 17
        ccnum = "51023467890234674"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase17(self):
        # Test Case: 17; Prefix: 52; Length: 15
        ccnum = "520134678901347"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase18(self):
        # Test Case: 18; Prefix: 52; Length: 16
        ccnum = "5201346789013466"
        self.assertTrue(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase19(self):
        # Test Case: 19; Prefix: 52; Length: 17
        ccnum = "52013467890134676"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase20(self):
        # Test Case: 20; Prefix: 55; Length: 15
        ccnum = "550123467890129"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase21(self):
        # Test Case: 21; Prefix: 55; Length: 16
        ccnum = "5501234678901230"
        self.assertTrue(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase22(self):
        # Test Case: 22; Prefix: 55; Length: 17
        ccnum = "55012346789012348"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase23(self):
        # Test Case: 23; Prefix: 56; Length: 16
        ccnum = "5601234789012348"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase24(self):
        # Test Case: 24; Prefix: 2220; Length: 16
        ccnum = "2220134567891343"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase25(self):
        # Test Case: 25; Prefix: 2221; Length: 15
        ccnum = "222103456789035"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase26(self):
        # Test Case: 26; Prefix: 2221; Length: 16
        ccnum = "2221034567890346"
        self.assertTrue(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase27(self):
        # Test Case: 27; Prefix: 2221; Length: 17
        ccnum = "22210345678903450"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase28(self):
        # Test Case: 28; Prefix: 2222; Length: 15
        ccnum = "222201345678904"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase29(self):
        # Test Case: 29; Prefix: 2222; Length: 16
        ccnum = "2222013456789016"
        self.assertTrue(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase30(self):
        # Test Case: 30; Prefix: 2222; Length: 17
        ccnum = "22220134567890137"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase31(self):
        # Test Case: 31; Prefix: 2720; Length: 15
        ccnum = "272013456891344"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase32(self):
        # Test Case: 32; Prefix: 2720; Length: 16
        ccnum = "2720134568913455"
        self.assertTrue(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase33(self):
        # Test Case: 33; Prefix: 2720; Length: 17
        ccnum = "27201345689134566"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCase34(self):
        # Test Case: 34; Prefix: 2721; Length: 16
        ccnum = "2721034568903457"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCaseCustom1(self):
        # Visa Non-Prefix but contains valid Number 4.
        ccnum = "1444444444444444"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCaseCustom2(self):
        # MC Non-Prefix but contains valid Number 52.
        ccnum = "1525252525252525"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCaseCustom3(self):
        # MC Non-Prefix but contains valid Number 2222.
        ccnum = "1222222222222226"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCaseCustom4(self):
        # Amex Non-Prefix but contains valid Number 34.
        ccnum = "1343434343434341"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCaseCustom5(self):
        # Amex Non-Prefix but contains valid Number 37.
        ccnum = "137373737373735"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCaseCustom6(self):
        # Empty String
        ccnum = ""
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCaseLuhn1(self):
        # Valid MC length, and prefix --> invalid Luhn
        ccnum = "5353535353535336"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCaseLuhn2(self):
        # Valid Visa length, and prefix --> invalid Luhn
        ccnum = "4353535353535339"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))

    def testCaseLuhn3(self):
        # Valid Amex length, and prefix --> invalid Luhn
        ccnum = "345353535353533"
        self.assertFalse(credit_card_validator(ccnum), msg=writeerror(ccnum))


if __name__ == '__main__':
    unittest.main()
