from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import login, landing_page
import variables





def test_new_project_in_new_space():
    """
    Test will login to Posit Cloud, Creates new space, Creates a new RStudio project in the new space,
    Verify the IDE loads, Modify the project name and will verify project name modified sucessfully

    """
    # Login to Posit Cloud
    user_login = login.Login()
    user_login.login()

    # Create new space and verify space created
    user_landing_page = landing_page.LandingPage()
    user_landing_page.create_new_space(user_login.driver, variables.SPACENAME)
    assert user_login.driver.find_element(By.XPATH, "//div[text()='" + variables.SPACENAME + "']/..").is_displayed() == True, "Create space failed"

    # Create new project in the space, and verify IDE loads
    user_landing_page.create_rstudio_project(user_login.driver)
    try:
        WebDriverWait(user_login.driver, 10).until(EC.presence_of_element_located((By.ID, "contentIFrame")))
        element_found = True
    except:
        element_found = False
    assert element_found == True, "Project IDE didn't load successfully"

    # Rename the project and verify rename done sucessfully
    user_landing_page.rename_restudio_project(user_login.driver, variables.PROJECTNAME)
    user_login.driver.find_element(By.XPATH, "//div[text()='" + variables.SPACENAME + "']/..").click()
    user_login.driver.implicitly_wait(2)
    project_name = user_login.driver.find_element(By.CSS_SELECTOR, 'div[class="itemHeader"]').text
    assert project_name == variables.PROJECTNAME, f"Project name should be {variables.PROJECTNAME}, but it is {project_name}"

    # Delete the created space and verify space was deleted
    user_landing_page.delete_space(user_login.driver, variables.SPACENAME)
    try:
        WebDriverWait(user_login.driver, 1).until(EC.presence_of_element_located((By.XPATH, "//div[text()='" + variables.SPACENAME + "']/..")))
        element_found = True
    except:
        element_found = False

    assert element_found == False, "Delete space failed"

    # Close browser
    user_login.driver.quit()