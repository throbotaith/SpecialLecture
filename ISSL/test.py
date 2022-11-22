import unittest
from CSVPrinter import CSVPrinter


class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))

    def test_read2(self):
        printer = CSVPrinter("sample2.csv")
        line = printer.read()
        self.assertEqual("value2B", line[1][2])

    def test_read3(self):
        try:
            printer = CSVPrinter("aaaa.csv")
            printer.read()
            unittest.TestCase.fail("This line should not be involked")
        except FileExistsError as error:
            print("error!")


test = TestCSVPrinter()
test.test_read()
