from django.test import TestCase

from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage


# IMPORTS
import sys
import sqlite3
import os


# GLOBAL VARS
ABS_PATH = os.getcwd()
DB_FILE = ABS_PATH + '/db.sqlite3'
JSON_FILE = ABS_PATH + '/recipes_data.json'


class TestInitParams(TestCase):
    """ Just for informations when runing tests """
    print("##################################################")
    print("Python - version : " + sys.version + "\n")
    print("SQLite - version : " + sqlite3.version + "\n")
    print("\n")
    print("""      TEST MODULE FOR : DG-GQL-RECIPES   """)
    print("""          Author: NajlaBH                """)
    print("\n")
    print("##################################################")

    """ Default test """
    @classmethod
    def setUpTestData(cls):
        print("\nsetUpTestData: Run once to set up non-modified data for all class methods.\n")
        pass

    #def setUp(self):
    #    print("\nsetUp: Run once for every test method to setup clean data.\n")
    #    pass

    """Check if app contains required static files"""
    def test_dbfile(self):
        """
        Test1: Check if database file exist
        """
        print("\nTest1: Check if database file exist")
        if DB_FILE: 
            return os.path.exists(DB_FILE)

    def test_jsondatafile(self):
        """
        Test2: Check if json data file exist
        """
        print("\nTest2: Check if json data file exist")
        if JSON_FILE:
            return os.path.exists(JSON_FILE)
 
    def setUp(self):
        """
        Test3: Check if json data file is readable
        """
        print("\nTest3: Check if json data file is readable")
        self.testfile = open(JSON_FILE)
        self.testdata = self.testfile.read()
        self.testfile.close()
   

       
    ##TODO##
    #check if json file is not empty
