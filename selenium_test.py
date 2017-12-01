#coding=utf-8
from selenium import webdriver


driver =webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.zhihu.com/")

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/a[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/span").click()

account=driver.find_element_by_name("account")
account.clear()
account.send_keys(u"账号")

password=driver.find_element_by_name("password")
password.clear()
password.send_keys(u"密码")

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[2]/button").click()

driver.quit()
