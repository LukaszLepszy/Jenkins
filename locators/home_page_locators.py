from selenium.webdriver.common.by import By

class HomePageLocators:
    home_page = "https://www.saucedemo.com/"
    lang = (By.CSS_SELECTOR, "div[class ='l-header__lang']")
    button_loggining = "a[title ='Logowanie i rezerwacje'][class='btn']"
    login_input = "input[id='user-name']"
    password_input = "input[id='password']"
    login_button = "input[id='login-button']"
    header_container = "div[class='header_secondary_container']"
    header_text = "span[class='title']"