from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import login, landing_page
import variables, pytest



@pytest.fixture()
def setup():
    pytest.user_login = login.Login()
    pytest.user_landing_page = landing_page.LandingPage()

    yield
    # Delete the created space and verify space was deleted
    if pytest.user_login.driver.find_element(By.XPATH, "//div[text()='" + variables.SPACENAME + "']/..").is_displayed():
        pytest.user_landing_page.delete_space(pytest.user_login.driver, variables.SPACENAME)
    
    # Logout and close browser
    pytest.user_landing_page.logout(pytest.user_login.driver)
    pytest.user_login.driver.quit()



def test_new_project_in_new_space(setup):
    """
    Test will login to Posit Cloud, Creates new space, Creates a new RStudio project in the new space,
    Verify the IDE loads, Modify the project name and will verify project name modified sucessfully

    """
    # Login to Posit Cloud
    pytest.user_login.login()

    # Create new space and verify space created
    
    pytest.user_landing_page.create_new_space(pytest.user_login.driver, variables.SPACENAME)
    assert pytest.user_login.driver.find_element(By.XPATH, "//div[text()='" + variables.SPACENAME + "']/..").is_displayed() == True, "Create space failed"

    # Create new project in the space, and verify IDE loads
    pytest.user_landing_page.create_rstudio_project(pytest.user_login.driver)
    pytest.user_login.driver.switch_to.frame(pytest.user_login.driver.find_element(By.ID, 'contentIFrame'))
    try:
        WebDriverWait(pytest.user_login.driver, 10).until(EC.presence_of_element_located((By.ID, "rstudio")))
        element_found = True
    except:
        element_found = False
    assert element_found == True, "Project IDE didn't load successfully"
    pytest.user_login.driver.switch_to.default_content()

    # Rename the project and verify rename done sucessfully
    pytest.user_landing_page.rename_restudio_project(pytest.user_login.driver, variables.PROJECTNAME)
    pytest.user_login.driver.find_element(By.XPATH, "//div[text()='" + variables.SPACENAME + "']/..").click()
    project_name = pytest.user_login.driver.find_element(By.CSS_SELECTOR, 'div[class="itemHeader"]').text
    assert project_name == variables.PROJECTNAME, f"Project name should be {variables.PROJECTNAME}, but it is {project_name}"