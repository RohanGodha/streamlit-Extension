from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Start the web driver (adjust the path to your driver executable)
driver = webdriver.Chrome('path/to/chromedriver')

# Open YouTube
driver.get('https://www.youtube.com')

# Search for a video (modify the query to your desired video)
search_box = driver.find_element_by_xpath('//input[@id="search"]')
search_box.send_keys('Your Video Title' + Keys.RETURN)

# Play the video
play_button = driver.find_element_by_xpath('//button[@aria-label="Play"]')
play_button.click()

# Increase the volume (modify the number of times to increase/decrease volume)
volume_up_button = driver.find_element_by_xpath('//button[@aria-label="Increase volume"]')
for _ in range(3):
    volume_up_button.click()

# Decrease the volume
volume_down_button = driver.find_element_by_xpath('//button[@aria-label="Decrease volume"]')
for _ in range(3):
    volume_down_button.click()

# Close the browser
driver.quit()
