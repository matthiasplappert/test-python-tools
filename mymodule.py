import requests


def get_ip():
    """Get my current external IP."""
    return requests.get("https://ipv4.icanhazip.com/").text.strip()
