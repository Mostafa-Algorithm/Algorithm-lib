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
from typing import Optional, List, Union, Any
from dataclasses import dataclass
from enum import Enum


class BrowserType(Enum):
  """Supported browser types"""
  CHROME = "chrome"
  UNDETECTED_CHROME = "undetected_chrome"
  FIREFOX = "firefox"
  EDGE = "edge"


@dataclass
class BrowserConfig:
  """Configuration for browser initialization"""
  browser_type: BrowserType = BrowserType.UNDETECTED_CHROME
  headless: bool = False
  incognito: bool = True
  maximize: bool = False
  proxy: Optional[str] = None
  user_agent: Optional[str] = None
  window_size: tuple = (800, 600)
  disable_images: bool = False
  disable_javascript: bool = False


class WebDriver:
  """
    Enhanced Selenium WebDriver wrapper with common utilities
    for browser automation and web scraping.
    """

  DEFAULT_TIMEOUT = 30

  def __init__(self, config: BrowserConfig = BrowserConfig()) -> None:
    """
        Initialize the WebDriver with given configuration

        Args:
            config: BrowserConfig object with initialization parameters
        """
    self.config = config
    self.driver = self._initialize_driver()

  def _initialize_driver(self) -> webdriver:
    """Initialize the appropriate WebDriver based on configuration"""
    capabilities = DC.CHROME

    if self.config.browser_type == BrowserType.UNDETECTED_CHROME:
      options = uc.ChromeOptions()
    else:
      options = webdriver.ChromeOptions()

    # Common options
    if self.config.headless:
      options.add_argument('--headless')
      options.add_argument('--disable-gpu')

    if self.config.incognito:
      options.add_argument("--incognito")

    if self.config.proxy:
      options.add_argument(f'--proxy-server={self.config.proxy}')

    if self.config.user_agent:
      options.add_argument(f'--user-agent={self.config.user_agent}')

    if self.config.disable_images:
      options.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images": 2}
      )

    if self.config.disable_javascript:
      options.add_experimental_option(
        "prefs", {'profile.managed_default_content_settings.javascript': 2}
      )

    # Initialize the appropriate driver
    if self.config.browser_type == BrowserType.UNDETECTED_CHROME:
      driver = uc.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
        desired_capabilities=capabilities
      )
    else:
      driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
        desired_capabilities=capabilities
      )

    # Window management
    if self.config.maximize:
      driver.maximize_window()
    else:
      driver.set_window_size(*self.config.window_size)

    return driver

  # Element location methods
  def get_element(self, by: By, locator: str, timeout: int = DEFAULT_TIMEOUT) -> webdriver.Remote:
    """
        Wait for and return a single web element

        Args:
            by: Locator strategy (By.ID, By.XPATH, etc.)
            locator: Element locator string
            timeout: Maximum wait time in seconds

        Returns:
            WebElement object
        """
    return WebDriverWait(self.driver, timeout).until(
      EC.presence_of_element_located((by, locator))
    )

  def get_elements(self, by: By, locator: str, timeout: int = DEFAULT_TIMEOUT) -> List[webdriver.Remote]:
    """
        Wait for and return multiple web elements

        Args:
            by: Locator strategy (By.ID, By.XPATH, etc.)
            locator: Elements locator string
            timeout: Maximum wait time in seconds

        Returns:
            List of WebElement objects
        """
    return WebDriverWait(self.driver, timeout).until(
      EC.presence_of_all_elements_located((by, locator))
    )

  # Convenience methods for common locators
  def by_id(self, element_id: str, timeout: int = DEFAULT_TIMEOUT) -> webdriver.Remote:
    return self.get_element(By.ID, element_id, timeout)

  def by_name(self, name: str, timeout: int = DEFAULT_TIMEOUT) -> webdriver.Remote:
    return self.get_element(By.NAME, name, timeout)

  def by_class(self, class_name: str, timeout: int = DEFAULT_TIMEOUT) -> webdriver.Remote:
    return self.get_element(By.CLASS_NAME, class_name, timeout)

  def by_xpath(self, xpath: str, timeout: int = DEFAULT_TIMEOUT) -> webdriver.Remote:
    return self.get_element(By.XPATH, xpath, timeout)

  def by_css(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> webdriver.Remote:
    return self.get_element(By.CSS_SELECTOR, selector, timeout)

  def by_link_text(self, text: str, timeout: int = DEFAULT_TIMEOUT) -> webdriver.Remote:
    return self.get_element(By.LINK_TEXT, text, timeout)

  def by_partial_link_text(self, text: str, timeout: int = DEFAULT_TIMEOUT) -> webdriver.Remote:
    return self.get_element(By.PARTIAL_LINK_TEXT, text, timeout)

  def by_tag(self, tag_name: str, timeout: int = DEFAULT_TIMEOUT) -> webdriver.Remote:
    return self.get_element(By.TAG_NAME, tag_name, timeout)

  def by_aria_label(self, label: str, timeout: int = DEFAULT_TIMEOUT) -> webdriver.Remote:
    return self.get_element(By.CSS_SELECTOR, f'[aria-label="{label}"]', timeout)

  # Browser actions
  def open(self, url: str) -> None:
    """Navigate to the specified URL"""
    self.driver.get(url)

  def close(self) -> None:
    """Close the browser and quit the driver"""
    self.driver.quit()

  def refresh(self) -> None:
    """Refresh the current page"""
    self.driver.refresh()

  def back(self) -> None:
    """Navigate back in browser history"""
    self.driver.back()

  def forward(self) -> None:
    """Navigate forward in browser history"""
    self.driver.forward()

  # Element interactions
  def set_input(self, element: webdriver.Remote, text: str, clear: bool = True, submit: bool = False) -> None:
    """
        Set text in an input field

        Args:
            element: Input WebElement
            text: Text to input
            clear: Whether to clear the field first
            submit: Whether to submit after input (press Enter)
        """
    if clear:
      element.clear()
    element.send_keys(text)
    if submit:
      element.send_keys(Keys.ENTER)

  def click(self, element: webdriver.Remote) -> None:
    """Click on an element"""
    element.click()

  def hover(self, element: webdriver.Remote) -> None:
    """Hover over an element using JavaScript"""
    self.driver.execute_script("arguments[0].dispatchEvent(new Event('mouseover'));", element)

  # Page information
  def get_url(self) -> str:
    """Get current page URL"""
    return self.driver.current_url

  def get_title(self) -> str:
    """Get current page title"""
    return self.driver.title

  def get_page_source(self) -> str:
    """Get complete page HTML source"""
    return self.driver.page_source

  def get_screenshot(self, path: str) -> bool:
    """
        Take screenshot of current page

        Args:
            path: File path to save screenshot

        Returns:
            True if successful, False otherwise
        """
    return self.driver.save_screenshot(path)

  # Frame and window management
  def switch_to_frame(self, frame_reference: Union[str, webdriver.Remote]) -> None:
    """Switch to specified frame"""
    self.driver.switch_to.frame(frame_reference)

  def switch_to_default(self) -> None:
    """Switch back to default content"""
    self.driver.switch_to.default_content()

  def switch_to_window(self, window_handle: str) -> None:
    """Switch to specified browser window/tab"""
    self.driver.switch_to.window(window_handle)

  def new_tab(self, url: str = "") -> None:
    """Open new browser tab"""
    self.driver.execute_script(f"window.open('{url}');")

  def close_tab(self) -> None:
    """Close current browser tab"""
    self.driver.close()

  # JavaScript and advanced interactions
  def execute_script(self, script: str, *args) -> Any:
    """Execute JavaScript code"""
    return self.driver.execute_script(script, *args)

  def scroll_to(self, element: webdriver.Remote) -> None:
    """Scroll to make element visible"""
    self.driver.execute_script("arguments[0].scrollIntoView();", element)

  def scroll_to_bottom(self) -> None:
    """Scroll to bottom of page"""
    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  def scroll_to_top(self) -> None:
    """Scroll to top of page"""
    self.driver.execute_script("window.scrollTo(0, 0);")

  # Form handling
  def select_dropdown_by_value(self, element: webdriver.Remote, value: str) -> None:
    """Select dropdown option by value"""
    Select(element).select_by_value(value)

  def select_dropdown_by_index(self, element: webdriver.Remote, index: int) -> None:
    """Select dropdown option by index"""
    Select(element).select_by_index(index)

  def select_dropdown_by_text(self, element: webdriver.Remote, text: str) -> None:
    """Select dropdown option by visible text"""
    Select(element).select_by_visible_text(text)

  # Cookies management
  def get_cookies(self) -> List[dict]:
    """Get all browser cookies"""
    return self.driver.get_cookies()

  def get_cookie(self, name: str) -> Optional[dict]:
    """Get specific cookie by name"""
    return self.driver.get_cookie(name)

  def add_cookie(self, cookie_dict: dict) -> None:
    """Add a cookie to the browser"""
    self.driver.add_cookie(cookie_dict)

  def delete_cookie(self, name: str) -> None:
    """Delete a cookie by name"""
    self.driver.delete_cookie(name)

  def delete_all_cookies(self) -> None:
    """Delete all browser cookies"""
    self.driver.delete_all_cookies()

  # Alerts and popups
  def alert_accept(self) -> None:
    """Accept an alert"""
    self.driver.switch_to.alert.accept()

  def alert_dismiss(self) -> None:
    """Dismiss an alert"""
    self.driver.switch_to.alert.dismiss()

  def alert_text(self) -> str:
    """Get alert text"""
    return self.driver.switch_to.alert.text

  def alert_send_keys(self, text: str) -> None:
    """Send text to an alert"""
    self.driver.switch_to.alert.send_keys(text)

  # Browser information
  def get_window_size(self) -> dict:
    """Get current browser window size"""
    return self.driver.get_window_size()

  def set_window_size(self, width: int, height: int) -> None:
    """Set browser window size"""
    self.driver.set_window_size(width, height)

  def get_window_position(self) -> dict:
    """Get browser window position"""
    return self.driver.get_window_position()

  def set_window_position(self, x: int, y: int) -> None:
    """Set browser window position"""
    self.driver.set_window_position(x, y)

  # Wait conditions
  def wait_for_element_visible(self, by: By, locator: str, timeout: int = DEFAULT_TIMEOUT) -> webdriver.Remote:
    """Wait for element to be visible"""
    return WebDriverWait(self.driver, timeout).until(
      EC.visibility_of_element_located((by, locator))
    )

  def wait_for_element_clickable(self, by: By, locator: str, timeout: int = DEFAULT_TIMEOUT) -> webdriver.Remote:
    """Wait for element to be clickable"""
    return WebDriverWait(self.driver, timeout).until(
      EC.element_to_be_clickable((by, locator))
    )

  def wait_for_page_load(self, timeout: int = DEFAULT_TIMEOUT) -> bool:
    """Wait for page to fully load"""
    return WebDriverWait(self.driver, timeout).until(
      lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


class WebDriverExceptions:
  """Container for Selenium exception classes"""
  NoSuchWindow = NoSuchWindowException
  Timeout = TimeoutException
  WebDriver = WebDriverException
  NoSuchElement = NoSuchElementException
  ElementClickIntercepted = ElementClickInterceptedException
  ElementNotInteractable = ElementNotInteractableException
  StaleElement = StaleElementReferenceException
  InvalidSelector = InvalidSelectorException
  NoSuchFrame = NoSuchFrameException
  NoSuchAlert = NoSuchAlertException
  UnexpectedAlertPresent = UnexpectedAlertPresentException
  InvalidCookieDomain = InvalidCookieDomainException
  UnableToSetCookie = UnableToSetCookieException
  JavascriptError = JavascriptException