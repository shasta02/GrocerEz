# -*- coding: utf-8 -*-
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import threading


def check_all_numbers(s):
    nums = "0123456789$ ,"
    for c in s:
        if c not in nums and c != '\n' and c != ' ' and c != '\r':
            return False
    return True


def run_target(driver, user_product, user_zip):
    init_time = time.time()

    driver.implicitly_wait(30)

    driver.maximize_window()
    url = "https://www.target.com/store-locator/find-stores/" + user_zip
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
    time.sleep(2)

    url = "https://www.target.com/s?searchTerm=" + user_product + "&facetedValue=5zkty"
    driver.get(url)
    time.sleep(2)

    if re.match(user_product, 'orange'):
        driver.execute_script("window.scrollTo(0, 100)")
        driver.find_element_by_link_text("Clear filters").click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[4]/div[3]/div[2]/div/div[2]/div[2]/div/div/div[2]/fieldset[1]/label[2]/div').click()
        time.sleep(2)

    el = driver.find_element_by_tag_name('body')
    file = open('target.txt', 'w')

    file.write(el.text)

    run_time = time.time() - init_time
    print("Target driver done in", run_time)
    driver.close()
    file.close()

    file2 = open('target.txt', 'r')
    count = 0

    target_ans = open('target_ans.txt', 'w')
    max2 = 0
    for line in file2:
        if count == 1 and not re.match("third party advertisement", line) and not re.match("sponsored", line):
            target_ans.write(line)
            count = 0
        elif line[0] == '$':
            target_ans.write(line)
            max2 += 1
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
        elif re.match("Check stores", line):
            count = 1
        if max2 == 2:
            break
    target_ans.close()
    file2.close()

    run_time = time.time() - init_time
    print("Target done in", run_time)


def run_walmart(driver, user_product, user_zip):
    init_time = time.time()

    driver.implicitly_wait(30)

    driver.maximize_window()
    driver.get("https://www.walmart.com/")
    time.sleep(5)
    driver.find_element_by_xpath("//div[6]/div/div[3]/button").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(user_zip)
    time.sleep(0.5)
    driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(Keys.ENTER)
    time.sleep(3)
    url = "https://www.walmart.com/search/?query=" + user_product
    driver.get(url)
    time.sleep(3)

    el = driver.find_element_by_tag_name('body')
    file = open('walmart.txt', 'w')

    file.write(el.text)

    run_time = time.time() - init_time
    print("Walmart driver done in", run_time)
    driver.close()
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

    run_time = time.time() - init_time
    print("Walmart done in", run_time)


def run_wholefoods(driver, user_product, user_zip):
    init_time = time.time()

    driver.implicitly_wait(30)

    driver.maximize_window()
    driver.get("https://products.wholefoodsmarket.com/")

    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/input').click()

    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/input').clear()

    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/input').send_keys(
        user_zip)

    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]').click()

    url = "https://products.wholefoodsmarket.com/search?sort=relevance&text=" + user_product
    driver.get(url)

    file = open('wholefoods.txt', 'w', encoding='utf-8')
    element = driver.find_element_by_tag_name('body')

    file.write(element.text)
    run_time = time.time() - init_time
    print("Wholefoods driver done in", run_time)
    driver.close()
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

    run_time = time.time() - init_time
    print("Wholefoods done in", run_time)


def run_amazon(driver, user_product, user_zip):
    init_time = time.time()

    driver.implicitly_wait(30)

    driver.maximize_window()

    driver.get("https://www.amazon.com/alm/storefront?almBrandId=QW1hem9uIEZyZXNo")

    driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[1]/div/span/a").click()

    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]").click()

    driver.find_element_by_css_selector("#GLUXZipUpdateInput").send_keys(user_zip)

    driver.find_element_by_css_selector("#GLUXZipUpdate > span > input").click()

    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/span/span").click()

    url = "https://www.amazon.com/s?k=" + user_product + "&i=amazonfresh"
    driver.get(url)

    price1 = driver.find_element_by_css_selector("#search > div.s-desktop-width-max.s-desktop-content.s-opposite"
                                                 "-dir.sg-row > "
                                                 "div.sg-col-20-of-24.s-matching-dir.sg-col-28-of-32.sg-col-16-of"
                                                 "-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg"
                                                 "-col-24-of-28 > div > span:nth-child(5) > div:nth-child(1) > "
                                                 "div:nth-child(1) > div > span > div > div > div:nth-child(4) > "
                                                 "div > div > a > span.a-price > span:nth-child(2)").text
    price2 = driver.find_element_by_css_selector("#search > div.s-desktop-width-max.s-desktop-content.s-opposite"
                                                 "-dir.sg-row > "
                                                 "div.sg-col-20-of-24.s-matching-dir.sg-col-28-of-32.sg-col-16-of"
                                                 "-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg"
                                                 "-col-24-of-28 > div > span:nth-child(5) > div:nth-child(1) > "
                                                 "div:nth-child(2) > div > span > div > div > div:nth-child(4) > "
                                                 "div > div > a > span:nth-child(1) > span:nth-child(2)").text

    file = open('amazon.txt', 'w', encoding='utf-8')
    element = driver.find_element_by_tag_name('body')

    file.write(element.text)
    run_time = time.time() - init_time
    print("Amazon driver done in", run_time)
    driver.close()
    file.close()

    i = 0
    for c in price1:
        if c == '\n':
            break
        i += 1
    if i < len(price1) - 1:
        price1 = price1[:i] + "." + price1[i + 1:]

    i = 0
    for c in price2:
        if c == '\n':
            break
        i += 1
    if i < len(price2) - 1:
        price2 = price2[:i] + "." + price2[i + 1:]

    file2 = open('amazon.txt', 'r')

    amazon_ans = open('amazon_ans.txt', 'w', encoding='utf-8')
    count = 0
    nums = 0
    price = False
    for line in file2:
        if "Show " in line:
            count = 1
        elif "Previous" in line:
            break
        elif count == 1 and "$" not in line and not check_all_numbers(line) and len(line) > 3:
            amazon_ans.write(line)
            nums += 1
        if nums == 1 and not price:
            amazon_ans.write(price1 + "\n")
            price = True
        if nums == 2:
            amazon_ans.write(price2)
            break
    amazon_ans.close()
    file2.close()

    run_time = time.time() - init_time
    print("Amazon done in", run_time)


user_product = "apples"
user_zip = "95123"

driver1 = webdriver.Chrome(executable_path=r'C:\Users\NARAVENK\Downloads\chromedriver_win32 (1)\chromedriver.exe')
driver2 = webdriver.Chrome(executable_path=r'C:\Users\NARAVENK\Downloads\chromedriver_win32 (1)\chromedriver2.exe')
driver3 = webdriver.Chrome(executable_path=r'C:\Users\NARAVENK\Downloads\chromedriver_win32 (1)\chromedriver3.exe')
driver4 = webdriver.Chrome(executable_path=r'C:\Users\NARAVENK\Downloads\chromedriver_win32 (1)\chromedriver4.exe')

thread1 = threading.Thread(target=run_target, args=[driver1, user_product, user_zip])
thread2 = threading.Thread(target=run_walmart, args=[driver2, user_product, user_zip])
thread3 = threading.Thread(target=run_wholefoods, args=[driver3, user_product, user_zip])
thread4 = threading.Thread(target=run_amazon, args=[driver4, user_product, user_zip])

thread1.start()
thread2.start()
thread3.start()
thread4.start()
