import allure
from selenium.webdriver import Keys

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MyInfoPage(BasePage):
    PAGE_URL = Links.MY_INFO_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    MIDDLE_NAME_FIELD = ("xpath", "//input[@name='middleName']")
    LAST_NAME_FIELD = ("xpath", "//input[@name='lastName']")
    SAVE_BUTTON = ("xpath", "//button[@type='submit']")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def change_name(self, name):
        with allure.step(f"Change name on '{name}'"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name_field.send_keys(Keys.COMMAND + "A")
            first_name_field.send_keys(Keys.BACKSPACE)
            first_name_field.send_keys(name)
            self.name = name

    @allure.step("Click on submit button for save changes")
    def save_changes(self):
        button = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON), "Button 'save' is not clickable")
        button.click()

    @allure.step("Changes has been saved")
    def is_changes_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name),
                        "Name has not been changed")
