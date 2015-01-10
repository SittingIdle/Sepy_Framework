import sys
import os
frameworkPath = os.getcwd()
print frameworkPath

sLibraryPath = frameworkPath + "\\Libraries"
print sLibraryPath
sys.path.insert(0, sLibraryPath)
import GenericLib
import time
from datetime import datetime

current_time = datetime.now().strftime('%Y%m%d%H%M%S')
##print current_time

## Browser and URL ##
sConfigFilePath = frameworkPath + "\\Config.ini"
print "SConfig File Path "
print sConfigFilePath
GenericLib.openBrowser("http://www.healthkart.com")
time.sleep(5)
##print "slept for 10 sec"

## Not a member ##
##GenericLib.actionsOnMenu("LINK=protein supplements","LINK=Whey Proteins")
GenericLib.clickOnSubmenuItem("css=div[id='dropDownbox1']> ul > li[class='gm-mc brdr-t  gm-brdr-l-orange']>a", "css=a[class='gm-tc-nm maintainHover']")
GenericLib.closeBrowser()
