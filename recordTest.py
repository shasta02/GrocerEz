# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time


class Target(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\NARAVENK\Downloads\chromedriver_win32 (1)\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_target(self):
        user_product = 'banana'
        user_zip = '95129'
        driver = self.driver

        """driver.get("https://www.target.com/")
        driver.find_element_by_xpath("//button[@id='storeId-utilityNavBtn']/div[2]").click()
        driver.find_element_by_id("zipOrCityState").click()
        driver.find_element_by_id("zipOrCityState").clear()
        driver.find_element_by_id("zipOrCityState").send_keys(user_zip)
        driver.find_element_by_id("zipOrCityState").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("(//button[@type='button'])[9]").click()
        driver.find_element_by_id("search").click()
        driver.find_element_by_id("search").clear()
        driver.find_element_by_id("search").send_keys(user_product)
        driver.find_element_by_id("search").send_keys(Keys.ENTER)"""

        driver.get("https://www.target.com/s?searchTerm=toilet+paper")
        driver.find_element_by_xpath(
            "//div[@id='mainContainer']/div[3]/div[2]/div/div/div[3]/div[2]/ul/li/div/div[2]/div/div/div/div[5]/div/div/div/div/div/div/button").click()
        time.sleep(5)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
