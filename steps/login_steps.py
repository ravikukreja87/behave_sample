from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'when a user opens Chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when(u'user navigates to tech canvass url \'https://techedge.techcanvass.co/Login.aspx\'')
def step_impl(context):
    context.driver.get('https://techedge.techcanvass.co/Login.aspx')


@when(u'user enters username in the login text box')
def step_impl(context):
    context.driver.find_element(By.ID,"txtLoginid").send_keys("test")


@when(u'user enters password in password text box')
def step_impl(context):
    context.driver.find_element(By.ID,"txtpassword").send_keys("test")


@when(u'clicks on the Login button')
def step_impl(context):
    context.driver.find_element(By.ID,"btnLogin").click()


@then(u'validate that title is \'Dashbard\' after I click on login button')
def step_impl(context):
    print('skip')


@then(u'validate heading of webpage to be \'My Courses\' after I click login button')
def step_impl(context):
    print('skip')
    context.driver.quit()

@then(u'validate that popup saying \'Please check your login credentials.\' is displayed')
def step_impl(context):
        login_fail_alert = context.driver.switch_to.alert
        print(login_fail_alert.text)
        login_fail_alert.accept()
        context.driver.quit()


