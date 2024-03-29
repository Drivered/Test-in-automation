from .base_page import BasePage
from .locators import LoginPageLocators, RegistrationPageLocators
import time


class LoginPage(BasePage):
	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):
		assert "login" in self.browser.current_url, "Login link is not presented"

	def should_be_login_form(self):
		assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form fail"

	def should_be_register_form(self):
		assert self.browser.find_element(*LoginPageLocators.LOGIN_REG), "Login reg form fail"
	
	def register_new_user(self, email, password):
		reg = self.browser.find_element(*RegistrationPageLocators.EMAIL_USER)
		reg.send_keys(email)
		user_password = self.browser.find_element(*RegistrationPageLocators.PASSWORD1_USER)
		user_password.send_keys(password)
		user_password2 = self.browser.find_element(*RegistrationPageLocators.PASSWORD2_USER)
		user_password2.send_keys(password)
		
	def register_button(self):
		btn = self.browser.find_element(*RegistrationPageLocators.BTN_REG)
		btn.click()