from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up WebDriver (automatically downloads correct chromedriver version)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open Gmail
    driver.get("https://www.gmail.com")
    
    # Maximize the window
    driver.maximize_window()

    # Wait until email input field is visible and enter email
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "identifierId"))
    )
    email_input.send_keys("kimkakiiza@gmail.com")

    # Click the Next button
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
    )
    next_button.click()

    # Get and validate the page title (after 5 seconds wait to allow navigation)
    WebDriverWait(driver, 5).until(lambda d: d.title.lower() != "gmail")

    actual_title = driver.title
    expected_title = "Gmail"

    if actual_title.lower() == expected_title.lower():
        print("Test Passed")
    else:
        print(f"Test Failed - Actual title: {actual_title}")

finally:
    # Close browser
    driver.quit()
