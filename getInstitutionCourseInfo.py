from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import csv

# This code allowed me to automate the process of clicking on a website's dropdown menus to extract data
# Through this process, I was able to get the relationships between two keys :
# a foreign institution and the courses they have that transfer back to Northeastern University for credit

# opens a browser and gets the website I want to perform automated actions on
driver = webdriver.Edge()
driver.get("https://www.northeastern.edu/geo/studyabroad/course-equivalency/evaluations/courses-by-program/")
frame = driver.find_element_by_xpath('//*[@id="pods"]/body/div[1]/main/article/section/div/div/div[1]/div/p[3]/iframe')

# switched to frame as frame error occurred
driver.switch_to.frame(frame)

# adjusted view to view dropdown menu (table)
image = driver.find_element_by_class_name('wrapperFULL')
driver.execute_script("arguments[0].scrollIntoView(true);", image)

# I needed to find the length for selecting all the course options so I could iterate that number of times
institution_button = Select(driver.find_element_by_id('FICE'))
num_of_institutions = len(institution_button.options)
geoFile = open('ha.csv', 'w')
writer = csv.writer(geoFile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)

# loops through all institutions
# has to be modified for different runs of the program to capture different institutions
for k in range(1, num_of_institutions):

    # print statement used for testing
    print("Institution: " + str(k))

    # get the institution button (dropdown menu) and selects the kth option
    institution_button = Select(driver.find_element_by_id('FICE'))
    institution_button.select_by_index(k)

    # prepares scraping of the webpage
    # these lines are important as they give you the instance of the website
    # in other words, it gives you the html contents once the clicks on the website are performed above
    page_zero = driver.page_source
    soup_zero = BeautifulSoup(page_zero, 'html.parser')

    # gets the name of the institution
    institution_tag = soup_zero.find('select', id='FICE')
    institution_options = institution_tag.find_all('option')
    institution_name = institution_options[k].text

    # print statement used for testing
    print(institution_name)

    # restarts the list  - this list is used to create a row of data in the csv file
    # this row of data will have the institution name in the first column and the courses in the succeeding columns
    institution_info = []
    institution_info.append(institution_name)

    # waits 5 seconds for the department button to appear before throwing an exception
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.ID, 'tseg')))
    department_button = Select(driver.find_element_by_id('tseg'))
    num_of_departments = len(department_button.options)

    #loops through all the departments for a given institution - changed to capture different departments
    # useful for when a department's table doesn't display (occurred twice
    # these two times account for the two csv files)
    for i in range(1, num_of_departments):

        # print statement used for testing
        print("Department: " + str(i))

        # we wait here as we wait for the department and table to disappear at the bottom
        wait_two = WebDriverWait(driver, 10)
        wait_two.until(EC.presence_of_element_located((By.ID, 'tseg')))
        department_button_one = Select(driver.find_element_by_id('tseg'))
        department_button_one.select_by_index(i)

        # some departments' tables take a very long time to load as there is alot of data
        # as a result, we wait a significant amount of time (near 5 mins) for the table to appear
        table_wait = WebDriverWait(driver, 296)
        table_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table[border='1']")))

        course_button = Select(driver.find_element_by_id('TransferCourse'))

        # prepares scraping of the webpage
        # these lines are important as they give you the instance of the website
        # in other words, it gives you the html contents once the clicks on the website are performed above
        page = driver.page_source
        soup = BeautifulSoup(page, "html.parser")

        # find the table tag that has the elements we need
        page_table = soup.find('table', border='1')
        rows_of_department_courses = page_table.find_all('tr')
        for j in range(1, len(rows_of_department_courses)):
            data = rows_of_department_courses[j].find_all('td')

            # this if-else statement covers two cases that occured
            # 1) course names were displayed as links (a tag) OR...
            # 2) course names were bolded (b tag)
            # In either case, I retrieved the course name
            if data[1].find('a'):
                nu_course = data[1].find('a')
                course = nu_course.contents[0]
                # print statement used for testing
                print(course)
                institution_info.append(course)
            else:
                nu_course = data[1].find('b')
                course = nu_course.contents[0]
                # print statement used for testing
                print(course)
                institution_info.append(course)

        # resets the department button by selecting the blank option
        department_button_reset = Select(driver.find_element_by_id('tseg'))
        department_button_reset.select_by_index(0)
        # 10 is used as sometimes tables take too long to disappear
        table_wait_disappear = WebDriverWait(driver, 10)
        table_wait_disappear.until_not(EC.presence_of_element_located((By.CSS_SELECTOR, "table[border='1']")))

    # resets the institution button by selecting the blank option
    institution_button_reset = Select(driver.find_element_by_id('FICE'))
    institution_button_reset.select_by_index(0)

    # waits for the department button selection to disappear
    department_wait_disappear = WebDriverWait(driver, 10)
    department_wait_disappear.until_not(EC.presence_of_element_located((By.ID, 'tseg')))

    writer.writerow(institution_info)

geoFile.close()

# WebDriver API classes
# Element - methods to perform on element (ex; submit())
# SearchContext - how to search for an element on a webpage

# The best locators are : 1) unique 2) descriptive 3) static

# How to use for-each loops
# for element in iterable:
#     operate(element)

# OR...
# def foreach(function, iterable):
#     for element in iterable:
#         function(element)

# Python Selenium Documentation Source
# https://selenium-python.readthedocs.io/