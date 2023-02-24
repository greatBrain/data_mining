from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as manager
import pandas as pd

web_url = "https://www.thesun.co.uk/sport/football/"

#instead of passing manually the path of the web browser driver, we use the ChromeDriverManager to 
#install the correct version tha match with the current browser version.
driver = webdriver.Chrome(service=Service(manager().install()))

driver.get(web_url)

#Find elements using Xpath:
elements_container = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')


#Lists of elements to be added to a dictionary
titles = []
subtitles = []
links = []


#Iterate over el_container to print every element found using 'find_element':
for data in elements_container:
    #title = data.find_element(by="xpath", value="./a/h2").text
    subtitle = data.find_element(by="xpath", value="./a/p").text
    link = data.find_element(by="xpath", value="./a").get_attribute("href")

    #titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

data = {"subtitles":subtitles, "links":links}

#Write the data to a dataframe:
dataframe = pd.DataFrame(data)

#Export the dataframe to a file (may be to: JSON, CSV, to the clipboard, etc.):
dataframe.to_csv('data.csv')