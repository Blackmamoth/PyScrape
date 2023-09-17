from bs4 import BeautifulSoup
from helpers.helper import get_flipkart_list
from helpers.console import ConsoleLogger
from helpers.environment import Environment
from common.models import Product
import requests
from requests.exceptions import HTTPError
from helpers.email import send_email


class FlipkartScraper:
    def __init__(self) -> None:
        self.product_list = get_flipkart_list()
        ConsoleLogger.info("Flipkart's product list acquired.")
        for product in self.product_list:
            self.scrape(product)

    def scrape(self, product: Product):
        try:
            ConsoleLogger.info(f"Scraping {product.name}")
            request = requests.get(
                product.url, headers={"User-Agent": Environment.USER_AGENT}
            )
            soup = BeautifulSoup(request.text, "lxml")
            price = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
            if price is None:
                ConsoleLogger.error("Could not find the element with price.")
                return
            current_price = int(price.text.replace("₹", "").replace(",", ""))
            ConsoleLogger.info(f"Current price  : ₹{current_price}")
            ConsoleLogger.info(f"Required price : ₹{product.price_required}")
            if current_price <= product.price_required:
                ConsoleLogger.info("Sending Email...")
                send_email(product, current_price)
        except HTTPError as http_error:
            ConsoleLogger.error(http_error.strerror)
