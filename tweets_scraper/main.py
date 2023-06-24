# Import Libraries

import json
import pandas as pd
import sqlite3
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Library for different Browsers

# Firefox
from selenium.webdriver import Firefox

# Google Chrome
# from selenium.webdriver import Chrome

# Microsoft Edge
# from msedge.selenium_tools import Edge, EdgeOptions

# Driver for different Browsers

# Firefox
driver = Firefox()

# Google Chrome
# driver = Chrome()

# Microsoft Edge
# options = EdgeOptions()
# options.use_chromium = True
# driver = Edge(options=options)


def main():
    driver.get(url="https://twitter.com/i/flow/login")

    your_name = str(input("Enter your username: "))
    your_pass = getpass("Enter your password")

    username = driver.find_element(By.XPATH, "//input[@name='text']")
    username.send_keys(your_name)
    username.send_keys(Keys.RETURN)
    sleep(3)

    ok_btn = driver.find_element(By.XPATH, "//span[contains(text(),'OK')]")
    sleep(5)
    ok_btn.click()

    # In this position,
    # If recaptcha appears we have to manually solve it
    # Manually Solve Recaptcha

    password = driver.find_element(By.XPATH, '//input[@name="password"]')
    password.send_keys(your_pass)
    password.send_keys(Keys.RETURN)
    sleep(3)

    # Search BBC News
    search = driver.find_element(
        By.XPATH, './/input[@data-testid="SearchBox_Search_Input"]')

    search.send_keys("bbcbangla")
    search.send_keys(Keys.RETURN)

    bbc_profile = driver.find_element(By.LINK_TEXT, 'BBC News Bangla')
    bbc_profile.click()

    # Scrapping Tweets
    post_urls = []
    post_times = []
    post_texts = []
    comment_counts = []
    retweet_counts = []
    like_counts = []

    tweets = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")

    while True:
        for tweet in tweets:

            post_url = tweet.find_element(
                By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[3]/a').get_attribute('href')
            post_urls.append(post_url)

            post_time = tweet.find_element(
                By.XPATH, ".//time").get_attribute('datetime')
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

        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        sleep(3)
        tweets = driver.find_elements(
            By.XPATH, "//article[@data-testid='tweet']")

        tweet_count = len(list(set(post_urls)))
        if tweet_count >= 20:
            break

    # Taking unique values
    unique_post_urls = list(set(post_urls))
    unique_post_times = list(set(post_times))
    unique_post_texts = list(set(post_texts))
    unique_comment_counts = list(set(comment_counts))
    unique_retweet_counts = list(set(retweet_counts))
    unique_like_counts = list(set(like_counts))

    # Creating dictionary by combining all
    all_tweets_dict = []

    for i, (url, time, text, comment_cnt, retweet_cnt, like_cnt
            ) in enumerate(zip(
            unique_post_urls,
            unique_post_times,
            unique_post_texts,
            unique_comment_counts,
            unique_retweet_counts,
            unique_like_counts)
    ):

        i = i + 1
        tweet_dict = {}

        tweet_dict["id"] = i
        tweet_dict["post_url"] = url
        tweet_dict["post_time"] = time
        tweet_dict["post_text"] = text
        tweet_dict["comment_count"] = comment_cnt
        tweet_dict["retweet_count"] = retweet_cnt
        tweet_dict["like_count"] = like_cnt

        all_tweets_dict.append(tweet_dict)

    # Converting Dictionary into json
    with open("DATA.json", "w") as output_file:
        json.dump(all_tweets_dict, output_file, ensure_ascii=False)

    # Lists to DataFrame
    df = pd.DataFrame(zip(
        unique_post_urls,
        unique_post_times,
        unique_post_texts,
        unique_comment_counts,
        unique_retweet_counts,
        unique_like_counts), columns=['post_urls', 'post_times', 'post_texts', 'comment_counts', 'retweet_counts', 'like_counts'])

    # DataFrame to Excel
    df.to_excel("twitter_data.xlsx", index=False)
    twitter_data = pd.read_excel('twitter_data.xlsx', header=0)

    # Excel to Database
    db_conn = sqlite3.connect("twitter_data.db")
    cur = db_conn.cursor()

    cur.execute(
        """
    CREATE TABLE twitter_data (
        post_urls TEXT NOT NULL,
        post_times TEXT NOT NULL,
        post_texts TEXT NOT NULL,
        comment_counts INTEGER,
        retweet_counts INTEGER,
        like_counts INTEGER,
    );

    """
    )

    twitter_data.to_sql('twitter_data', db_conn,
                        if_exists='append', index=False)


# Calling main function
if __name__ == '__main__':
    main()
