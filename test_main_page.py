from pages.main_page import MainPage
from selenium.webdriver.common.by import By

import time
user_language = "ru"

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

    el1 = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary")
    el2 = browser.find_element(By.NAME,"login_submit")
    print(f"Last =  {browser.current_url}")
    assert el1 == el2

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
