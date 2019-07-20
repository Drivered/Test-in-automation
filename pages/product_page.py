from .base_page import BasePage
from .locators import LoginCartPageLocators

class CartPage(BasePage):
	def test_add_cart(self):
		self.button_add_cart()
		self.solve_quiz_and_get_code()
	
	def button_add_cart(self):
		link = self.browser.find_element(*LoginCartPageLocators.LOGIN_BUT)
		link.click()