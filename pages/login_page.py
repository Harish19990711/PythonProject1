from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com")