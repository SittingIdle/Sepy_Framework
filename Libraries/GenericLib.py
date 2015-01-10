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
from selenium.webdriver.common.action_chains import ActionChains

current_time = datetime.now().strftime('%Y%m%d%H%M%S')
print current_time
##print frameworkPath
frameworkPath = os.getcwd()
print frameworkPath
iniFilePath = frameworkPath + "\\config.ini"
config = ConfigParser.RawConfigParser()
config.read(iniFilePath)
sTestCaseName = config.get("Other","Test Case Name")
print sTestCaseName
##sPathSpliter = currDir.split("\\")
##print len(sPathSpliter)
##frameworkPath = sPathSpliter[0]
##for i in range(1, len(sPathSpliter)-1):
##    frameworkPath = frameworkPath + "\\" + sPathSpliter[i]
    
global driver
driver = webdriver 
logFile = frameworkPath + "\\Logs\\GL_" + current_time + ".log"
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
    try:
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
        waitTime = 120
        wait = WebDriverWait(driver, 120)
        if oLocatorUpperCase.startswith("XPATH") or oLocatorUpperCase.startswith("//"):
            oElement = wait.until(EC.presence_of_element_located((By.XPATH, oLocator)))
##          oElement = driver.find_element_by_xpath(oLocator)
        elif oLocatorUpperCase.startswith("CSS"):
            oElement = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, oLocator)))
##          oElement = driver.find_element_by_css_selector(oLocator)
        elif oLocatorUpperCase.startswith("LINK"):
            oElement = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK, oLocator)))
    ##        oElement = driver.find_element_by_partiallinktext(oLocator)
        elif oLocatorUpperCase.startswith("ID"):
            oElement = wait.until(EC.presence_of_element_located((By.ID, oLocator)))
    ##        oElement = driver.find_element_by_id(oLocator)
        elif oLocatorUpperCase.startswith("NAME"):
            oElement = wait.until(EC.presence_of_element_located((By.NAME, oLocator)))
##            oElement = driver.find_element_by_name(oLocator)
        elif oLocatorUpperCase.startswith("CLASS"):
            oElement = wait.until(EC.presence_of_element_located((By.CLASS_NAME, oLocator)))
##            oElement = driver.find_element_by_class_name(oLocator)
        else:
            oElement = "Please define the object property with its attribute name"
    except Exception, e:
        oElement = str(e)
        eResult = "Looking for the Locator:- '" + oLocator + "'."
        tcReport("findElement", eResult, oElement, "Fail")

    return oElement
        
            
    
def openBrowser(url) :
##        setUp()
    sIniFilePath = frameworkPath + "\\config.ini"
    print "Under open Browser"
    print sIniFilePath
    print getValueFromINIFile(sIniFilePath , "Environment", "browser")
    browserName = getValueFromINIFile(sIniFilePath , "Environment", "browser")
    global driver
    print browserName
    if (browserName.lower() == "google chrome" or browserName.lower() == "gc" or browserName.lower() == "chrome"):
        chromedriver = frameworkPath + "\\Selenium_Drivers"
        print chromedriver
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome()
    elif (browserName.lower() == "firefox" or browserName.lower() == "ff" or browserName.lower() == "mozilla firefox"):
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Firefox()
        
    driver.implicitly_wait(60) 
    driver.get(url)
    eResult = "Open URL:- '" + url + "'."
    aResult = "Open URL sucessfully"
    tcReport("openBrowser", eResult, aResult, "Pass")
##        print a

##########################################################################################
def inputText(oLocator, value):
    global log
    eResult = "Should input Text successfully"
    try:
        oElement = findElement(oLocator)
        oElement.send_keys(value)
        sStatusMessage = "True , Text :- '" + value + "' set successfully to Locator:- '" + oLocator + "'."
        sStatus = "Pass"
    except Exception, e:
        sStatusMessage = "Unexpected error for Locator - '" + oLocator + "' : " + str(e)
##        sStatusMessage = "Unexpected error for Locator - '" + oLocator + "' : "
        sStatus = "Fail"
    log.info(sStatus)
    print sStatusMessage
    tcReport("inputText", eResult, sStatusMessage, sStatus)
    return sStatus

##########################################################################################
def clickObject(oLocator):
    eResult = "Click on desired object"
    try:
        oElement = findElement(oLocator)
##        print oElement
        oElement.click()
        sStatusMessage = "True , Object  :- '" + oLocator + "' Click successfully."
        sStatus = "Pass"
    except Exception, e:
        sStatusMessage = "Unexpected error for Locator - '" + oLocator + "' : " + str(e)
        sStatus = "Fail"
    log.info(sStatus)
    tcReport("clickObject", eResult, sStatusMessage, sStatus)
    return sStatus

