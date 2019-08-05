import csv  
import json  
  
# https://www.guru99.com/reading-and-writing-files-in-python.html

CSV = "original.csv"


def getHeader(CSV):
    f=open(CSV, "r")

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
        elif character == "\n":
            dataArray.append(tempword)
            tempword= ""
        else:
            tempword += character

    return dataArray

# def formatJSON(datarow):
def createJSON():
    f=open(CSV, "r")
    
    finalJSON = []
    f1 = f.readlines()
    # headerline = f1[0]

    for line in f1:
        # print(line)
        finalJSON.append(addDatarowToJSON(line, getHeader(CSV), {}))

    # print(finalJSON)

    f.close()

    
    # # Open the CSV  
    # f = open(CSV, 'rU')  
    # # Change each fieldname to the appropriate field name. I know, so difficult.  
    # reader = csv.DictReader( f, getHeader(CSV))  
    # # Parse the CSV into JSON  
    # out = json.dumps( [ row for row in reader ] )  
    # print("JSON parsed!") 
    # # Save the JSON  
    f = open( 'output.json', 'w')  
    out = json.dumps(finalJSON)  
    f.write(out)  
    # print(out)
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