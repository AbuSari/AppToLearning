import requests
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSessionIdException

import time
import datetime

import xlsxwriter

import getpass
print(getpass.getuser())



workbook = xlsxwriter.Workbook(r'C:\Users\Mohammed Alsuwailem\TESTSELENIUM.xlsx')
columns=0
row=0
col=0
cell_format = workbook.add_format({'bold': True, 'italic': True})
cell_format= cell_format.set_align('center')
# swissinfoSheet = workbook.add_worksheet('swissinfo')
# swissinfoSheet.write(row,col, 'تاريخ النشر',cell_format)
# swissinfoSheet.write(row,col+1, 'تصنيف الخبر')
# swissinfoSheet.write(row,col+2, 'العنوان')
# swissinfoSheet.write(row,col+3, 'ملخص')
# swissinfoSheet.write(row,col+4, 'الرابط')
# swissinfoDateFrame = pd.DataFrame(columns = ["pub_date", "category","title","abstract","web_url"])


# main_url = "https://www.swissinfo.ch/ara/reuters"


s = Service(r'C:\Users\Mohammed Alsuwailem\Downloads\chromedriver_win32 (3)\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# driver = webdriver.Chrome(executable_path=r'C:\Users\Mohammed Alsuwailem\Downloads\chromedriver_win32 (3)\chromedriver.exe')
# sss = driver.get('https://www.swissinfo.ch/ara/reuters')
# extra = driver.find_elements(By.XPATH,"//*[contains(text(), '{}')]".format('أظهر المزيد'))
# print(extra)
# time.sleep(3)
# extra[0].click()
# time.sleep(3)
# article = driver.find_elements(By.TAG_NAME,'article')
# print('1')
# for i in article:
#     title = i.find_elements(By.TAG_NAME,'div')[1].text.split('\n')
#     title1 = title[0]
#     date = title[1]
#     abstract = title[2]
#     url = i.find_element(By.CSS_SELECTOR,"a.si-teaser__link").get_attribute('href')
    
#     new_row = {'pub_date':date, 'category':'None', 'title':title1, 'abstract':abstract, 'web_url':url}
#     swissinfoDateFrame = swissinfoDateFrame.append(new_row, ignore_index=True)

# row= row + 1
# driver.close()

# for i, j in swissinfoDateFrame.iterrows():
#     swissinfoSheet.write(row,col,j['pub_date'])
#     swissinfoSheet.write(row,col+1,j['category'])
#     swissinfoSheet.write(row,col+2,j['title'])
#     swissinfoSheet.write(row,col+3,j['abstract'])
#     swissinfoSheet.write(row,col+4,j['web_url'])
#     row = row +1
    
# swissinfoSheet.set_column(first_col=0, last_col=0,width = 30,cell_format = cell_format)
# swissinfoSheet.set_column(first_col=1, last_col=1,width = 70,cell_format = cell_format)
# swissinfoSheet.set_column(first_col=2, last_col=2,width = 100,cell_format = cell_format)
# swissinfoSheet.set_column(first_col=3, last_col=3,width = 130,cell_format = cell_format)
# swissinfoSheet.set_column(first_col=3, last_col=3,width = 130,cell_format = cell_format)
# swissinfoSheet.autofilter('A1:Z1')

##########################DONE############################
import re
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
rowtitleCount=1
worksheet = workbook.add_worksheet()

print("Current session is {}".format(driver.session_id))
    

sss = driver.get('https://www.doingbusiness.org/en/data/exploreeconomies/Colombia ')
s = driver.find_element(By.TAG_NAME,'text')
rank = s.text
yearD = driver.find_element(By.CLASS_NAME,'k-header')
print(yearD.text)
year = yearD.text
yearNumbers = re.findall('\d+', year )
#Collecting Data Ends 
#Store Data in Excel File Starts
worksheet.write('A'+str(rowtitleCount), 'السنة')
worksheet.write('A'+str(rowtitleCount+1),'مؤشر سهولة الأعمال',cell_format)
worksheet.set_column(1, 1, 10,)
row = row+2
col = 1
worksheet.write(row,1,2020)
worksheet.write(row+1,1,rank)
driver.close()
driver.quit()
workbook.close()


#######################################################################
driver.close()

# workbook.close()
print('2')
