from openpyxl import load_workbook
import xlrd
import ConfigParser
from ConfigParser import SafeConfigParser
import sys
import os
import time
from datetime import datetime
global frameworkPath
frameworkPath = os.getcwd()
print frameworkPath

##sPathSpliter = currDir.split("\\")
##print len(sPathSpliter)
##frameworkPath = sPathSpliter[0]
##for i in range(1, len(sPathSpliter)):
##    frameworkPath = frameworkPath + "\\" + sPathSpliter[i]
sCurrentTime = datetime.now().strftime('%Y%m%d_%H%M%S')
global intCounter
intCounter = 0
global sReportPath
sReportPath = frameworkPath + "\\Reports\\Automation_Report_" + str(sCurrentTime) + ".html"

def readTestSuiteXlsxFile():
    # Pre Setting:
    global intCounter
    sIniFilePath = frameworkPath + "\\config.ini"
    setValueIntoINIFile(sIniFilePath, "Other", "FrameworkPath", frameworkPath)
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    logFile = frameworkPath + "\\Logs\\GL_" + current_time + ".log"
    setValueIntoINIFile(sIniFilePath , "Other", "Log File", logFile)
    setValueIntoINIFile(sIniFilePath , "Other", "TestCase Status", "")
    setValueIntoINIFile(sIniFilePath , "Other", "TestCase_FileName", "")
    setValueIntoINIFile(sIniFilePath , "Other", "Test Case Name", "")
    testSuiteFileName = getValueFromINIFile_Dr(sIniFilePath , "Environment", "testSuiteFile")
    testSuitePath = frameworkPath + "\\Test Suite\\" + testSuiteFileName
    oWorkbook = xlrd.open_workbook(testSuitePath)
    testSuiteSheetFileName = getValueFromINIFile_Dr(sIniFilePath , "Environment", "testSuiteSheetName")
    oWorksheet = oWorkbook.sheet_by_name(testSuiteSheetFileName)
    rowCount = oWorksheet.nrows

    for iRow in range(1, rowCount):
        sTestCaseCell = oWorksheet.cell_value(iRow, 0)
        sTestCaseExecutionCell = oWorksheet.cell_value(iRow, 1)

        sTestCaseName = sTestCaseCell
        sTestCaseExecutionVal = sTestCaseExecutionCell
        print sTestCaseName, sTestCaseExecutionVal

        if sTestCaseExecutionVal == "Yes":
            print sTestCaseName
            intCounter = intCounter + 1
            sFilePath = frameworkPath + "\\Test Cases\\" + sTestCaseName +".py"
            setValueIntoINIFile(sIniFilePath , "Other", "Test Case Name", sTestCaseName)
            sTCCurrentTime = datetime.now().strftime('%Y%m%d_%H%M%S')
            sTCFileName = sTestCaseName + "_" + str(sTCCurrentTime) + ".html"
            setValueIntoINIFile(sIniFilePath , "Other", "TestCase_FileName", sTCFileName)
            sTCReportPath = frameworkPath + "\\Reports\\TestCaseReport\\" + sTCFileName
            setValueIntoINIFile(sIniFilePath , "Other", "TestCase_Path", sTCReportPath)
            execfile(sFilePath)
            Complete_Report()
            setValueIntoINIFile(sIniFilePath , "Other", "TestCase Status", "")
            setValueIntoINIFile(sIniFilePath , "Other", "TestCase_FileName", "")
            setValueIntoINIFile(sIniFilePath , "Other", "Test Case Name", "")

######################################################################################
def setValueIntoINIFile(filePath , headerName, propertyName, propertyValue):
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
    except:
        sResult = "Unexpected error while fecthing value from Ini file: " , sys.exc_info()[0]
    return sResult

##########################################################################################
def getValueFromINIFile_Dr(filePath , headerName, propertyName):
    try:
        config = ConfigParser.RawConfigParser()
        config.read(filePath)
        sResult = config.get(headerName,propertyName)
        
    except:
        sResult = "Unexpected error while fecthing value from Ini file: " , sys.exc_info()[0]

##    log.info("PropertyName : - '" + propertyName + "' having value:- '" + sResult + "'.")
    return sResult

