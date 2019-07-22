from selenium.webdriver.common.by import By

class MainPageLocators(object):
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	LOGIN_REG = (By.CSS_SELECTOR, "#register_form")

class LoginCartPageLocators(object):
	ADD_BUT = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
	NAME_ITEM = (By.CSS_SELECTOR, "h1")
	PRICE_ITEM = (By.CSS_SELECTOR, "p.price_color")
	PRICE_FINAL = (By.CSS_SELECTOR, "#messages p strong")
	NAME_FINAL = (By.CSS_SELECTOR, "#messages strong")
	MESSAGES = (By.CSS_SELECTOR, "#messages")

class BasePageLocators(object):
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class CartPageLocators(object):
	CART_BTN = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
	CART_BLANK = (By.CSS_SELECTOR, "h2 .col-sm-6.h3")
	CART_TEXT = (By.CSS_SELECTOR, "p")

class RegistrationPageLocators(object):
	EMAIL_USER = (By.CSS_SELECTOR, "#id_registration-email")
	PASSWORD1_USER = (By.CSS_SELECTOR, "#id_registration-password1")
	PASSWORD2_USER = (By.CSS_SELECTOR, "#id_registration-password2")
	BTN_REG = (By.CSS_SELECTOR, "[value ='Register']")