             
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.parse
import time

# Get raw input from user
raw_url = input("Enter the target URL with fragment payload: ")

# Encode the fragment part
if '#' in raw_url:
    base, frag = raw_url.split('#', 1)
    encoded_url = base + '#' + urllib.parse.quote(frag)
else:
    encoded_url = raw_url

# Setup Chrome (non-headless to capture alert if needed)
options = Options()
# Comment out headless to see alert visually
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)
driver.get(encoded_url)

time.sleep(5)  # Wait for JS to execute

# Save screenshot
driver.save_screenshot("dom_xss_proof.png")
print("📸 Screenshot saved as dom_xss_proof.png")

driver.quit()

