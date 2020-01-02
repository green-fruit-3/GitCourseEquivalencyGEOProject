import urllib
from bs4 import BeautifulSoup
import csv

# Data cleaning needed to be completed
# this code was made as I wanted to create a PivotTable with course, major, and institution keys
# Here, I wanted to retreive the entire list of courses
with open('majorURLSTurnedCSVUpdated.csv') as f:
    data = csv.reader(f)
    # if attempting to write to an already open csv file, will result in Permission denied
    courseMajorDataFile = open('allcourses.csv', 'w')
    writer = csv.writer(courseMajorDataFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        url = str(row[0])
        r = urllib.request.urlopen(url).read()

        soup = BeautifulSoup(r, "html.parser")

        major = soup.find('h1', class_='page-title')
        # doesn't include major name as all I wanted to retrieve were the list of all courses

        # represents the course tables
        tables = soup.find_all('table', class_='sc_courselist')  # tables-ResultSet
        atags = [None] * len(tables)
        for i in range(0, len(tables)):
            atags[i] = tables[i].find_all("a", class_='bubblelink code')
            for j in range(0, len(atags[i])):
                passStr = str(atags[i][j].contents[0])
                writer.writerow(passStr)
courseMajorDataFile.close()

#url = "http://catalog.northeastern.edu/undergraduate/engineering/electrical-computer/computer-engineering-computer-science-bscompe/#programrequirementstext"


# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all