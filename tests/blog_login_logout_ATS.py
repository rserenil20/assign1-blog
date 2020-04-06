import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_Login__Logout_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        # Use username and password to login to the website.
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(5)
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(2)

        # Locate and click the logout button in the top right of the page
        elem = driver.find_element_by_xpath("//*[@id=\"user-tools\"]/a[3]").click()
        time.sleep(2)

        # Locate and click the Log in again link on the page
        elem = driver.find_element_by_xpath("//*[@id=\"content\"]/p[2]/a").click()
        assert "Logged Out"
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
