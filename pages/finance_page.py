from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chrome_config import get_chrome_options, create_driver
from config import BASE_URL, TIMEOUT


class FinancePage:
    """
    Creates an instance of FinancePage.

    Attributes:
        driver (WebDriver): The WebDriver instance.
    """

    driver = create_driver()

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = BASE_URL

        self.price_selector = (By.CSS_SELECTOR,
                               "#yDmH0d > c-wiz.zQTmif.SSPGKf.u5wqUe > div > div.e1AOyf > div > main > div.Gfxi4 > div.yWOrNb > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.QZMA8b > c-wiz > div > div:nth-child(1) > div > div.rPF6Lc > div > div:nth-child(1) > div > span > div > div")

    def wait_for_price_to_be_displayed(self):
        """
        Method to wait until the price element is displayed
        """
        WebDriverWait(self.driver, TIMEOUT).until(EC.presence_of_element_located(self.price_selector))

    def open_btc_page(self):
        """Method to open the page."""
        self.driver.get(self.url)

    def get_prices(self) -> float:
        """
        Method to find the price element and get the numeric value of the price.

        Returns:
            float: The numeric value of the price.
        """
        price_element = self.driver.find_element(*self.price_selector)
        price_text = price_element.text
        price = float(price_text.replace(',', ''))  # Handle thousands separator if needed
        return price
