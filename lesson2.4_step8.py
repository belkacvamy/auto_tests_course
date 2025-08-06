from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
browser.find_element(By.CSS_SELECTOR, "#book").click()


browser.execute_script("window.scrollBy(0, 150);")

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)


browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

browser.find_element(By.CSS_SELECTOR, "#solve").click()

time.sleep(5)
browser.quit()