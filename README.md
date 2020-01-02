getCatalogCourses Script Documentation
Example 'Errors'
1) EECE2414 to EECE2530 - the program does not capture in between as these links do not exist on the webpage
     - no easy work around (can't determine which courses in btwn these two courses actually exist)
     - Different but similar Problem :  cases like Political Science minor where you can take any POLS class for credit
       a) For Political Science minor, you can complete any three Political Science courses for the minor
       b) Using the current methodology, there is no easy way to determine all of the Political Science courses
2) EECE4698 - course appears on the program requirements page but doesn't have a link
    - should not be a problem as if the course doesn't have a code, this likely means it was deactivated (no longer 
    exists)

---------------------------------------
firstSeleniumTest Script Documentation
Example 'Errors':
1) A foreign course might have two equivalents here at Northeastern. I only included the first equivalent. Capturing all
the course equivalents can be done to further this project and it shouldn't be too difficult to accomplish (I don't know
how difficult it would be though). I did notice once that the two equivalents were combined together on the GEO website.
I believe this course code turned out to be WMNS/JWSS. Using the current methodology, neither course was retrieved.

2) On the GEO website, some courses are labeled as electives. I don't think these courses are included in the final
Excel dashboard as I don't believe they would appear in the undergraduate course catalog.

Institutions and their Departments that caused errors as the GEO website failed to deliver their tables
The institutions and departments below are referenced as the 5th and 6th csv file in this documentation
NUH in Italy Lorenzo Medici Institution 110 Dept NUH
C&P in Hungary Budapest Math Institution 198 Dept 4

Known System Requirements:
 - Webdriver
   - Suggestion : If you aren't familiar with Selenium and/or webdrivers, I recommend watching a YouTube tutorial on 
   working with Selenium that discusses the installation of the webdriver 


Running the Program

1) When the webpage opens up, scroll such that the institution dropdown button appears at the very top and is not
hindered by any elements (ex; the banner wrapper, the jiovchat button when it gets larger, etc)
If this is not done, the program will stop prematurely

2) The program was run several times as it stopped prematurely, anyways. The program would not run once and successfully
capture all the data from all the institutions. As I read stories online, I found many people
found their Selenium tests to be unreliable/flaky at times. When my program runs, it fails at seemingly random points.
I did not fix this. I noticed that if I ran the code for a certain limited range of institutions at a time, the 
likelihood of the code running successfully would increase. Thus, instead of one long run of the program, I opted for 
six (it could've been any number, this number worked for me) smaller runs that captured different institutions' data.

After thinking about why the program failed at different points during different runs of the same code, an avenue I 
didn't explore was the use of different Expected Conditions(for instance, instead of using solely 
presence_of_element_located, perhaps I could've used this in conjunction with visibility_of_element) 

Six csv files were created. Each time the program was run, either the parameters for the institution changed 
(to get different institutions) or both these parameters and the parameters controlling the departments changed.
The six csv files created accounted for the following institutions:
 1) Institutions 1-109
 2) Institutions 111-176
 3) Institutions 177-197
 4) Institutions 199 - 213
 5) Institution #110 (Italy, Florence : Lorenzo de Medici) - separate csv file created as table for one department never
  displayed (presumed to be an error on the GEO website) / changed department parameters and completed one department
  manually (this manual data collection amounted to nothing as no new courses were added to the list of courses offered
  at the institution)
 6) Institution #198 (Hungary, Budapest : Math) - separate csv file created as table for one department never
  displayed (presumed to be an error on the GEO website) / changed department parameters and completed one department
  manually (this manual data collection amounted to nothing as no new courses were added to the list of courses offered
  at the institution)
  
FUTURE: if the website structure changes, the program may not work, as it's reliant on the structure of the website