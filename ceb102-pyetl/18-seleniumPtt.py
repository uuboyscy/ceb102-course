from selenium.webdriver import Chrome

driver = Chrome('./chromedriver')

driver.get('https://www.ptt.cc/bbs/index.html')

driver.find_element_by_class_name('board-name').click()
driver.find_element_by_class_name('btn-big').click()