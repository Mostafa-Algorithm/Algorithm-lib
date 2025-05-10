# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DC
import undetected_chromedriver as uc
from time import sleep

class WebDriver:
    time = 30

    def __init__(self, undetected: bool = True, incognito: bool = True, maxmize: bool = False, proxy: str = None, disable_gpu: str = False) -> None:
        capabilities = DC.CHROME

        if undetected: options = uc.ChromeOptions()
        else: options = webdriver.ChromeOptions()

        if disable_gpu:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')

        if incognito: options.add_argument("--incognito")

        if proxy: options.add_argument('--proxy-server=%s' % proxy)

        if undetected:
            self.driver = uc.Chrome(
                service=Service(ChromeDriverManager().install()),
                desired_capabilities=capabilities,
                options=options
            )
        else:
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                desired_capabilities=capabilities,
                options=options
            )
        
        if maxmize: self.driver.maximize_window()
        else: self.driver.set_window_size(800, 600)

    def get_element_by_id(self, id: str, time: int = time) -> object : return self.get_element(By.ID, id, time)

    def get_element_by_name(self, name: str, time: int = time) -> object : return self.get_element(By.NAME, name, time)

    def get_element_by_class(self, class_name: str, time: int = time) -> object : return self.get_element(By.CLASS_NAME, class_name, time)

    def get_element_by_tag(self, tag: str, time: int = time) -> object : return self.get_element(By.TAG_NAME, tag, time)

    def get_element_by_xpath(self, path: str, time: int = time) -> object : return self.get_element(By.XPATH, path, time)

    def get_element_by_selector(self, selector: str, time: int = time) -> object : return self.get_element(By.CSS_SELECTOR, selector, time)

    def get_element_by_aria_label(self, label: str) -> object : return self.driver.find_elements_by_css_selector("[aria-label=%s]" % label)

    def get_element(self, by: By, element: str, time: int = time) -> object : return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((by, element)))

    def get_element_by_link_text(self, element) -> object  : return self.driver.find_element(By.LINK_TEXT, element)

    def get_elements_by_class(self, class_name, time=time) -> object  : return self.get_elements(By.CLASS_NAME, class_name, time)

    def get_elements(self, by, elements, time=time) -> object  : return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located((by, elements)))

    def get_driver(self) -> object : return self.driver

    def open(self, url: str) -> None  : self.driver.get(url=url)

    def close(self) -> None : self.driver.quit()

    def set_input_data(self, input: object, data: str, click: bool = False) -> None :
        input.clear()
        input.send_keys(data)
        if click:
            input.send_keys(Keys.ENTER)

    def get_attribute(self, element: object, attribute: str) -> str: return element.get_attribute(attribute)

    def get_url(self) -> str : return self.driver.current_url

    def switch_to(self, frame, default: bool = False) -> None:
        if default:
            self.driver.switch_to.default_content()
            sleep(0.5)
        self.driver.switch_to.frame(frame)

    def execute_js(self, code: str) -> None : self.driver.execute_script(code)

    def get_logs(self) -> any : return self.driver.get_log()

    def alert_accept(self) -> None : self.driver.switch_to.alert.accept()
    
    def select_by_value(self, element, value: str) -> None : Select(element).select_by_value(value)
    
    def select_by_index(self, element, index: int) -> None : Select(element).select_by_index(index)

class Exceptions:
    NSWE = NoSuchWindowException
    TOE = TimeoutException
    WDE = WebDriverException
    NSEE = NoSuchElementException
    ECIE = ElementClickInterceptedException
    ENIE = ElementNotInteractableException
    IE = IndentationError