import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

web_url = "https://www.thesun.co.uk/sport/football/"

#The chromedriver was added to a sym link: 
chrome_driver_path = "/usr/bin/chromedriver"

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(web_url)

#Find elements using Xpath:
el_container = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

#Iterate over el_container to print every element found using 'find_element':
for el in el_container:
    subtitle = el.find_element(by="xpath", value='./a/h2').text

print(subtitle)
