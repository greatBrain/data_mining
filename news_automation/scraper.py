#Copy of original web scrapper file.
import os
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager as manager
import pandas as pd


class Driver:
      def __init__(self):
          #For headless mode:   	 
          options = Options()
          options.add_argument('--headless=new')
          self.driver = webdriver.Chrome(service=Service(manager().install()), options=options)
          self.site_url = "https://www.thesun.co.uk/sport/football/"


          
class Scraper():
      def __init__(self):                 
          self.driver_instance = Driver()
          self.web_driver = self.driver_instance.driver
          self.web_driver.get(self.driver_instance.site_url)    
          print("Page URL:", self.web_driver.current_url)          
          print("Page Title:", self.web_driver.title)
      

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
          
          try:
          
            dataframe = pd.DataFrame(self.get_elements()) 

            #Get the executable app path:
            app_path = os.path.dirname(sys.executable)
            
            #Get current date and time to name the file:
            now = datetime.now()
            current_date = now.strftime("%d%m%Y")
            file_name = f'data_file_{current_date}.csv'  #Name news files as the current day

            #Save the new created file to the path, this is a better way to save the files no metter the OS used:
            file_path = os.path.join(app_path, file_name)          
            dataframe.to_csv(file_path)  

            self.driver_instance.quit()      

          except Exception as e:
              print(f"Error, the operation could not be completed: ", e, "try again.\n")
              self.web_driver.quit()   

      def auto_search(self):
          #Search for the search box, click on it an then send the text for what u are looking for
          pass
      


      def run(self):
          return self.export_data() 
      

class Main:
      def __init__(self):                 
          self.scrpaer = Scraper()

      def main(self) -> None:
          self.scrpaer.run()        
              

if __name__ == '__main__':
   main_class = Main()
   main_class.main()
