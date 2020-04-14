# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\NARAVENK\Downloads\chromedriver_win32 (1)\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        user_product = "oranges"
        user_zip = "95129"

        driver = self.driver
        #driver.maximize_window()
        time.sleep(2)
        driver.get("https://www.walmart.com/")
        time.sleep(5)
        driver.find_element_by_xpath("//div[6]/div/div[3]/button").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(user_zip)
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_id("global-search-input").click()
        driver.find_element_by_id("global-search-input").clear()
        time.sleep(2)
        driver.find_element_by_id("global-search-input").send_keys(user_product)
        driver.find_element_by_id("global-search-form").submit()
        time.sleep(5)

        el = driver.find_element_by_tag_name('body')
        print(el.text)
        file = open('walmart.txt', 'w')

        file.write(el.text)
        file.close()

        file2 = open('walmart.txt', 'r')
        count = 0
        max2 = 0
        walmart_ans = open('walmart_ans.txt', 'w')
        for line in file2:
            if count == 1:
                walmart_ans.write(line)
                max2 = max2 + 1
                count = 0
            if re.match("Product Title", line):
                count = 1
            if max2 == 2:
                break
        file2.close()
        walmart_ans.close()

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
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
