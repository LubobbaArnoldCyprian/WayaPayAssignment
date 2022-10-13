from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginPage:
    textbox_email_xpath = "//input[@id='email']"
    textbox_password_xpath = "//input[@id='pass']"
    button_login_xpath = "//button[.='Log in']"
    button_cookies_xpath = "//button[.='Only allow essential cookies']"

# Post Message
    button_initial_xpath = "//div[contains(@class,'x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou')]"
    textfield_content_xpath = "//div[@class='_1mf _1mj']"
    button_post_xpath = "//div[contains(@class,'x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67')]"
# Logout
    button_account_xpath = "//div[@class='x1n2onr6 x78zum5']"
    button_logout_xpath = "//span[normalize-space()='Log Out']"

    def __init__(self, driver):
        self.driver = driver
# Login

    def set_user_email(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickCookie(self):
        self.driver.find_element(By.XPATH, self.button_cookies_xpath).click()

# Post message

    def clickInitial(self):
        time.sleep(10)
        element = self.driver.find_element(By.XPATH, self.button_initial_xpath)
        element.click()

    def inputMessage(self, post):
        self.driver.find_element(By.XPATH, self.textfield_content_xpath).click()
        self.driver.find_element(By.XPATH, self.textfield_content_xpath).send_keys(post)

    def clickPost(self):
        self.driver.find_element(By.XPATH, self.button_post_xpath).click()

# click Logout
    def clickAccount(self):
        self.driver.find_element(By.XPATH, self.button_account_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
