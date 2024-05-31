from selenium import webdriver
import time
import undetected_chromedriver as uc
from config import *
import importlib
from random import randint

def get_driver(website):
    configModule = importlib.import_module(name=f".{website}", package=CONFIG_DIR)
    options = webdriver.ChromeOptions()
    # adding some required headers
    headers = HEADERS
    headers['Referer'] = configModule.BASE_URL
    for key, value in headers.items():
        options.add_argument(f"--header={key}:{value}")
    options.page_load_strategy = configModule.PAGE_LOAD_STRATEGY
    driver = uc.Chrome(options=options, version_main=CHROME_VERSION)
    return driver

def scroll_by_some_height(driver, height):
    driver.execute_script(f"window.scrollBy(0, {height});")

def scroll_to_bottom_instantly(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def scroll_incrementally(driver, n_of_increments, scroll_amt = SCROLL_AMOUNT):
    for _ in range(n_of_increments):
        delay = randint(1, 3)
        time.sleep(delay)
        scroll_amt = randint(150, 400)
        print(scroll_amt)
        driver.execute_script(f"window.scrollBy(0, {scroll_amt});")

def scroll_to_bottom_incrementally(driver, scroll_amt=SCROLL_AMOUNT):
    while True:
        # scroll down the page by the specified amount
        driver.execute_script(f"window.scrollBy(0, {scroll_amt});")
        time.sleep(1)  # wait for the page to load
        
        # check if we've reached the bottom of the page
        scroll_height = driver.execute_script("return document.body.scrollHeight")
        window_height = driver.execute_script("return window.innerHeight")
        scroll_pos = driver.execute_script("return window.pageYOffset")
        
        if (scroll_height - (window_height + scroll_pos)) == 0:
            break