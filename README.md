# posit-cloud-project

This project utlize Selenium with Python and Pytest framework.
The smoke test case perfrom login to Posit Cloud web application, create a new space, create a RStudio project in the space and finally deleting the space, logout and closing the browser.

Before running: Make sure CHROME_DRIVER_PATH variable on varaibles file, has correct value for the Chrome driver path.
For running the test case make sure we are on tests folder and execute: pytest test_smoke_after_build.py
