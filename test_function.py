import unittest #this is very important to 
from name_function import get_formatted_name
class test_get_formatted_name():
    def testing(self):
        formatted_name=get_formatted_name("deepak","singh")
        self.assertEqual(formatted_name,"Deepak Singh")

from name_function import places
class test_place():
    def testing(self):
        fname=places("khatima","uttarakhand")
        self.assertEqual("Khatima Uttarakhand India") #expected output you can put
                                                        #anything here
unittest.main()
