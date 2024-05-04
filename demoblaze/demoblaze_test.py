import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cart(self):
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(1536, 824)
    self.driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    assert self.driver.switch_to.alert.text == "Product added"
    self.driver.find_element(By.LINK_TEXT, "Dell i7 8gb").click()
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    assert self.driver.switch_to.alert.text == "Product added"
    self.driver.find_element(By.ID, "cartur").click()
  
  def test_categories(self):
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(1536, 824)
    element = self.driver.find_element(By.ID, "itemc")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "itemc").click()
    self.driver.find_element(By.LINK_TEXT, "Laptops").click()
    self.driver.find_element(By.LINK_TEXT, "Monitors").click()
    self.driver.find_element(By.LINK_TEXT, "Phones").click()
    self.driver.find_element(By.ID, "itemc").click()
  
  def test_check_cart_and_delete(self):
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(1536, 824)
    self.driver.find_element(By.ID, "cartur").click()
    self.driver.find_element(By.LINK_TEXT, "Delete").click()
  
  def test_other_pages(self):
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(1536, 824)
    self.driver.find_element(By.ID, "cartur").click()
    self.driver.find_element(By.LINK_TEXT, "About us").click()
    self.driver.find_element(By.CSS_SELECTOR, "#videoModal .btn").click()
    self.driver.find_element(By.LINK_TEXT, "Contact").click()
    element = self.driver.find_element(By.LINK_TEXT, "Contact")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "recipient-email").click()
    self.driver.find_element(By.ID, "recipient-email").send_keys("amine.gasmi.0123@gmail.com")
    self.driver.find_element(By.ID, "recipient-name").send_keys("amine gasmi")
    self.driver.find_element(By.ID, "message-text").click()
    self.driver.find_element(By.ID, "message-text").send_keys("aaaaa")
  
  def test_place_order(self):
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(1536, 824)
    self.driver.find_element(By.ID, "cartur").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active > .nav-link").click()
    self.driver.find_element(By.ID, "cartur").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("mohamed amine gasmi")
    self.driver.find_element(By.ID, "country").send_keys("Tunisia")
    self.driver.find_element(By.ID, "city").send_keys("Tunis")
    self.driver.find_element(By.ID, "card").click()
    self.driver.find_element(By.ID, "card").send_keys("aaaaa")
    self.driver.find_element(By.ID, "month").click()
    self.driver.find_element(By.ID, "month").send_keys("aaaaa")
    self.driver.find_element(By.ID, "year").send_keys("aaaaaa")
    self.driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".confirm").click()
    self.driver.find_element(By.ID, "cartur").click()
  
  def test_variables(self):
    self.vars["amine"] = "username"
    self.vars["azerty123"] = "password"
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(1536, 824)
    self.driver.find_element(By.ID, "signin2").click()
    self.driver.find_element(By.ID, "sign-username").click()
    self.driver.find_element(By.ID, "sign-username").send_keys(self.vars["username"])
    self.driver.find_element(By.ID, "sign-password").click()
    self.driver.find_element(By.ID, "sign-password").send_keys(self.vars["password"])
    self.driver.find_element(By.CSS_SELECTOR, "#signInModal .btn-primary").click()
