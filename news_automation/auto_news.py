from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

#Website URL
web_url = "https://www.thesun.co.uk/sport/football"

#Path where is the chromedriver file
path = "/home/itachi/Documents/workspapces/automation/news_automation/chromedriver"


#Activatng the headless mode (Chrome will not start automatically)



#Service object who executes the webdriver
service = Service(executable_path=path)

#Webdriver 
driver = webdriver.Chrome(service=service)

#Open an instance of Chrome
driver.get(web_url)


#Get website HTML continers
container = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
sub_titles = []
links = []


#Getting specific attributes:
for data in  container:
    title = data.find_element(by="xpath", value='./a/h2').text
    titles.append(title)
    subtitle = data.find_element(by="xpath", value='./a/p').text
    sub_titles.append(subtitle)
    data_links = data.find_element(by="xpath", value='./a').get_attribute("href")
    links.append(data_links)

data_dict = {'titles': titles, 'subtitles': sub_titles, 'links':links}
df_headlines = pd.DataFrame(data_dict)

#Export to a CSV file (There are ,amy options like JSON excel txt, etc.)
df_headlines.to_csv('data_headlines.csv')

#Closing the driver
driver.quit()
