import allure
from allure_commons.types import AttachmentType

from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @allure.step("Open website")
    def go_to_website(self):
        self.driver.get('https://www.saucedemo.com')
        self.wait_until_visibility_css(self.login_button)
        allure.attach(self.driver.get_screenshot_as_png(), name="Main page", attachment_type=AttachmentType.PNG)

    @allure.step("Get text from button")
    def get_visible_button(self):
        self.wait_until_visibility_css(self.lang)
        x = self.find_by_css_selector(self.button_loggining).text
        return x

    @allure.step("Put login and password")
    def put_data_input(self, value):
        self.wait_until_clicable_css(self.login_input)
        login = self.find_by_css_selector(self.login_input)
        login.send_keys(value)
        self.wait_until_clicable_css(self.password_input)
        password = self.find_by_css_selector(self.password_input)
        password.send_keys("secret_sauce")
        allure.attach(self.driver.get_screenshot_as_png(), name="Login and Password text in inputs", attachment_type=AttachmentType.PNG)

    @allure.step("Click login button")
    def click_button(self):
        button = self.find_by_css_selector(self.login_button)
        button.click()
        self.wait_until_visibility_css(self.header_container)
        allure.attach(self.driver.get_screenshot_as_png(), name="Clicking login button", attachment_type=AttachmentType.PNG)

