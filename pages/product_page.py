from .base_page import BasePage
from .locators import LoginCartPageLocators

class ProductPage(BasePage):
	def test_add_cart(self):
		self.button_add_cart()
		self.solve_quiz_and_get_code()
		self.name_of_item()
		self.price_of_item()
	
	def button_add_cart(self):
		link = self.browser.find_element(*LoginCartPageLocators.ADD_BUT)
		link.click()
	
	def name_of_item(self):
		name_item = self.browser.find_element(*LoginCartPageLocators.NAME_ITEM)
		name_final_item = self.browser.find_element(*LoginCartPageLocators.NAME_FINAL)
		assert name_item.text == name_final_item.text, "Name is Fail"
	
	def price_of_item(self):
		price_item = self.browser.find_element(*LoginCartPageLocators.PRICE_ITEM)
		price_final_item = self.browser.find_element(*LoginCartPageLocators.PRICE_FINAL)
		assert price_item.text == price_final_item.text, "Price is Fail"