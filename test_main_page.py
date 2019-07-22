from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import CartPageLocators
from pages.base_page import BasePage
import pytest
from pages.cart_page import CartPage

@pytest.mark.login_guest
class TestLoginFromMainPage(object):
	# @pytest.fixture(scope="function", autouse=True)
	# def setup(self):
		# self.product = ProductFactory(title = "Best book created by robot")
		# # создаем по апи
		# self.link = self.product.link
		# yield
		# # после этого ключевого слова начинается teardown
		# # выполнится после каждого теста в классе
		# # удаляем те данные, которые мы создали 
		# self.product.delete()

	def test_guest_can_go_to_login_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
		page = MainPage(browser, link)
		page.open()
		page.go_to_login_page()
		login_page = LoginPage(browser, browser.current_url)
		login_page.should_be_login_page()

	def test_guest_should_see_login_link(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
		page = MainPage(browser, link)
		page.open()
		page.should_be_login_link()

	def test_guest_cant_see_product_in_cart_opened_from_main_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com"
		page = CartPage(browser, link)
		page.open()
		page.basket_login_cart()