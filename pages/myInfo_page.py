from base.basePage import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MyInfoPage(BasePage):
    PAGE_URL = Links.MY_INFO_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    MIDDLE_NAME_FIELD = ("xpath", "//input[@name='middleName']")
    LAST_NAME_FIELD = ("xpath", "//input[@name='lastName']")
    SAVE_BUTTON = ("xpath", "//button[@type='submit']")

    def change_name(self, name):
        first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
        first_name_field.clear()
        assert first_name_field.get_attribute("value") == "", "Field is not empty for insert new value"
        first_name_field.send_keys(name)
        self.name = name

    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    def is_changes_saved(self):
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))