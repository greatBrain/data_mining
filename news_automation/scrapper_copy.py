#Copy of original web scrapper file.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as manager
import pandas as pd


class Driver:
      def __init__(self):
          self.driver = webdriver.Chrome(service=Service(manager().install()))
          self.site_url = "https://www.thesun.co.uk/sport/football/"


class Main:
      def __init__(self):
     	  #Create the Driver class instance:
     	  self.driver_instance = Driver()
     	  self.web_driver = self.driver_instance.driver
     	  self.web_driver.get(self.driver_instance.site_url)

      def get_all_data(self):
          elements_container = self.web_driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')
          return elements_container

      def print_data(self):
          subtitle = [data.find_element(by="xpath", value="./a/p").text for data in self.get_all_data()]
          return subtitle

if __name__ == '__main__':
   main_class = Main()
   print(main_class.print_data())
