from selenium import webdriver

webdriverChrome = webdriver.Chrome("Drivers/Chrome/chromedriver.exe")
#webdriverEdge = webdriver.Edge("Drivers/Edge/msedgedriver.exe")

webdriver.get("google.com")