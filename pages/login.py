from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import variables


class Login(object):
    
    s = Service(variables.CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=s)

    def __init__(self):
        self.driver.maximize_window()

    def login(self):
        """
        Login to Posit Cloud web application
        self: The Login object

        """
        self.driver.get("https://posit.cloud/")
        self.driver.find_element(By.CSS_SELECTOR, 'a[class="menuItem"]').click()
        email = self.driver.find_element(By.NAME, 'email')
        email.send_keys(variables.USERNAME)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.driver.implicitly_wait(3)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(variables.PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()