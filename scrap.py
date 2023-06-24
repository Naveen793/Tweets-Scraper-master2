# Import Libraries

import re
import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# Library for different Browsers

# Firefox
#from selenium.webdriver import Firefox

# Google Chrome
from selenium.webdriver import Chrome

# Microsoft Edge
# from msedge.selenium_tools import Edge, EdgeOptions
# Driver for different Browsers

# Firefox
#driver = Firefox()

# Google Chrome
driver = Chrome()

# Microsoft Edge
# options = EdgeOptions()
# options.use_chromium = True
# driver = Edge(options=options)
driver.get(url="https://twitter.com/i/flow/login")

your_name = "@NaveenV45395753"
your_pass = "Bunnynav2005"
sleep(5)
username = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
username.send_keys(your_name)
username.send_keys(Keys.RETURN)
sleep(5)
ok_btn = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
sleep(5)
ok_btn.click()
password = driver.find_element(By.XPATH, '//input[@name="password"]')
password.send_keys(your_pass)
password.send_keys(Keys.RETURN)
sleep(3)
search = driver.find_element(
    By.XPATH, './/input[@data-testid="SearchBox_Search_Input"]')
search.send_keys("@apecoin #100X")
search.send_keys(Keys.RETURN)

# Scrapping Tweets

post_urls = []
post_times = []
post_texts = []
comment_counts = []
retweet_counts = []
like_counts = []

tweets = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
ass=1
while True:
    for tweet in tweets:
        ass+=1
       

        post_time = tweet.find_element(
            By.XPATH, "//time").get_attribute('datetime')
        post_times.append(post_time)

        post_text = tweet.find_element(
            By.XPATH, '//div[@data-testid="tweetText"]').text
        post_texts.append(post_text)

        comment_count = driver.find_element(
            By.XPATH, ".//div[@data-testid='reply']").text
        comment_counts.append(comment_count)

        retweet_count = driver.find_element(
            By.XPATH, ".//div[@data-testid='retweet']").text
        retweet_counts.append(retweet_count)

        like_count = driver.find_element(
            By.XPATH, ".//div[@data-testid='like']").text
        like_counts.append(like_count)
        print(post_time,like_count,'hii')

    

    tweet_count = len(post_times)
    if ass == 5:
        break


tweet_count