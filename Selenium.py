
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time

# Set the GeckoDriver path
gecko_path = "/snap/bin/geckodriver"
service = Service(gecko_path)

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(service=service)

try:
    # Step 1: Open the OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    time.sleep(3)  # Wait for page to load

    # Step 2: Enter Username & Password
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")

    username.send_keys("Admin")  # Default username
    password.send_keys("admin123")  # Default password

    # Step 3: Click Login Button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    time.sleep(5)  # Wait for login to complete

    # Step 4: Verify Successful Login
    try:
        dashboard_text = driver.find_element(By.TAG_NAME, "h6").text
        if "Dashboard" in dashboard_text:
            print("Login successful!")
        else:
            print("Login failed!")
    except:
        print("Login failed!")


finally:
    # Step 7: Close the browser
    driver.quit()
