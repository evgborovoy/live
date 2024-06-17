import random
import allure
import pytest
from base.base_test import TestBase

@allure.feature("Profile Functionality")
class TestMyInfoFeature(TestBase):
    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_button()
        self.my_info_page.is_opened()
        self.my_info_page.change_name(f"test_name{random.randint(1, 100)}")
        self.my_info_page.save_changes()
        self.my_info_page.is_changes_saved()
        self.my_info_page.make_screenshot("Success")
