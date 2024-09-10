from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class MakeChrome:
    def make_chrome(link):
        path_to_extension = r'M:\Dev\sports_predict\uBOLite_0.1.22.9205.mv3'
        path_to_driver = r'M:\Dev\sports_predict\chromedriver_win32\chromedriver.exe'

        chrome_options = Options()
        chrome_options.add_argument('load-extension=' + path_to_extension)

        driver = webdriver.Chrome(path_to_driver, options=chrome_options)
        driver.create_options()
        driver.get(link)
        return(driver)