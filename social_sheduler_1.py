
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, time
import requests
import time as t


current_time = datetime.now().time()



hours = current_time.hour
minutes = current_time.minute
seconds = current_time.second

current_time_updated = time(hours, minutes, seconds)
# specific_time = time(13, 32, seconds)  # Replace with your specific time

specific_time = time(hours, minutes, seconds)  # Replace with your specific time

# print(current_time)
print(specific_time)
print(current_time_updated)

if current_time_updated < specific_time:
    print("The current time is earlier than the specific time.")
elif current_time_updated > specific_time:
    print("The current time is later than the specific time.")
else:
    print("The current time is the same as the specific time.")



time_not_same = True
if current_time_updated == specific_time:
    time_not_same = False
    service = Service("C:Development\chromedriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.twitter.com")
    # driver.maximize_window()
    t.sleep(15)
    login = driver.find_element(By.CLASS_NAME, 'css-4rbku5')
    login.click()
    t.sleep(5)
    email_entry = driver.find_element(By.CLASS_NAME, 'r-30o5oe')
    email_entry.send_keys("Your email")
    email_entry.send_keys(Keys.ENTER)
    t.sleep(5)
    password_entry = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password_entry.send_keys("Your Password")
    password_entry.send_keys(Keys.ENTER)
    # time.sleep(5)
    # log_in_button = driver.find_element(By.CLASS_NAME, "css-901oao")
    # log_in_button.click()
    def get_quote():
        quote = f"It is {current_time_updated} and my bot is tweeting on my behalf"
        return quote
    t.sleep(5)
    tweet_text = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
    tweet_text.send_keys(get_quote())
    print(f"Tweet has been written successfully!")
    t.sleep(5)
    tweet_button = driver.find_element(By.XPATH, "//*[text()='Tweet']")
    driver.execute_script("arguments[0].click();", tweet_button)
    print(f"{tweet_button.text} Tweet has been tweeted successfully!")

if time_not_same:
    print("Time is not the same s the mentioned time!!!!")
    
