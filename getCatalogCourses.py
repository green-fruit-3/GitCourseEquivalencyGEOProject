import urllib
from bs4 import BeautifulSoup
import csv

# I had a csv list of all the urls corresponding to programs of study (majors, minors, concentrations)
# An example url is shown below
# I iterated through this list to get all of the program names (majors, minors, concentrations)
# and courses for those programs
with open('majorURLSTurnedCSVUpdated.csv') as f:

    # from the csv file, reads the list of urls I gathered
    data = csv.reader(f)

    # if attempting to write to an already open csv file, this will result in Permission denied
    courseMajorDataFile = open('coursemajordatafileishere.csv', 'w')

    # iterate through the list of urls to gather course data
    writer = csv.writer(courseMajorDataFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        url = str(row[0])
        r = urllib.request.urlopen(url).read()

        # used to scrape webpage
        soup = BeautifulSoup(r, "html.parser")

        """
        Example of what the below code will generate:
        Background: Some of the courses in the Cybersecurity and Business major at Northeastern University include 
        CS3000(Algorithms), FINA3301(Investments), CS3650(Computer Systems), and CS3500(Object-Oriented Design)
        
        The code below will create a csv file that looks something like: 
        
        Cybersecurity and Business
        CS3000
        FINA3301
        CS3650
        CS3500
        
        where the above data is in one column and all of the other majors and their data are insert in new columns to the right
        """

        # will contain all course data, and program name, for a given program of study
        courseMajorDataList = []
        major = soup.find('h1', class_='page-title')
        majorName = str(major.contents[0])
        courseMajorDataList.append(majorName)

        # represents the course tables
        # this part of the script will get all of the courses for one program of study
        # the for-loop provides the iteration through all of the programs of study
        tables = soup.find_all('table', class_='sc_courselist')  # tables-ResultSet
        atags = [None] * len(tables)
        for i in range(0, len(tables)):
            atags[i] = tables[i].find_all("a", class_='bubblelink code')
            for j in range(0, len(atags[i])):
                passStr = str(atags[i][j].contents[0])
                courseMajorDataList.append(passStr)
        writer.writerow(courseMajorDataList)
courseMajorDataFile.close()

#url = "http://catalog.northeastern.edu/undergraduate/engineering/electrical-computer/computer-engineering-computer-science-bscompe/#programrequirementstext"
