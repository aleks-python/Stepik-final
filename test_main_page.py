import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    print(f"Start =  {browser.current_url}")
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    print(f"Second =  {browser.current_url}")
    el1 = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary")
    el2 = browser.find_element(By.NAME,"login_submit")
    print(f"Last =  {browser.current_url}")
    assert el1 == el2
    time.sleep(10)
