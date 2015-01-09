import os
import sys
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import mysql.connector
from mysql.connector import errorcode
import ConfigParser
import logging

current_time = datetime.now().strftime('%Y%m%d%H%M%S')
print current_time
##print "a"
##class sample():
global driver
driver = webdriver
logFile = "GL_" + current_time + ".log"
logging.basicConfig(filename=logFile, level=logging.INFO)
log = logging.getLogger("Generic Lib")
##def setUp():
##        chromedriver = "E:\BeachBody\CASL\Selenium_Python"
##        os.environ["webdriver.chrome.driver"] = chromedriver
##        driver = webdriver.Chrome()
##        return driver
##    print "gfdsg"
##    global a

def findElement(oLocator):
    oLocatorUpperCase = oLocator.upper()
##    print oLocatorUpperCase
    if oLocatorUpperCase.startswith("XPATH") or oLocatorUpperCase.startswith("CSS") or oLocatorUpperCase.startswith("ID") or oLocatorUpperCase.startswith("NAME") or oLocatorUpperCase.startswith("LINK") or oLocatorUpperCase.startswith("CLASS"):
        oLocatorArray = oLocator.split("=")
        if len(oLocatorArray) != 1 :
            oLocatorValue = oLocatorArray[1]
            for x in range(1, (len(oLocatorArray)-1)): 
                oLocatorValue = oLocatorValue + "=" + oLocatorArray[x+1];
            oLocator = oLocatorValue
        else:
            oLocator = oLocatorArray[1]

    oLocator = oLocator.strip()

    if oLocatorUpperCase.startswith("XPATH") or oLocatorUpperCase.startswith("//"):
        oElement = driver.find_element_by_xpath(oLocator)
    elif oLocatorUpperCase.startswith("CSS"):
        oElement = driver.find_element_by_css_selector(oLocator)
    elif oLocatorUpperCase.startswith("LINK"):
        oElement = driver.find_element_by_partiallinktext(oLocator)
    elif oLocatorUpperCase.startswith("ID"):
        oElement = driver.find_element_by_id(oLocator)
    elif oLocatorUpperCase.startswith("NAME"):
        oElement = driver.find_element_by_name(oLocator)
    elif oLocatorUpperCase.startswith("CLASS"):
        oElement = driver.find_element_by_class_name(oLocator)
    else:
        oElement = "Please define the object property with its attribute name"
##        print driver.find_element_by_id(oLocator)
##        oElement = driver.find_element_by_id(oLocator)
##        print "Under ID"
##        print oElement.is_displayed()
##        if oElement.is_displayed() == False :
##            oElement = driver.find_element_by_id(oLocator)
##            print "Under Name"
##            print oElement.is_displayed()
##            if oElement.is_displayed() == False:
##                oElement = driver.find_element_by_class_name(oLocator)
##                print "under class name"
##    print oElement
##    oElement.click()
##    print "after click"
##    oElement.send_keys("saurabh")
    return oElement
        
            
    
def openBrowser(url) :
##        setUp()
    print "kj"
    chromedriver = "E:\BeachBody\CASL\Selenium_Python"
    os.environ["webdriver.chrome.driver"] = chromedriver
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(60) 
    driver.get(url)
##        print a

##########################################################################################
def inputText(oLocator, value):
    global log
    try:
        oElement = findElement(oLocator)
        oElement.send_keys(value)
        sStatus = "True , Text :- '" + value + "' set successfully to Locator:- '" + oLocator + "'."
    except:
        sStatus = "Unexpected error for Locator - '" + oLocator + "' : " , sys.exc_info()[0]
    log.info(sStatus)
    return sStatus

##########################################################################################
def clickObject(oLocator):
    try:
        oElement = findElement(oLocator)
##        print oElement
        oElement.click()
        sStatus = "True , Object  :- '" + oLocator + "' Click successfully."
    except:
        sStatus = "Unexpected error for Locator - '" + oLocator + "' : " , sys.exc_info()[0]
    log.info(sStatus)
    return sStatus

##########################################################################################
def selectCheckbox(oLocator):
    try:
        oElement = findElement(oLocator)
        bChecked = oElement.is_selected()
        if (bChecked == False):
            oElement.click()
        sStatus = "True , Object  :- '" + oLocator + "' checked successfully."
    except:
        sStatus = "Unexpected error for Locator - '" + oLocator + "' : " , sys.exc_info()[0]

    log.info(sStatus)
    return sStatus

##########################################################################################
def deselectCheckbox(oLocator):
    try:
        oElement = findElement(oLocator)
        bChecked = oElement.is_selected()
        if (bChecked == True):
            oElement.click()
        sStatus =  "True , Object  :- '" + oLocator + "' un-checked successfully."
    except:
        sStatus = "Unexpected error for Locator - '" + oLocator + "' : " , sys.exc_info()[0]

    return sStatus