#########################################################################################
def Complete_Report():
    global sReportPath
    StatusDetbgcolor=""
    sIniPath = frameworkPath + "\\config.ini"
    sImagePath = frameworkPath + "\\Xebia.jpg"
    sHeaderName = "Environment"
    sEnvName = getValueFromINIFile_Dr(sIniPath , sHeaderName, "Environment")
    sReleaseName = getValueFromINIFile_Dr(sIniPath , sHeaderName, "Release")
    sUserReq = getValueFromINIFile_Dr(sIniPath , sHeaderName, "User Requested")
    sTestCaseName = getValueFromINIFile_Dr(sIniPath , "Other", "Test Case Name")
    sTC_Status = getValueFromINIFile_Dr(sIniPath , "Other", "TestCase Status")
    sTC_FileName = getValueFromINIFile_Dr(sIniPath , "Other", "TestCase_FileName")
    sRunStartTime = datetime.now().strftime('%Y/%m/%d  %H:%M:%S')
    if sTC_Status.lower() == "pass":
        StatusDetbgcolor='"#BCE954"'
    elif sTC_Status.lower() == "fail":
        finalTestCaseStatus="Fail"
        StatusDetbgcolor = '"#F9966B"'
    elif sTC_Status.lower() == "done":
        StatusDetbgcolor = '"#BCE954"'
    else:
        finalTestCaseStatus="Pass"
        StatusDetbgcolor = '"#BCE954"'
##    sReportPath = frameworkPath + "\\Reports\\Automation_Report_" + str(sCurrentTime) + ".html"
    print sReportPath
    if not(os.path.isfile(sReportPath)):
        sFile = open(sReportPath, "w")
        sFile.write('<html><HEAD><TITLE>Automation Report</TITLE></HEAD><body><h4 align="center"><FONT COLOR="660066" FACE="Arial"SIZE=5><b>Automation Test Report</b><img src="' + sImagePath + '" alt="Xebia" align="right"></h4>')
        sFile.write('<table cellspacing=1 cellpadding=1   border=1> <tr>')
        sFile.write('<h4> <FONT COLOR="660000" FACE="Arial" SIZE=4.5> Test Details :</h4>')
        sFile.write('<td width=150 align="left" bgcolor="#8904B1"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2.75><b>Run Date</b></td>')
        sFile.write('<td width=150 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=2.75><b>'+ sRunStartTime +'</b></td></tr>')
        sFile.write('<tr  border=1><td width=150 align="left" bgcolor="#8904B1"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2.75><b>User Requested</b></td>')
        sFile.write('<td width=150 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=2.75><b>'+ sUserReq +'</b></td></tr>')
        sFile.write('<tr  border=1><td width=150 align="left" bgcolor="#8904B1"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2.75><b>Environment</b></td>')
        sFile.write('<td width=150 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=2.75><b>'+ sEnvName +'</b></td></tr>')
        sFile.write('<tr><td  border=1 width=150 align="left" bgcolor="#8904B1"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2.75><b>Release</b></td>')
        sFile.write('<td  border=1 width=150 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=2.75><b>'+ sReleaseName +'</b></td></tr></table>')
        sFile.write('<h4> <FONT COLOR="660000" FACE="Arial" SIZE=4.5> Detailed Report :</h4><table  border=1 cellspacing=1    cellpadding=1 ><tr> ')
        sFile.write('<td width=80  align="center" bgcolor="#8904B1"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2><b>S.No</b></td>')
        sFile.write('<td width=75 align="center" bgcolor="#8904B1"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2><b>Test Case</b></td>')
        sFile.write('<td width=600 align="center" bgcolor="#8904B1"><FONT COLOR="#E0E0E0" FACE="Arial" SIZE=2><b>Status</b></td>')
    else:
       sFile = open(sReportPath, "a")

    #Append test report after creating
    sFile.write('<tr><td width=80 align="center"><FONT COLOR="#153E7E" FACE="Arial" SIZE=1><b>' + str(intCounter) + '</b></td>')
    sFile.write('<td width=600 align="left"><FONT COLOR="#153E7E" FACE="Arial" SIZE=1><b><a href=TestCaseReport/' + str(sTC_FileName) + '>' + str(sTestCaseName) + '</b></td>')
    sFile.write('<td width=75 align="center" bgcolor=' + StatusDetbgcolor + '><FONT COLOR="#153E7E" FACE="Arial" SIZE=1><b>' + str(finalTestCaseStatus) + '</b></td>')
        
##fetchSQLData()
##    setUp()
##print getValueFromINIFile('Config.ini','DataBase', 'host')
##setValueIntoINIFile("D:\\Botanix\\Python\\config.ini" , "Other", "FrameworkPath", frameworkPath)

readTestSuiteXlsxFile()

##import os
##print os.getcwd()

