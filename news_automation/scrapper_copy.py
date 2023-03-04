#Copy of original web scrapper file.
import os
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
          self.driver_instance = Driver()
          self.web_driver = self.driver_instance.driver
          self.web_driver.get(self.driver_instance.site_url)          

      #Get all data from the web:   
      def get_all_data(self):
          elements_container = self.web_driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')
          return elements_container

      #Search inside all data element by element:
      def get_elements(self):
          try:
             #title = [data.find_element(by="xpath", value="./a/h2").text for data in self.get_all_data()]
             subtitle = [data.find_element(by="xpath", value="./a/p").text for data in self.get_all_data()]
             links = [data.find_element(by="xpath", value="./a").get_attribute("href") for data in self.get_all_data()]

             data = {"subtitles":subtitle, "links":links}
             return data
          
          except Exception as e:
                 return False          


      def export_data(self):
          
          if self.get_elements() !=False:
             dataframe = pd.DataFrame(self.get_elements())       

             while True:            
                if not os.path.isdir('data_files'):        
                   os.mkdir('data_files')                                       
                dataframe.to_csv('data_files/data.csv')
                break                

          else:
             print("An exception has ocurred, the operation could not be completed. Try again.\n")


if __name__ == '__main__':
   main_class = Main()
   main_class.export_data()