##########################################################################################
def selectCheckbox(oLocator):
    eResult = "Should select the checkbox"
    try:
        oElement = findElement(oLocator)
        bChecked = oElement.is_selected()
        if (bChecked == False):
            oElement.click()
        sStatusMessage = "True , Object  :- '" + oLocator + "' checked successfully."
        sStatus = "Pass"
    except Exception, e:
        sStatusMessage = "Unexpected error for Locator - '" + oLocator + "' : " + str(e)
        sStatus = "Fail"
    tcReport("selectCheckbox", eResult, sStatusMessage, sStatus)
    log.info(sStatus)
    return sStatus

##########################################################################################
def deselectCheckbox(oLocator):
    eResult = "Should de select the checkbox"
    try:
        oElement = findElement(oLocator)
        bChecked = oElement.is_selected()
        if (bChecked == True):
            oElement.click()
        sStatusMessage =  "True , Object  :- '" + oLocator + "' un-checked successfully."
        sStatus = "Pass"
    except Exception, e:
        sStatusMessage = "Unexpected error for Locator - '" + oLocator + "' : " + str(e)
        sStatus = "Fail"
    tcReport("deselectCheckbox", eResult, sStatusMessage, sStatus)
    log.info(sStatus)    
    return sStatus

##########################################################################################
def selectDropDownByVisibleText(oLocator, sValue):
    eResult = "Should select the dropdown Value using visible text on screen"
    try:
        oElement = findElement(oLocator)
        select = Select(oElement)
        select.select_by_visible_text(sValue)
        sStatusMessage = "True , Visible text :- '" + sValue + "' selected successfully for object :- '" + oLocator + "'."
        sStatus = "Pass"
    except Exception, e:
        sStatusMessage = "Unexpected error for Locator - '" + oLocator + "' : " + str(e)
        sStatus = "Fail"
    tcReport("selectDropDownByVisibleText", eResult, sStatusMessage, sStatus)
    log.info(sStatus)
    return sStatus

##########################################################################################
def selectDropDownByValue(oLocator, sValue):
    try:
        oElement = findElement(oLocator)
        select = Select(oElement)
        select.select_by_value(sValue)
        sStatusMessage = "True , Option Value :- '" + sValue + "' selected successfully for object :- '" + oLocator + "'."
        sStatus = "Pass"
    except Exception, e:
        sStatusMessage = "Unexpected error for Locator - '" + oLocator + "' : " + str(e)
        sStatus = "Fail"
    tcReport("selectDropDownByValue", "It should select the dropdown value using value attribute", sStatusMessage, sStatus)
    log.info(sStatus)
    return sStatus

##########################################################################################
def objectIsSelected(oLocator):
    try:
        oElement = findElement(oLocator)
        oSelected = oElement.is_selected()
        if (oSelected == True):
            sStatusMessage = "True , Object :- '" + oLocator + "' is selected."
            sStatus = "Pass"
        else:
            sStatusMessage = "False , Object :- '" + oLocator + "' is not selected."
            sStatus = "Pass"
    except Exception, e:
        sStatusMessage = "Unexpected error for Locator - '" + oLocator + "' : " + str(e)
        sStatus = "Fail"
        
    tcReport("objectIsSelected", "It should check either object is selected or not", sStatusMessage, sStatus)
    log.info(sStatus)
    return sStatus

##########################################################################################
def verifyObjectText(oLocator, sExpectedText):
    eResult = "Expected Text:- " + sExpectedText
    try:
        oElement = findElement(oLocator)
        sActualText = oElement.text
        if sExpectedText in sActualText :
            sStatusMessage = "True , expected text:- '" + sExpectedText + "' matched with Actual Text:- '" +  sActualText + "'."
            print sStatusMessage
            sStatus = "Pass"
        else:
            sStatusMessage = "False , expected text:- '" + sExpectedText + "' did not matched with Actual Text:- '" +  sActualText + "'."
            sStatus = "Fail"
    except Exception, e:
        sStatusMessage = "Unexpected error for Locator - '" + oLocator + "'." ##+ str(e)
        sStatus = "Fail"

    tcReport("verifyObjectText", eResult, sStatusMessage, sStatus)
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
        sStatusMessage = "Connected to the DB having Host : '" + host + "', Port:- '" + port + "', User Name : - '" + userName + "', Password:- '" + password + "', DB name : - '" + dbName + "'." 
        sStatus = "Pass"
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            sStatusMessage = "Something is wrong with your user name or password"
            sStatus = "Fail"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            sStatusMessage = "Database does not exists"
            sStatus = "Fail"
        else:
            sStatusMessage = err
            sStatus = "Fail"
        cnx = "some error occurs"

    tcReport("connectMySQL", "It should connect the My SQL DB", sStatusMessage, sStatus)
    log.info (cnx + ", Connected to the DB having Host : '" + host + "', Port:- '" + port + "', User Name : - '" + userName + "', Password:- '" + password + "', DB name : - '" + dbName + "'." )
    return cnx

