from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time, variables



class LandingPage(object):

    def create_new_space(self, driver, space_name):
        """
        Create a new space and refresh the page
        self: The LandingPage object
        driver: Selenium webdrvier
        space_name: Space name string

        """
        driver.find_element(By.CSS_SELECTOR, 'button[class="newSpace menuItem"]').click()
        self.name = driver.find_element(By.ID, 'name')
        self.name.clear()
        self.name.send_keys(space_name)
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        create_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, variables.CREATE_BTN)))
        create_button.click()
        driver.refresh()
    
    def delete_space(self, driver, space_name):
        """
        Delete a space
        self: The LandingPage object
        driver: Selenium webdrvier
        space_name: Space name for deleation

        """
        driver.find_element(By.XPATH, "//div[text()='" + space_name + "']/..").click()
        driver.find_element(By.XPATH, '//button[@class="action moreActions"]/..').click()
        driver.find_element(By.ID, 'headerDeleteSpaceButton').click()
        space_to_delete_text_element = driver.find_element(By.ID, 'deleteSpaceTest')
        space_to_delete_text_element.send_keys("Delete " + space_name)
        delete_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "deleteSpaceSubmit")))
        delete_button.click()
        time.sleep(1)
    
    def create_rstudio_project(self, driver):
        """
        Creates RStudio project
        self: The LandingPage object
        driver: Selenium webdrvier

        """
        driver.find_element(By.CSS_SELECTOR, 'div[class="actionBar inline showTitles"]').click()
        driver.find_element(By.CSS_SELECTOR, 'button[title="New RStudio Project"]').click()
        driver.implicitly_wait(30)

    def rename_restudio_project(self, driver, project_name):
        """
        Rename RStudio project
        self: The LandingPage object
        driver: Selenium webdrvier
        project_name: Project string to modify name to

        """
        project_name_element = driver.find_element(By.ID, 'currentLocation')
        # create action chain object
        action = ActionChains(driver)
        action.move_to_element(project_name_element)
        action.click()
        action.send_keys(project_name)
        action.send_keys(Keys.ENTER)
        action.perform()
        driver.implicitly_wait(3)

    def logout(self, driver):
        """
        Logout from the system

        """
        driver.find_element(By.ID, 'currentUser').click()
        driver.find_element(By.CSS_SELECTOR, 'a[class="menuItem logout"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'main')))


