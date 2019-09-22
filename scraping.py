from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import datetime

# Die Zeit News scraping : https://www.zeit.de/news/index
class NewsScraping():

    def __init__(self):
        self.driver= webdriver.Chrome(executable_path='/User/Driver/chromedriver')
        self.df = pd.DataFrame()
        self.article_list= []
        self.times_list= []
        self.thema_list= []
        self.quelle_list=[]


    def compile_data(self):

        # Artikel:
        article = self.driver.find_elements_by_xpath("//span[@class='newsteaser__title']")
        self.article_list = [value.text for value in article]

        # Zeit:
        time = self.driver.find_elements_by_xpath("//time[@class='newsteaser__time']")
        self.times_list = [value.text for value in time]

        #Thema:
        thema= self.driver.find_elements_by_xpath("//span[@class='newsteaser__kicker']")
        self.thema_list = [value.text for value in thema]

        #Quelle
        quelle= self.driver.find_elements_by_xpath("//span[@class='newsteaser__product']")
        self.quelle_list = [value.text for value in quelle]


        for i in range(len(self.article_list)):
            try:

                self.df.loc[i, 'time'] = self.times_list[i]

            except Exception as e:

                print('Zeit konnte nicht gefunden werden ')
            try:
                self.df.loc[i, 'article'] = self.article_list[i]

            except Exception as e:

                print('Artikel konnte nicht gefunden werden ')

            try:
                self.df.loc[i, 'thema'] = self.thema_list[i]

            except Exception as e:

                print('Thema konnte nicht gefunden werden ')

            try:
                self.df.loc[i, 'quelle'] = self.quelle_list[i]

            except Exception as e:

                print('Quelle konnte nicht gefunden werden')

        print('Excel Sheet created!')

# EXECUTE
writer = pd.ExcelWriter("Zeit.xlsx")

driver = newsscraping()

link = 'https://www.zeit.de/news/index?date=2019-09-17' # https://www.zeit.de/news/index

driver.driver.get(link)

driver.compile_data()

# AUF NÄCHSTE SEITE KLICKEN
# vorheriger_tag = driver.driver.find_element_by_xpath("//a[@class='pager__button pager__button--next']")
#
# vorheriger_tag.click()
#
# driver.compile_data()

driver.df.to_excel(writer, sheet_name='die_Zeit_17-09-19')

writer.save()

# Scrolling
# 1. Scroll down page by pixel
# driver.execute_script("window.scrollBy(0,1000)","")

# 2. Scroll down page till the element is visible
# stuff = driver.find_element_by_xpath('xpath')
# driver_execute_script("arguments[0].scrollIntoView();", flag)

# 3. Scroll down page till end
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
