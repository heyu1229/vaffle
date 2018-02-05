from selenium import webdriver
import unittest,time


class MyTest(unittest.TestCase):

    def setUp(self):
        time.sleep(2)

        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--proxy-server=socks5://172.100.10.6:1080')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)

        '''
        binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
        self.driver = webdriver.Firefox(firefox_binary=binary)

        '''
        self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver

    def tearDown(self,driver):
        driver.quit()