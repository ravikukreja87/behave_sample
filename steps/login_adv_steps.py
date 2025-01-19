from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'I am on the Login Page')
def step_impl(context):
    context.driver = webdriver.Chrome()



@when(u'I enter {username} and {password}')
def step_impl(context, username, password):
    context.driver.get('https://techedge.techcanvass.co/Login.aspx')
    context.driver.find_element(By.ID, "txtLoginid").send_keys(username)
    context.driver.find_element(By.ID, "txtpassword").send_keys(password)


@when(u'I click on login button')
def step_impl(context):
    context.driver.find_element(By.ID,"btnLogin").click()
    context.driver.quit()