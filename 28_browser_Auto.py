from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element("link text", "Sign in")
time.sleep(1)
signin_link.click()

login_box = browser.find_element("id", "login_field")
login_box.send_keys("Kai-Nikola")
password_box = browser.find_element("id", "password")
password_box.send_keys("Nandu@9152545777")
password_box.submit()
assert "Kai-Nikola" in browser.page_source
time.sleep(5)