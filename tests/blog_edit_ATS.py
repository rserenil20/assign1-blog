import unittest
import time
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.keys import Keys


class Blog_Edit_ATS(unittest.TestCase):

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

        # Locate and click the first blog post on the page.
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/h2/a").click()
        time.sleep(2)

        # Locate and click the edit button for the post.
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/a").click()
        time.sleep(2)

        # Find the title and replace the text.
        elem = driver.find_element_by_id("id_title")
        elem.send_keys(Keys.CONTROL + "a")
        elem.send_keys(Keys.DELETE)

        elem.send_keys("Test edit")
        # Find the post body and replace the text.
        elem = driver.find_element_by_id("id_text")
        elem.send_keys(Keys.CONTROL + "a")
        elem.send_keys(Keys.DELETE)
        elem.send_keys("This is a test edit of a post with selenium edited on " + str(datetime.now()))
        time.sleep(2)

        # Find and click the save button for the post.
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(5)
        assert "Blog Entry 1 Edited"
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
