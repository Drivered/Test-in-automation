from pages.product_page import CartPage
from pages.base_page import BasePage

def test_guest_can_add_product_to_cart(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	page = CartPage(browser, link)
	page.open()
	page.test_add_cart()	