from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : r'C:\Users\Samiullah\Videos\.idea'}
chrome_options.add_experimental_option('prefs', prefs)


driver = webdriver.Chrome(r"C:\Users\Samiullah\Downloads\chromedriver", options=chrome_options)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/")
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(.,'File Upload')]").click();
time.sleep(2)

driver.find_element_by_id("file-upload").send_keys(r"C:\Users\Samiullah\Pictures\Sami_assign")
time.sleep(2)

driver.find_element_by_id("file-submit").send_keys(Keys.ENTER)
time.sleep(2)

driver.get("http://the-internet.herokuapp.com/")
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(.,'File Download')]").click();
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(.,'file.png')]").click();
time.sleep(2)

driver.get("http://the-internet.herokuapp.com/")
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(.,'Multiple Windows')]").click();
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(.,'Click Here')]").click();
time.sleep(2)
