import csv  
import json  
  
# https://www.guru99.com/reading-and-writing-files-in-python.html

CSV = "ihdata.csv"
JSONNAME = "ihdata.json"

def getHeader(CSV):
    f=open(CSV, "r", encoding='utf-8')

    f1 = f.readlines()
    headerline = f1[0]

    keys = rowToArray(headerline)

    f.close()
    return keys

def rowToArray(row):
    dataArray = []
    tempword = ""
    for character in row:
        
        if character == "\t":       
            dataArray.append(tempword)
            tempword= ""
        elif character == ",":
            dataArray.append(tempword)
            tempword= ""
        elif character == "\n":
            dataArray.append(tempword)
            tempword= ""
        else:
            tempword += character

    return dataArray

# def formatJSON(datarow):
def createJSON():
    f=open(CSV, "r", encoding='utf-8')
    
    finalJSON = []
    f1 = f.readlines()
    # headerline = f1[0]

    for line in f1:
        # print(line)
        finalJSON.append(addDatarowToJSON(line, getHeader(CSV), {}))

    # print(finalJSON)

    f.close()

    f = open( JSONNAME, 'w')  
    out = json.dumps(finalJSON)  
    f.write(out)  
    f.close()
# # print("JSON saved!")

def addDatarowToJSON(datarow, keys, jsonfile):
    # print(datarow, keys)
    dataArray = rowToArray(datarow)

    # simple check, ensure data array and keys are equal size
    if len(dataArray) == len(keys):
        for x in range(len(dataArray)):
            jsonfile[keys[x]] = dataArray[x]

    # print(jsonfile)
    return jsonfile



createJSON()