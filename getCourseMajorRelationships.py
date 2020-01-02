import urllib
from bs4 import BeautifulSoup
import csv

# the code here is very similar to the code in the file getCatalogCourses.py
# this code was made as I wanted to create a PivotTable with course, major, and institution keys
# a simple way to do this was to write the same data to a different csv file, in a slightly different format
# Here, I get the relationships between courses and majors
with open('majorURLSTurnedCSVUpdated.csv')as f:

    # from the csv file, reads the list of urls I gathered
    data = csv.reader(f)

    # if attempting to write to an already open csv file, will result in Permission denied
    courseMajorDataFile = open('ightbet.csv', 'w')

    # iterate through the list of urls to gather course data
    writer = csv.writer(courseMajorDataFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        url = str(row[0])
        r = urllib.request.urlopen(url).read()

        soup = BeautifulSoup(r, "html.parser")

        """
        Example of what the below code will generate:
        Background: Some of the courses in the Cybersecurity and Business major at Northeastern University include 
        CS3000(Algorithms), FINA3301(Investments), CS3650(Computer Systems), and CS3500(Object-Oriented Design)

        The code below will create a csv file that looks something like: 

        course:CS3000 major:Cybersecurity and Business
        course:FINA3301 major:Cybersecurity and Business
        course:CS3650 major:Cybersecurity and Business
        course:CS3500 major:Cybersecurity and Business

        where the above data is in one column and all of the other majors and their data are inserted into new rows below
        in the same column
        """

        major = soup.find('h1', class_='page-title')
        majorName = str(major.contents[0])

        # represents the course tables
        tables = soup.find_all('table', class_='sc_courselist')  # tables-ResultSet
        atags = [None] * len(tables)
        for i in range(0, len(tables)):
            atags[i] = tables[i].find_all("a", class_='bubblelink code')
            for j in range(0, len(atags[i])):
                passStr = str(atags[i][j].contents[0])
                writer.writerow("course:"+passStr+" major:"+majorName)
courseMajorDataFile.close()

#url = "http://catalog.northeastern.edu/undergraduate/engineering/electrical-computer/computer-engineering-computer-science-bscompe/#programrequirementstext"


# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all