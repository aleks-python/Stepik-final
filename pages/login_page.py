from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_SUBMIT = (By.NAME, "login_submit")

    REG_EMAIL = (By.ID, "id_registration-email")
    REG_PASS1 = (By.ID, "id_registration-password1")
    REG_PASS2 = (By.ID, "id_registration-password2")
    REG_SUBMIT = (By.NAME, "registration_submit")

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login username input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login submit input is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True