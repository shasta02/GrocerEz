# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

def check_all_numbers(s):
    nums = "0123456789$ ,"
    for c in s:
        if c not in nums and c != '\n' and c != ' ' and c != '\r':
            return False
    return True

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
        user_product = 'apples'
        user_zip_code = '95129'

        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.amazon.com/alm/storefront?almBrandId=QW1hem9uIEZyZXNo")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[1]/div/span/a").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]").click()
        time.sleep(3)
        driver.find_element_by_css_selector("#GLUXZipUpdateInput").send_keys(user_zip_code)
        time.sleep(3)
        driver.find_element_by_css_selector("#GLUXZipUpdate > span > input").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/span/span").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[3]/div[1]/input").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[3]/div[1]/input").send_keys(user_product)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input").click()
        time.sleep(5)

        file = open('amazon.txt', 'w', encoding='utf-8')
        element = driver.find_element_by_tag_name('body')
        time.sleep(1)

        file.write(element.text)
        time.sleep(2)
        file.close()

        file2 = open('amazon.txt', 'r', encoding='utf-8')

        amazon_ans = open('amazon_ans.txt', 'w', encoding='utf-8')
        count = 0
        price = False
        for line in file2:
            if "Show " in line:
                count = 1
            elif "Previous" in line:
                break
            elif count == 1 and "$" not in line and not check_all_numbers(line) and len(line) > 3:
                amazon_ans.write(line)
                price = False
            elif count == 1 and line[0] == "$" and not price:
                amazon_ans.write(line)
                price = True
        amazon_ans.close()
        file2.close()

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
