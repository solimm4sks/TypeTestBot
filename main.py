from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://typing-speed-test.aoeu.eu/')
sleep(1)

inputBox = driver.find_element_by_id('input')
while True:
    #try:
    inputBox.send_keys(driver.find_element_by_xpath('//span[@id="currentword"]').text + ' ')
    #except:
    #   pass