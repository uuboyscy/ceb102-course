from selenium.webdriver import Chrome
import time

url = 'https://www.dcard.tw/f'

driver = Chrome('./chromedriver')

driver.get(url)

driver.find_element_by_tag_name('input').send_keys('攝影')

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/form/button[2]').click()
# driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div[1]/div/div/form/button[2]')
time.sleep(3)
driver.execute_script('var s = document.documentElement.scrollTop=10000')
time.sleep(3)
driver.execute_script('var s = document.documentElement.scrollTop=1')
time.sleep(3)
driver.execute_script('var s = document.documentElement.scrollTop=10000')
