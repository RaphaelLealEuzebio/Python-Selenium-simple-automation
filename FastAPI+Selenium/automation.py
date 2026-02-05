from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def google_search(term: str):
    # selenium aqui
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    time.sleep(3)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(term)
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)
    title = driver.title
    driver.quit()

    return title