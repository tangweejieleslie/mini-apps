import csv  
import json  
  
# https://www.guru99.com/reading-and-writing-files-in-python.html

CSV = "original.csv"


def getHeader(CSV):
    f=open(CSV, "r")

    f1 = f.readlines()
    headerline = f1[0]

    keys = rowToArray(headerline)

        # append each character into a string
        # until tab

    print(keys)
    return keys
    f.close()


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


# Open the CSV  
f = open(CSV, 'rU')  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, getHeader(CSV))  
# Parse the CSV into JSON  
out = json.dumps( [ row for row in reader ] )  
print("JSON parsed!") 
# Save the JSON  
f = open( 'output.json', 'w')  
f.write(out)  
print(out)

print("JSON saved!")

