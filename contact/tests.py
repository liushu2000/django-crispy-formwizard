from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium import selenium, webdriver


class MySeleniumTests(LiveServerTestCase):
    #fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        #cls.selenium = webdriver.Chrome()
        super(MySeleniumTests, cls).setUpClass()

    #@classmethod
    #def tearDownClass(cls):
        #cls.selenium.quit()
        #super(MySeleniumTests, cls).tearDownClass()

    def test_jump_step(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/contacts_crispy/'))
        name_input = self.selenium.find_element_by_name("0-name")
        name_input.send_keys('Sean')
        email_input = self.selenium.find_element_by_name("0-email")
        email_input.send_keys('sean@msn.com')
        self.selenium.find_element_by_xpath('//input[@value="Next"]').click()
        self.selenium.find_element_by_name("2-phone")

        #self.selenium.implicitly_wait(5)
        time.sleep(2)

        self.selenium.find_element_by_name("wizard_goto_step").click()

        time.sleep(2)

        self.selenium.get('%s%s' % (self.live_server_url, '/contacts_crispy/'))
        name_input = self.selenium.find_element_by_name("0-name")
        name_input.send_keys('John')
        email_input = self.selenium.find_element_by_name("0-email")
        email_input.send_keys('john@msn.com')
        self.selenium.find_element_by_xpath('//input[@value="Next"]').click()
        self.selenium.find_element_by_name("0-memo")
        #self.assertIn("Phone", html.text)
