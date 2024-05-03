import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver (Ensure you have chromedriver installed and in PATH)
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.example.com")

# Wait for the search input field to be visible
search_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "q"))
)

# Perform actions on the web page
search_input.send_keys("example search query" + Keys.RETURN)

# Wait for search results to load
time.sleep(2)  # Replace with WebDriverWait or other explicit wait strategies if needed

# Assert conditions
assert "Example Domain" in driver.title, "Title does not match expected value"

search_results = driver.find_elements_by_css_selector("h3")  # Assuming search results are in <h3> tags
assert len(search_results) > 0, "No search results found"

# Close the browser
driver.quit()