##########################################################################################
def selectDropDownByVisibleText(oLocator, sValue):
    try:
        oElement = findElement(oLocator)
        select = Select(oElement)
        select.select_by_visible_text(sValue)
        sStatus = "True , Visible text :- '" + sValue + "' selected successfully for object :- '" + oLocator + "'."
    except:
        sStatus = "Unexpected error for Locator - '" + oLocator + "' : " , sys.exc_info()[0]

    log.info(sStatus)
    return sStatus

##########################################################################################
def selectDropDownByValue(oLocator, sValue):
    try:
        oElement = findElement(oLocator)
        select = Select(oElement)
        select.select_by_value(sValue)
        sStatus = "True , Option Value :- '" + sValue + "' selected successfully for object :- '" + oLocator + "'."
    except:
        sStatus = "Unexpected error for Locator - '" + oLocator + "' : " , sys.exc_info()[0]

    log.info(sStatus)
    return sStatus

##########################################################################################
def objectIsSelected(oLocator):
    try:
        oElement = findElement(oLocator)
        oSelected = oElement.is_selected()
        if (oSelected == True):
            sStatus = "True , Object :- '" + oLocator + "' is selected."
        else:
            sStatus = "False , Object :- '" + oLocator + "' is not selected."
    except:
        sStatus = "Unexpected error for Locator - '" + oLocator + "' : " , sys.exc_info()[0]

    log.info(sStatus)
    return sStatus

##########################################################################################
def verifyObjectText(oLocator, sExpectedText):
    try:
        oElement = findElement(oLocator)
        sActualText = oElement.text
        if sExpectedText in sActualText :
            sStatus = "True , expected text:- ' " + sExpectedText + "' matched with Actual Text:- '" +  sActualText + "'."
        else:
            sStatus = "False , expected text:- ' " + sExpectedText + "' did not matched with Actual Text:- '" +  sActualText + "'."
    except:
        sStatus = "Unexpected error for Locator - '" + oLocator + "' : " , sys.exc_info()[0]

    log.info(sStatus)
    return sStatus

##########################################################################################
def writeInNotePad(fileName, sText):
    sFile = open("Users//"+fileName+".txt", "w")
    sFile.write(sText)
    sFile.close()
    log.info("write the value in notepad file at : - '" + fileName + "'.")

##########################################################################################
def connectMySQL():
    try:
        filePath = "Config.ini"
        host = getValueFromINIFile(filePath, 'DataBase', 'Host')
        port = getValueFromINIFile(filePath, 'DataBase', 'Port')
        userName = getValueFromINIFile(filePath, 'DataBase', 'Username')
        password = getValueFromINIFile(filePath, 'DataBase', 'Password')
        dbName = getValueFromINIFile(filePath, 'DataBase', 'Database')
        cnx = mysql.connector.connect(user=userName, password=password, host=host,database=dbName, port=port)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exists")
        else:
            print(err)
        cnx = "some error occurs"

    log.info (cnx + ", Connected to the DB having Host : '" + host + "', Port:- '" + port + "', User Name : - '" + userName + "', Password:- '" + password + "', DB name : - '" + dbName + "'.") 
    return cnx

##########################################################################################
def fetchSQLData():
    try:
        sql = connectMySQL()
        cursor = sql.cursor()
        cursor.execute("select emailAddress from User_ where emailAddress = 'at20140903110215@test.com' ")
        
        rows = cursor.fetchall()
        if len(rows) == 0 :
            sStatus = "Fail"
        else:
            sStatus = rows[0][0]
            print "DB Result: - " + sStatus

        sql.close()
##        for row in rows:
##            print row[0]
    except:
        sStatus = "Unexpected error for fetching value from Database: " , sys.exc_info()[0]
        sql.close()
              
    log.info(sStatus)
    return sStatus
##########################################################################################
def CreateIniFile():
    config = ConfigParser.RawConfigParser()
    config.add_section('Section1')
    config.set('Section1', 'an_int', '15')
    config.set('Section1', 'a_bool', 'true')
    config.set('Section1', 'a_float', '3.1415')
    config.set('Section1', 'baz', 'fun')
    config.set('Section1', 'bar', 'Python')
    config.set('Section1', 'foo', '%(bar)s is %(baz)s!')
    # Writing our configuration file to 'example.cfg'
    with open('example.ini', 'wb') as configfile:
        config.write(configfile)

##########################################################################################
def getValueFromINIFile(filePath , headerName, propertyName):
    try:
        config = ConfigParser.RawConfigParser()
        config.read(filePath)
        sResult = config.get(headerName,propertyName)
    except:
        sResult = "Unexpected error while fecthing value from Ini file: " , sys.exc_info()[0]

    log.info("PropertyName : - '" + propertyName + "' having value:- '" + sResult + "'.")
    return sResult
        
##fetchSQLData()
##    setUp()
##print getValueFromINIFile('Config.ini','DataBase', 'host')




       
