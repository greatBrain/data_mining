#Price comparator between some super markets

import os
import sys
from datetime import datetime 
from selenium import webdriver as wbd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverMnanager as manager
import pandas as pd

class Driver:
      def __init__(self) -> None:
            #Defines the chrome driver, the options, the mode and the URLS to search. 
            options = Options()
            options.add_argument('--headless=new')
            self.driver = wbd.Chrome(service=Service(manager().install()), options=options)
            urls = ["https://supermercadosnacional.com/bebe/alimentacion-del-bebe?p=2", 
                    "https://sirena.do/products/category/alimentos-?page=1&limit=15&sort=1"
                   ]

class Scraper:
      def __init__(self) -> None:
          self.web_driver = Driver().driver
          