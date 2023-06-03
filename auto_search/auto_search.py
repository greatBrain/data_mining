#Automatic search for example in the search bar of any website
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 

# web driver manager: https://github.com/SergeyPirogov/webdriver_manager 
# will help us automatically download the web driver binaries 
# then we can use `Service` to manage the web driver's state. 
from webdriver_manager.chrome import ChromeDriverManager

#We say to Selenium to wait for 10 seconds to load dynamic content 
from selenium.webdriver.support.wait import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC 

options = wd.ChromeOptions()

options.add_argument("--headless")

#this returns the path web driver downloaded 
chrome_path = ChromeDriverManager().install()

chrome_service = Service(chrome_path) 
driver = wd.Chrome(service=chrome_service, options=options) 

url = "https://en.wikipedia.org/wiki/Main_Page" 

driver.get(url)





# find the search box 
search_box = driver.find_element(By.CSS_SELECTOR, "input.vector-search-box-input")

#click in the search box:
search_box.click()

#Search for the article i want, after clicking. Simulate typing in the element:
search_box.send_keys("Edgar Allan Poe")

# wait for 10 seconds for content to load. 
search_suggestions = wdw(driver, 10).until( 
	EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.mw-searchSuggest-link")) 
) 
# click to the first suggestion 
search_suggestions[0].click() 

# extract the data using same selectors as in beautiful soup. 
main_div = driver.find_element(By.CSS_SELECTOR, "div.mw-body-content") 
content_div = main_div.find_element(By.CSS_SELECTOR, "div.mw-parser-output") 
paragraphs = content_div.find_elements(By.TAG_NAME, "p") 

print(paragraphs)

driver.quit()