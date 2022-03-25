import csv
import sys
from datetime import datetime
import re

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random

def main(argv):
    if len(sys.argv) != 4:
        sys.exit("not enough arguments")
    else:
        contactNum, fType, fileSize = sys.argv[1:]
        launch(int(contactNum),fType, fileSize)
        print("Good to go")

def generateEmail(first, last, company, suffix=".com"):
    #strip white spacesß
    fNameStr = "".join(first.split())
    lNameStr = "".join(last.split())
    companyStr = "".join(company.split())
    companyStr = re.sub('[().,*!@#$&/\']', '', companyStr)
    emailString = fNameStr+"."+lNameStr+"@"+companyStr+suffix
    return emailString

def launch(listSize, fType,fSize):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    with open('firstNames.txt','r') as f:
        firstNames = f.readlines()
    with open('lastNames.txt', 'r') as f:
        lastNames = f.readlines()
    with open('addresses.txt', 'r') as f:
        addresses = f.readlines()
    with open('companies.txt', 'r') as f:
        companies = f.readlines()
    with open('phoneNumbers.txt', 'r') as f:
        phoneNumbers = f.readlines()
    with open('jobTitles.txt', 'r') as f:
        jobTitles = f.readlines()

    #Generate random contacts
    contact = ""
    lname = ""

    #Figureout how many entries per files are needed
    def getFileSize():
        numOfFiles = int(listSize) / int(fSize)
        return int(numOfFiles)

    #prep the data
    firstName = ""
    lastName = ""
    companyName = ""
    jobTitle = ""
    companyAddress = ""
    companyPhone = ""
    email = ""

    #Initial time stamp
    now = datetime.now()
    print ("Start time: " + now.strftime("%H:%M:%S"))


    for x in range (0,getFileSize()):
        fileName = "Contacts_" + str(x);
        if fType == "csv":
            fileName = fileName+".csv"
            contactsFile = open(fileName, "a", encoding='UTF8')
            header = ['ID', 'First Name', 'Last Name', 'Company', 'Job Title', 'Address', "Phone Number", "email"]
            writer = csv.writer(contactsFile)
            writer.writerow(header)
            data = []
        else:
            fileName = fileName + ".txt"
            contactsFile = open(fileName, "a")
        #Generate contacts
        for i in range(0, int(fSize)):
            firstName = random.choice(firstNames)
            lastName = random.choice(lastNames)
            companyName = random.choice(companies)
            jobTitle = random.choice(jobTitles)
            companyAddress = random.choice(addresses)
            companyPhone = random.choice(phoneNumbers)
            email = generateEmail(firstName,lastName,companyName)
            if fType == "csv":
                data.append(i)
                data.append(firstName)
                data.append(lastName)
                data.append(companyName)
                data.append(jobTitle)
                data.append(companyAddress)
                data.append(companyPhone)
                data.append(email)
                writer.writerow(data)
                data.clear()
            else:
                contact = firstName.rstrip()
                contact = contact + " " + lastName
                contact = contact + companyName
                contact = contact + jobTitle
                contact = contact + companyAddress
                contact = contact + companyPhone
                contact = contact + email
                contactsFile.write('\n\n')
                contactsFile.write(contact)

        contactsFile.close()
        i = 0
    now = datetime.now()
    print("End time: " + now.strftime("%H:%M:%S"))





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv[1:])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
