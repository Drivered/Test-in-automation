from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
	def basket_login_cart(self):
		self.button_login_cart()
		self.is_not_element_present(*CartPageLocators.CART_BLANK)
		self.should_not_be_cart()
		self.text_be_cart()
		
	def button_login_cart(self):
		link = self.browser.find_element(*CartPageLocators.CART_BTN)
		link.click()

	def should_not_be_cart(self):
		assert self.is_not_element_present(*CartPageLocators.CART_BLANK), \
			"The product is present in the cart"
	
	def text_be_cart(self):
		link = self.browser.find_element(*CartPageLocators.CART_TEXT)
		assert link.text, "Text not in basket"