##########################################################################################
def fetchSQLData():
    try:
        sql = connectMySQL()
        cursor = sql.cursor()
        cursor.execute("select emailAddress from User_ where emailAddress = 'at20140903110215@test.com' ")
        
        rows = cursor.fetchall()
        if len(rows) == 0 :
            sStatusMessage = "No Row found"
            sStatus = "Fail"
        else:
            sStatus = rows[0][0]
            sStatusMessage = "DB Result: - " + sStatus
            sStatus = "Pass"

        sql.close()
##        for row in rows:
##            print row[0]
    except Exception, e:
        sStatusMessage = "Unexpected error for fetching value from Database: " + str(e)
        sStatus = "Fail"
        sql.close()

    tcReport("fetchSQLData", "It use to fetch data from SQL", sStatusMessage, sStatus)
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
##        sStatusMessage = "Property Name :- '" + propertyName + "' has value :- '" +  str(sResult) + "'."
##        sStatus = "Pass"
    except Exception, e:
        sResult = "Unexpected error while fecthing value from Ini file: " + str(e)
##        sStatusMessage = "Unexpected error while fecthing value from Ini file"
##        sStatus = "Fail"

##    log.info("PropertyName : - '" + propertyName + "' having value:- '" + sResult + "'.")
##    tcReport("getValueFromINIFile", "It use to fetch value from Config.ini file", sStatusMessage, sStatus)
    return sResult

########################################################################################
def setValueIntoINIFile_GL(filePath , headerName, propertyName, propertyValue):
    try:
        parser = ConfigParser.RawConfigParser()
        parser.read(filePath)
        if parser.has_section(headerName):
            parser.set(headerName, propertyName, str(propertyValue))
        else:
            parser.add_section(headerName)
            parser.set(headerName, propertyName, str(propertyValue))

        with open(filePath, 'wb') as configfile:
            parser.write(configfile)
        sResult = "PropertyName : - '" + propertyName + "' having value:- '" + sResult + "' has been set under Header:- '" + headerName + "'."
        sStatus = "Pass"
    except Exception, e:
        sResult = "Unexpected error while fecthing value from Ini file: " + str(e)
        sStatus = "Fail"

##    tcReport("setValueIntoINIFile_GL", "It use to set value in Config.ini file", sResult, sStatus)
    return sResult

#########################################################################################
def closeBrowser():
    try:
        driver.close()
        driver.quit()
        sStatusMessage = "Browser Close"
        sStatus = "Pass"
    except Exception, e:
        sStatusMessage = "Unexpected error : " + str(e)
        sStatus = "Fail"
        
    tcReport("Close Browser", "It should close the browser", sStatusMessage, sStatus)
    log.info(sStatusMessage)
    return sStatus

###############################################################################
def clickOnSubmenuItem(oLocatorMenu,oLocatorSubMenu):
    global driver
##        sStatus = ""
    eResult = "Should input Text successfully"
    try:
        menu = findElement(oLocatorMenu)
        ActionChains(driver).move_to_element(menu).perform()
        submenu = findElement(oLocatorSubMenu)
        oMenu = ActionChains(driver).move_to_element(menu).move_to_element(submenu)
        oMenu.click().perform()
        sStatusMessage = "True ,submenu clicked" + oLocatorSubMenu + "'."
        sStatus = "Pass"
    except Exception, e:
        sStatus = "Fail"
        sStatusMessage = "Unexpected error for Locator - '" + oLocatorSubMenu + "' : " + str(e)
    ##        sStatusMessage = "Unexpected error for Locator - '" + oLocator + "' : "
##    log.info(sStatusMessage)
    tcReport("inputText", eResult, sStatusMessage, sStatus)
    return sStatus

#########################################################################################
def clickAlert():
    global driver

    eResult = "Should perform operation on alert successfully"
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
        alert = driver.switch_to_alert()
        alert.accept()
        sStatus = "Pass"
        sStatusMessage = "Alert handled." 
    except Exception, e:
        print str(e)
        sStatus = "Fail"
        sStatusMessage = "Unexpected error for Alert" 
    ##        sStatusMessage = "Unexpected error for Locator - '" + oLocator + "' : "
