#Copy of original web scrapper file.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as manager
import pandas as pd


class Driver:
      def __init__(self):
          self.driver = webdriver.Chrome(service=Service(manager().install()))
          self.site_url = "https://www.thesun.co.uk/sport/football/"          
      
      def get_site_url(self):
          return self.driver.get(self.site_url)


class Main:
      def __init__(self):
     	    #Create the Driver class instance:
          self.web_driver = Driver()

      def get_all_data(self):
          elements_container =  self.web_driver.driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')
          return elements_container.text

      
# main_class = Main()
# print(main_class.get_all_data())
      