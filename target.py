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
        user_product = 'orange'
        user_zip = '95129'

        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.target.com/")
        driver.find_element_by_xpath("(//a[contains(text(),'Find Stores')])[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        time.sleep(2)
        driver.find_element_by_id("zipcode").click()
        time.sleep(2)
        driver.find_element_by_id("zipcode").clear()
        driver.find_element_by_id("zipcode").send_keys(user_zip)
        time.sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        time.sleep(2)
        driver.find_element_by_id("search").click()
        time.sleep(2)
        driver.find_element_by_id("search").clear()
        time.sleep(2)
        driver.find_element_by_id("search").send_keys(user_product)
        time.sleep(2)
        driver.find_element_by_id("search").send_keys(Keys.ENTER)
        driver.execute_script("window.scrollTo(0, 100)")
        if re.match(user_product, 'orange') : clearfilt = driver.find_element_by_link_text("Clear filters").click()

        time.sleep(5)

        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[4]/div[3]/div[2]/div/div[2]/div[2]/div/div/div[2]/fieldset[1]/label[2]/div').click()

        # driver.find_element_by_xpath(
        # "/html/body/div[1]/div/div[4]/div[3]/div[2]/div/div[2]/div[2]/div/div/div[3]/fieldset[1]/label[2]/div").click()

        el = driver.find_element_by_tag_name('body')
        print(el.text)
        file = open('target.txt', 'w')

        file.write(el.text)
        file.close()

        file2 = open('target.txt', 'r')
        count = 0

        target_ans = open('target_ans.txt', 'w')
        max2 = 0
        for line in file2:
            if count == 1 and not re.match("third party advertisement", line) and not re.match("sponsored", line):
                target_ans.write(line)
                count = 0
                max2 = max2 + 1
            elif re.match("Sort byRelevance", line):
                count = 1
            elif re.match("Add for delivery", line):
                count = 1
            elif re.match("Add for shipping", line):
                count = 1
            elif re.match("Choose options", line):
                count = 1
            elif re.match("Add to cart", line):
                count = 1
            elif re.match("Add for pickup", line):
                count = 1
            if max2 == 2:
                break
        target_ans.close()
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
