from selenium import webdriver

driver = webdriver.Chrome(executable_path = 'chromedriver.exe')

wkn_numbers = ["TT9PDA8",]

driver.get('https://www.hsbc-zertifikate.de/home/details#!/isin:DE000'+wkn_numbers[0])
hide_window = driver.find_element_by_id("c-disclaimer-dialog-button")
hide_window.click()

driver.implicitly_wait(1) #this is fucking OBNOXIOUS

test = driver.find_element_by_xpath("//*[contains(text(), 'Geldkurs (1 Stücke)')]/following-sibling::td")

print(test.text)
driver.quit()
