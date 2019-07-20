from selenium.webdriver.common.by import By

class MainPageLocators(object):
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	LOGIN_REG = (By.CSS_SELECTOR, "#register_form")

class LoginCartPageLocators(object):
	LOGIN_BUT = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")