# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time, re
from selenium.webdriver.support import expected_conditions as cond
import threading
from selenium.webdriver.chrome.options import Options

 
def check_all_numbers(s):
    nums = "0123456789$ ,"
    for c in s:
        if c not in nums and c != '\n' and c != ' ' and c != '\r':
            return False
    return True


def run_target(driver, user_product, user_zip):
    init_time = time.time()

    waiter = WebDriverWait(driver, 10)

    url = "https://www.target.com/store-locator/find-stores/" + user_zip
    driver.get(url)
    element = waiter.until(cond.element_to_be_clickable((By.CSS_SELECTOR, "#mainContainer > "
                                                                          "div:nth-child(2) > div "
                                                                          "> "
                                                                          "div.Row-uds8za-0.gUzGLa"
                                                                          ".h-padding-h-default > "
                                                                          "div:nth-child(1) > div "
                                                                          "> div > div > button")))
    element.click()

    url = "https://www.target.com/s?searchTerm=" + user_product + "&facetedValue=5zkty"
    driver.get(url)

    time.sleep(7)

    if re.match(user_product, 'orange'):
        element = waiter.until(
            cond.element_to_be_clickable((By.LINK_TEXT, "Clear filters")))
        element.click()
        element = waiter.until(
            cond.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[4]/div[3]/div[2]/div/div[2]/div["
                                                    "2]/div/div/div[2]/fieldset[1]/label[2]/div")))
        element.click()

    el = driver.find_element_by_tag_name("body")
    file = open('target.txt', 'w')

    file.write(el.text)

    run_time = time.time() - init_time
    print("Target driver done in", run_time)
    # driver.close()
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

    waiter = WebDriverWait(driver, 10)

    driver.get("https://www.walmart.com/")
    element = waiter.until(cond.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div["
                                                                   "2]/div/div[3]/div/div/div[2]/div[3]/button")))
    element.click()
    element = waiter.until(cond.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[4]/div["
                                                                   "2]/div/div[2]/div[2]/div[1]/form/div[1]/input")))
    element.click()
    element.clear()
    element.send_keys(user_zip)
    element.send_keys(Keys.ENTER)
    time.sleep(2)
    url = "https://www.walmart.com/search/?query=" + user_product
    driver.get(url)

    time.sleep(7)

    el = driver.find_element_by_tag_name('body')
    file = open('walmart.txt', 'w')

    file.write(el.text)

    run_time = time.time() - init_time
    print("Walmart driver done in", run_time)
    # driver.close()
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

    waiter = WebDriverWait(driver, 10)

    driver.get("https://products.wholefoodsmarket.com/")

    element = waiter.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div['
                                                                   '1]/div[2]/div[2]/div['
                                                                   '2]/div/div[1]/input')))
    element.click()
    element.clear()
    element.send_keys(user_zip)
    element = waiter.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div['
                                                                   '1]/div[2]/div[2]/div[2]/div['
                                                                   '2]/div[1]/div[1]')))
    element.click()

    url = "https://products.wholefoodsmarket.com/search?sort=relevance&text=" + user_product
    driver.get(url)

    time.sleep(7)

    file = open('wholefoods.txt', 'w', encoding='utf-8')
    element = driver.find_element_by_tag_name('body')

    file.write(element.text)
    run_time = time.time() - init_time
    print("Wholefoods driver done in", run_time)
    # driver.close()
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

    waiter = WebDriverWait(driver, 10)

    driver.get("https://www.amazon.com/alm/storefront?almBrandId=QW1hem9uIEZyZXNo")

    element = waiter.until(cond.element_to_be_clickable((By.XPATH, '/html/body/div['
                                                                   '1]/header/div/div[2]/div['
                                                                   '1]/div/span/a')))
    element.click()

    element = waiter.until(cond.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div['
                                                                   '1]/div/div[2]/div[3]/div['
                                                                   '2]/div[1]/div[1]')))
    element.click()
    driver.find_element_by_css_selector("#GLUXZipUpdateInput").send_keys(user_zip)

    element = waiter.until(cond.element_to_be_clickable((By.CSS_SELECTOR, '#GLUXZipUpdate > span > '
                                                                          'input')))
    element.click()

    element = waiter.until(cond.element_to_be_clickable((By.CSS_SELECTOR, '#GLUXZipUpdate > span > '
                                                                          'input')))
    element.click()

    element = waiter.until(cond.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div['
                                                                   '2]/span/span')))
    element.click()
    time.sleep(2)
    url = "https://www.amazon.com/s?k=" + user_product + "&i=amazonfresh"
    driver.get(url)

    time.sleep(7)

    file = open('amazon.txt', 'w', encoding='utf-8')
    element = driver.find_element_by_tag_name('body')

    file.write(element.text)
    run_time = time.time() - init_time
    print("Amazon driver done in", run_time)
    # driver.close()
    file.close()

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
            price = True
        if nums == 2:
            break
    amazon_ans.close()
    file2.close()

    run_time = time.time() - init_time
    print("Amazon done in", run_time)


user_product = "peppers"
user_zip = "10001"

init_time_overall = time.time()

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(
            executable_path=r'C:\Users\NARAVENK\Downloads\chromedriver_win32 (1)\chromedriver.exe')
driver.maximize_window()

run_target(driver, user_product, user_zip)
run_walmart(driver, user_product, user_zip)
run_amazon(driver, user_product, user_zip)
run_wholefoods(driver, user_product, user_zip)

driver.close()

print("Total run time:", (time.time() - init_time_overall))