from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_chrome_options():
    options = Options()
    options.add_argument('--remote-allow-origins=*')
    options.add_argument('--disable-search-engine-choice-screen')
    options.add_argument('user-data-dir=ChromeProfile')
    #options.add_argument('user-data-dir=/Users/pkaramanova/Library/Application Support/Google/Chrome/Default')
    options.page_load_strategy = 'normal'
    return options

def create_driver():
    chrome_options = get_chrome_options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver