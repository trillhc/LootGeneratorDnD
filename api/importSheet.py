import simplejson as json
from sheetKeys import allKeys
import gspread
from api.models import *
from api.constants import *


def SheetToDatabase():
    gc = gspread.service_account()


    for eachSheet, eachKey in allKeys.items():
        try:
            print("Loading Spreadsheet "+ eachSheet)
            wks = gc.open_by_key(eachKey)
            worksheetList = wks.worksheets()
            for eachWorksheet in worksheetList:
                try:
                    print("Loading Worksheet " + eachWorksheet.title)
                    className = globals()[eachWorksheet.title]
                    allRows = eachWorksheet.get_all_values()
                    allColumns = allRows[0]
                    allRows = allRows[1:]
                    idInc = 1
                    for eachRow in allRows:
                        try:
                            newRow = className(id=idInc)
                            rowInc = 0
                            #newRow.id = idInc
                            for eachCol in allColumns:
                                try:
                                    if eachRow[rowInc] != '':
                                        rowData = eachRow[rowInc]
                                        if rowData == "TRUE":
                                            rowData = True
                                        if rowData == "FALSE":
                                            rowData = False
                                        setattr(newRow, eachCol, rowData)
                                except Exception as e:
                                    print(str(e))
                                rowInc = rowInc + 1
                            db.session.add(newRow)
                            idInc = idInc + 1
                        except Exception as e:
                            print(str(e))
                    db.session.commit()
                except Exception as e:
                    print(str(e))
        except Exception as e:
            print(str(e))
    print("Finished Loading To Database")
    return(True)


#gem chance test sheet
#https://docs.google.com/spreadsheets/d/1A42jQEc6LetoWlX7QkPQtFegPl4VKwas1eKtHTIcTUQ/edit#gid=0
