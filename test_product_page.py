import pytest
import time
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.locators import LoginCartPageLocators
from pages.cart_page import CartPage
from pages.login_page import LoginPage

# product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
# urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	page = ProductPage(browser, link)
	page.open()
	page.test_add_cart()
	
def test_guest_cant_see_success_message(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.is_not_element_present(*LoginCartPageLocators.NAME_FINAL)
	page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()
	
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()

@pytest.mark.need_review	
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = CartPage(browser, link)
	page.open()
	page.basket_login_cart()

@pytest.mark.reg_guest	
class TestUserAddToCartFromProductPage(object):
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
		page = LoginPage(browser, link)
		email = str(time.time()) + "@fakemail.org"
		password = str(time.time())
		page.open()
		page.register_new_user(email, password)
		page.register_button()
		page.should_be_authorized_user()

	@pytest.mark.need_review
	def test_user_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		page = ProductPage(browser, link)
		page.open()
		page.is_not_element_present(*LoginCartPageLocators.NAME_FINAL)
		page.should_not_be_success_message()
		
	def test_user_can_add_product_to_cart(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
		page = ProductPage(browser, link)
		page.open()
		page.test_add_cart()
