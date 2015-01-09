import sys
import os
currDir = os.getcwd()
print currDir
sPathSpliter = currDir.split("\\")
print len(sPathSpliter)
frameworkPath = sPathSpliter[0]
for i in range(1, len(sPathSpliter)-1):
    frameworkPath = frameworkPath + "\\" + sPathSpliter[i]

sLibraryPath = frameworkPath + "\\Libraries"
print sLibraryPath
sys.path.insert(0, sLibraryPath)
import GenericLib
import Second

Second.secondLibFunction()
##GenericLib.openBrowser("http://www.google.co.in")
