from selenium import webdriver

driver = webdriver.Firefox(executable_path='C:\\Users\\User\\Documents\\geckodriver.exe')

# driver.get('https://www.youtube.com/')
driver.get('http://192.168.99.100:5000/')
data = driver.find_element_by_xpath("/html/body").get_attribute("textContent").strip(' \n\t')
print(data)

driver.close()



# driver = webdriver.Firefox(executable_path='C:\\Users\\User\AppData\Local\Temp\geckodriver-v0.24.0-win64')
# driver.get('http://inventwithpython.com')