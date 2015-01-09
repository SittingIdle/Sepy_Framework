import GenericLib
import time


####global driver
##def inputText():
####    global driver
##    driver = dateTime.driver
##    driver.find_element_by_name("q").send_keys("test")
##
##dateTime.openBrowser()
##time.sleep(5)
##inputText()
##dateTime.openBrowser()
##print current_time

def writeInNotePad(fileName, sText):
    sFile = open("Users//"+fileName+".txt", "w")
    sFile.write(sText)
    sFile.close()

##writeInNotePad("abc","sdjghask")

GenericLib.openBrowser("http://google.co.in")
GenericLib.inputText("name=q", "aaaaaaaa")
