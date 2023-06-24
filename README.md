# BBC Bangla News Tweets Scraper

Scraping Tweets from **BBC Bangla News** Twitter Profile. It can be used for any Twitter Profile/Handle.

## Table of Contents

-   [My Tools](#my-tools)
-   [Depencdencies](#dependencies)
-   [How to run locally](#how-to-run-locally)
-   [Challenges and Solution](#challenges-and-solutions)
-   [References](#references)

## My Tools

-   Linux
-   geckodriver
-   Firefox
-   VSCode

## Dependencies

-   Python (3.10.6)
-   Selenium (4.6.0)
-   Pandas (1.5.1)

## How to run locally

1. First, install the **Chrome/Firefox/MS Edge webdriver** in your PC and add the path in Environment variable. <br>

1. Clone the Repository <br>
   ```
   git clone https://github.com/MusfiqDehan/Tweets-Scraper.git
   ```

1. Change the directory <br>
   ```
   cd Tweets-Scraper
   ```

1. Initialize and Run Virtual Environments <br>
   ```
   pipenv install && pipenv shell
   ```

1. Install the dependencies <br>
   ```
   pip3 install -r requirements.txt
   ```

1. Run the app <br>
   ```
   python3 tweets_scraper/main.py
   ```

## Challenges and Solutions

-   We cannot directly scrape from https://twitter.com/bbcbangla this page
-   First we have to login to twitter(https://twitter.com/i/flow/login) otherwise after 10-15 seconds login modal will appear and it will interrupt the scraping process
-   So, I have written the scripts to automate the login process also.
-   But during my 15-20 trial 3-4 times only I was able to login directly and most of the times I have to fill the recaptcha.
-   Automating recaptcha is very difficult, after some research, I found out that if we use some paid service like 2captcha we might be able to automate recaptcha also. However, it is not affordable for me now.
-   So, for now we have manually fill the recaptcha
-   For step by step process, I have used Jupyter Notebook.

## References

-   [Selenium](https://www.selenium.dev/)
-   [Selenium-Python](https://selenium-python.readthedocs.io/)
