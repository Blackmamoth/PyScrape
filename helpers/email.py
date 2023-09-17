import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from common.models import Product
from helpers.console import ConsoleLogger
from helpers.environment import Environment


def replace_html_placeholders(product: Product, current_price: int) -> str:
    replacement_dict = {
        "$PRODUCT_NAME": product.name,
        "$PRODUCT_LINK": product.url,
        "$DESIRED_PRICE": f"₹{product.price_required}",
        "$CURRENT_PRICE": f"₹{current_price}",
    }
    with open("price_drop.html") as html_file:
        html_text = html_file.read()
    for placeholder, replacement in replacement_dict.items():
        html_text = html_text.replace(str(placeholder), str(replacement))
    return html_text


def send_email(product: Product, current_price: int) -> str:
    try:
        html = replace_html_placeholders(product, current_price)
        brevo_config = sib_api_v3_sdk.Configuration()
        brevo_config.api_key["api-key"] = Environment.BREVO_API_KEY
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
            sib_api_v3_sdk.ApiClient(brevo_config)
        )
        names = Environment.RECEIVER_NAMES.split(",")
        emails = Environment.RECEIVER_EMAILS.split(",")
        to = [{"name": name, "email": email} for name, email in zip(names, emails)]
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=to,
            html_content=html,
            sender={"email": Environment.SENDER},
            subject=f"Price for one of your desired items dropped.",
        )
        api_instance.send_transac_email(send_smtp_email)
        ConsoleLogger.info("Email sent successfully.")
    except ApiException as e:
        ConsoleLogger.error("Could not send email.")
        ConsoleLogger.error(e.reason)
