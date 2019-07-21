from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import math
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import LoginCartPageLocators
from .locators import BasePageLocators
# import time

class BasePage(object):	
	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)
	
	def open(self):
		self.browser.get(self.url)

	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True

	def solve_quiz_and_get_code(self):
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		# time.sleep(120)
		try:
			alert = self.browser.switch_to.alert
			print("Your code: {}".format(alert.text))
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")
				
	def is_disappeared(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout, 1, TimeoutException).\
				until_not(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return False
		return True
		
	def should_not_be_success_message_disappeared(self):
		assert self.is_disappeared(*LoginCartPageLocators.NAME_FINAL), \
			"Success message is presented, but should not be"
	
	def is_not_element_present(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True
		return False
	
	def should_not_be_success_message(self):
		assert self.is_not_element_present(*LoginCartPageLocators.NAME_FINAL), \
			"Success message is presented, but should not be"
	
	def go_to_login_page(self):
		link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
		link.click()

	def should_be_login_link(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
	
	def go_to_basket(self):
		link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
		link.click()