from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace this with the full path to your chromedriver
driver_path = r"C:\Users\ADMIN\Downloads\chromedriver-win64\chromedriver.exe"  # For Windows
# driver_path = "/usr/local/bin/chromedriver"  # For macOS/Linux

# Set up the driver with the specified path
service = Service(driver_path)
options = Options()
options.add_argument("--start-maximized")  # optional

driver = webdriver.Chrome(service=service, options=options)

# Open a website
driver.get("https://www.geeksforgeeks.org")

# Wait and click the button (customize selector as needed)
try:
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/div/ul/li[3]/a")))  # change this!
    button.click()
    print("Button clicked!")
except Exception as e:
    print(f"Error: {e}")

# Optional wait
time.sleep(5)

# Close the browser
driver.quit()
