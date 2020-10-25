import simplejson as json
from sheetKeys import allKeys
import gspread
from api.models import db, ItemMagicChance, CoinGen, ArtGemChance, ItemTypeTable, ItemGemTable, MundaneItem, ArmorGeneration, MagicItemTable, ItemArtTable
from  sqlalchemy.sql.expression import func, select
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
                            newRow = className()
                            rowInc = 0
                            newRow.id = idInc
                            for eachCol in allColumns:
                                try:
                                    setattr(newRow, eachCol, eachRow[rowInc])
                                except Exception as e:
                                    print(str(e))
                                    setattr(newRow, eachCol, None)
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

    #print(wks.sheet1.get('A1'))
    #values_list = wks.sheet1.row_values(1)
    #print(values_list)
    #url1 = "https://spreadsheets.google.com/feeds/cells/" + key + "/od6/public/values?alt=json"
    #url2 = "https://spreadsheets.google.com/feeds/list/" + key + "/od6/public/values?alt=json"