##    log.info(sStatusMessage)
    tcReport("inputText", eResult, sStatusMessage, sStatus)
    return sStatus

#########################################################################################
def tcReport(stepName, expectedResult, ActualResult, status):
    StatusDetbgcolor=""
    sIniPath = frameworkPath + "\\config.ini"
    sHeaderName = "Environment"
    sEnvName = getValueFromINIFile(sIniPath , sHeaderName, "Environment")
    sReleaseName = getValueFromINIFile(sIniPath , sHeaderName, "Release")
    sUserReq = getValueFromINIFile(sIniPath , sHeaderName, "User Requested")
    sRunStartTime = datetime.now().strftime('%Y/%m/%d  %H:%M:%S')
##    sCurrentTime = datetime.now().strftime('%Y%m%d_%H%M%S')
    if status.lower() == "pass":
        StatusDetbgcolor='"#BCE954"'
    elif status.lower() == "fail":
        TCStatus = "Fail"
        setValueIntoINIFile_GL(sIniPath , "Other", "TestCase Status", TCStatus)
        StatusDetbgcolor = '"#F9966B"'
    elif status.lower() == "done":
        StatusDetbgcolor = '"#BCE954"'
##    sTCFileName = sTestCaseName + "_" + str(current_time) + ".html"
##    setValueIntoINIFile_GL(sIniPath , "Other", "TestCase_FileName", sTCFileName)
##    sReportPath = frameworkPath + "\\Reports\\TestCaseReport\\" + sTCFileName
    sReportPath = getValueFromINIFile(sIniPath , "Other", "TestCase_Path")
    print sReportPath
    if not(os.path.isfile(sReportPath)):
        sFile = open(sReportPath, "w")
        sFile.write('<html><HEAD><TITLE>Test Case Results</TITLE></HEAD><body><h4 align="center"><FONT COLOR="660066" FACE="Arial"SIZE=5><b> Test Case Report -' + sTestCaseName + '</b></h4>')
        sFile.write('<table cellspacing=1 cellpadding=1   border=1> <tr>')
        sFile.write('<h4> <FONT COLOR="660000" FACE="Arial" SIZE=4.5> Test Details :</h4>')
        sFile.write('<td width=150 align="left" bgcolor="#153E7E"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2.75><b>Run Date</b></td>')
        sFile.write('<td width=150 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=2.75><b>'+ sRunStartTime +'</b></td></tr>')
        sFile.write('<tr  border=1><td width=150 align="left" bgcolor="#153E7E"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2.75><b>User Requested</b></td>')
        sFile.write('<td width=150 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=2.75><b>'+ sUserReq +'</b></td></tr>')
        sFile.write('<tr  border=1><td width=150 align="left" bgcolor="#153E7E"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2.75><b>Environment</b></td>')
        sFile.write('<td width=150 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=2.75><b>'+ sEnvName +'</b></td></tr>')
        sFile.write('<tr><td  border=1 width=150 align="left" bgcolor="#153E7E"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2.75><b>Release</b></td>')
        sFile.write('<td  border=1 width=150 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=2.75><b>'+ sReleaseName +'</b></td></tr></table>')
        sFile.write('<h4> <FONT COLOR="660000" FACE="Arial" SIZE=4.5> Detailed Report :</h4><table  border=1 cellspacing=1    cellpadding=1 ><tr> ')
        sFile.write('<td width=80  align="center" bgcolor="#153E7E"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2><b>Step Name</b></td>')
        sFile.write('<td width=75 align="center" bgcolor="#153E7E"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2><b>Status</b></td>')
        sFile.write('<td width=600 align="center" bgcolor="#153E7E"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2><b>Expected Result</b></td>')
        sFile.write('<td width=600 align="center" bgcolor="#153E7E"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2><b>Actual Result</b></td></tr>')
    else:
        sFile = open(sReportPath, "a")

    #Append test report after creating
    sFile.write('<tr><td width=80 align="center"><FONT COLOR="#153E7E" FACE="Arial" SIZE=1><b>' + str(stepName) + '</b></td>')
    sFile.write('<td width=75 align="center" bgcolor=' + StatusDetbgcolor + '><FONT COLOR="#153E7E" FACE="Arial" SIZE=1><b>' + str(status) + '</b></td>')
    sFile.write('<td width=600 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=1><b>' + str(expectedResult) + '</b></td>')
    sFile.write('<td width=600 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=1><b>' + ActualResult.encode('ascii', 'ignore') + '</b></td></tr> ')
        
##fetchSQLData()
##    setUp()
##print getValueFromINIFile('Config.ini','DataBase', 'host')



       
