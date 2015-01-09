import xlrd

# Create a workbook and add a worksheet.
workbook = xlrd.open_workbook('d://Expenses01.xlsx')
worksheet = worksheet = workbook.sheet_by_name('Sheet1')
rowCount = worksheet.nrows
print rowCount
num_cols = worksheet.ncols
print num_cols

cell_value = worksheet.cell_value(0, 0)
print cell_value

for iRow in range(0, rowCount):
    print iRow
    print worksheet.cell_value(iRow, 1)

##for iRow in range(2, rowCount+1):
##        sTestCaseCell = oWorksheet.cell(row = iRow, column = 1)
##        sTestCaseExecutionCell = oWorksheet.cell(row = iRow, column = 2)
##
##        sTestCaseName = sTestCaseCell.value
##        sTestCaseExecutionVal = sTestCaseExecutionCell.value
####        print sTestCaseName, sTestCaseExecutionVal
##
##        if sTestCaseExecutionVal == "Yes":
##            print sTestCaseName
##            intCounter = intCounter + 1
##            sFilePath = frameworkPath + "\\Test Cases\\" + sTestCaseName +".py"
##            setValueIntoINIFile(sIniFilePath , "Other", "Test Case Name", sTestCaseName)
##            sTCCurrentTime = datetime.now().strftime('%Y%m%d_%H%M%S')
##            sTCFileName = sTestCaseName + "_" + str(sTCCurrentTime) + ".html"
##            setValueIntoINIFile(sIniFilePath , "Other", "TestCase_FileName", sTCFileName)
##            sTCReportPath = frameworkPath + "\\Reports\\TestCaseReport\\" + sTCFileName
##            setValueIntoINIFile(sIniFilePath , "Other", "TestCase_Path", sTCReportPath)
##            execfile(sFilePath)
##            Complete_Report()
##            setValueIntoINIFile(sIniFilePath , "Other", "TestCase Status", "")
##            setValueIntoINIFile(sIniFilePath , "Other", "TestCase_FileName", "")
##            setValueIntoINIFile(sIniFilePath , "Other", "Test Case Name", "")
##


##
### Some data we want to write to the worksheet.
##expenses = (
##    ['Rent', 1000],
##    ['Gas',   100],
##    ['Food',  300],
##    ['Gym',    50],
##)
##
### Start from the first cell. Rows and columns are zero indexed.
##row = 0
##col = 0
##
### Iterate over the data and write it out row by row.
##for item, cost in (expenses):
##    worksheet.write(row, col,     item)
##    worksheet.write(row, col + 1, cost)
##    row += 1
##
### Write a total using a formula.
##worksheet.write(row, 0, 'Total')
##worksheet.write(row, 1, '=SUM(B1:B4)')
##
##workbook.close()
