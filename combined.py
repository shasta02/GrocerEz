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
        user_product = 'bananas'
        user_zip = '95123'

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
        ################################################################## WALMART CODE NEXT

        driver = self.driver
        time.sleep(2)
        driver.get("https://www.walmart.com/")
        time.sleep(8)
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
            if re.match("Sorry, no products matched", line):
                walmart_ans.write(line)
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

        ############################################################# Whole Foods Code


        driver = self.driver
        driver.get("https://products.wholefoodsmarket.com/")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/input').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/input').clear()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/input').send_keys(
            user_zip)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div[1]/div[1]/input').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div[1]/div[1]/input').send_keys(user_product)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div[1]/div[1]/input').send_keys(Keys.ENTER)

        time.sleep(5)

        file = open('wholefoods.txt', 'w', encoding='utf-8')
        element = driver.find_element_by_tag_name('body')
        time.sleep(1)

        file.write(element.text)
        time.sleep(2)
        print(element.text)
        file.close()

        file2 = open('wholefoods.txt', 'r')

        wholefoods_ans = open('wholefoods_ans.txt', 'w', encoding='utf-8')
        count = 0
        max2 = 0
        for line in file2:
            if line == '0 Results For:':
                wholefoods_ans.write('no stock')
                break
            elif "Get in-store pricing, sales and product info" in line:
                break
            elif count == 1 and line.upper() != line and line[0] != '$':
                wholefoods_ans.write(line)
                count = 0
                max2 = max2 + 1
            elif line == "Brand (A-Z)":
                count = 1
            elif line[0] == '$':
                count = 1
            if max2 == 2:
                break
        wholefoods_ans.close()
        file2.close()


        ##################################################################### Amazon Code


        driver = self.driver
        driver.get("https://www.amazon.com/alm/storefront?almBrandId=QW1hem9uIEZyZXNo")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[1]/div/span/a").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]").click()
        time.sleep(3)
        driver.find_element_by_css_selector("#GLUXZipUpdateInput").send_keys(user_zip)
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
            if re.match("No results for", line):
                amazon_ans.write(line)
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
