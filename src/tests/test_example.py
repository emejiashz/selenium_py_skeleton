import pytest
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest


@pytest.mark.usefixtures("init_driver")
class TestExample(BaseTest):

    def test_example(self):
        self.driver.find_element(By.NAME, "q").send_keys("pytest")
        self.driver.find_element(By.NAME, "btnK").click()
