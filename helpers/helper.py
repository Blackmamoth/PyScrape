import json
from common.models import Product
from helpers.environment import Environment


def get_amazon_list() -> list[Product]:
    file_path = Environment.JSON_FILE_PATH
    with open(file_path) as f:
        json_data = json.load(f)
        amazon_list = json_data["amazon"]
    product_list: list[Product] = []
    for item in amazon_list:
        product = Product(
            name=item["name"], price_required=item["price_required"], url=item["url"]
        )
        product_list.append(product)
    return product_list


def get_flipkar_list() -> list[Product]:
    file_path = Environment.JSON_FILE_PATH
    with open(file_path) as f:
        json_data = json.load(f)
        flipkart_list = json_data["flipkart"]
    product_list: list[Product] = []
    for item in flipkart_list:
        product = Product(
            name=item["name"], price_required=item["price_required"], url=item["url"]
        )
        product_list.append(product)
    return product_list
