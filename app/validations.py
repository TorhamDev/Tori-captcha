import re


def validate_email(email: str) -> bool:
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    if re.match(email_regex, email):
        return True

    return False
