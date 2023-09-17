from dotenv import load_dotenv
import os

load_dotenv()


class Environment:
    BREVO_API_KEY = os.environ.get("BREVO_API_KEY")
    JSON_FILE_PATH = os.environ.get("JSON_FILE_PATH")
    USER_AGENT = os.environ.get("USER_AGENT")
    SENDER = os.environ.get("SENDER")
    RECEIVER_NAMES = os.environ.get("RECEIVER_NAMES")
    RECEIVER_EMAILS = os.environ.get("RECEIVER_EMAILS")
