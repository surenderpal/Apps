from selenium import webdriver
import time
import selenium

driver=webdriver.Chrome()
driver.get("http://youtube.com/")
time.sleep(5)
searchbox=driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('Hitesth Choudhary')

search_buttton=driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
search_buttton.click()
