from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utils.config as config
@given(u'I am on the login page')
def go_to_login(context):
    context.driver= webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.wait = WebDriverWait(context.driver, 10)
    

@when('I enter "{user_name}" in the user field')
def type_user(context,user_name):
    context.driver.maximize_window()
    time.sleep(1)
    context.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    context.driver.find_element(By.ID,"user-name").send_keys(user_name)
    


@when('I enter "{password}" in the password field')
def type_password(context,password):
    context.wait.until(EC.presence_of_element_located((By.ID, "password")))
    context.driver.find_element(By.ID,"password").send_keys(password)


@when('I press the Login button')
def click_in_o(context):
    status= context.driver.find_element(By.ID,"login-button")
    assert status.is_displayed()==True
    status.click()
    time.sleep(1)

@then('I should see the main page')
def step_impl(context):
    try:
        context.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'app_logo')))#'//*[@class="app_logo"')))
        text=context.driver.find_element(By.CLASS_NAME,'app_logo').text
    except:
        context.driver.close()
        assert False,"Test Failed"
    assert text=="Swag Labs"
    context.driver.close()



@then('I should see an error message.')
def step_impl(context):
    try:
        context.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'error-button')))#'//*[@class="app_logo"')))
        error_message=context.driver.find_element(By.CLASS_NAME,'error-button')

    except:
        context.driver.close()
        assert False,"Test Failed"
    assert error_message.is_displayed()==True
    context.driver.close()