# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from flask import Flask, render_template, request

from app import getValue


class AppDynamicsJob(unittest.TestCase):
    app = Flask(__name__)
    i1 = 'a'
    i2 = 'a'
    i3 = 'a'
    z = 'a'

    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\NARAVENK\Downloads\chromedriver_win32 (1)\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    @app.route('/')
    def index(self):
        return render_template('index.html')

    @app.route('/', methods=['POST'])
    def getValue(self):
        i1 = request.form['item1']
        i2 = request.form['item2']
        i3 = request.form['item3']
        z = request.form['zip']

    if __name__ == '__main__':
        app.run(debug=True)

    def test_app_dynamics_job(self, i1, z):
        user_product = i1
        user_zip = z

        driver = self.driver
        driver.maximize_window()
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
